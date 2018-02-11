import datetime
from salamandra import *
from define_parameters import *
from standard_cell import *

############################# main #############################
def main():
    scm = {}
    SCM_design(param,scm)
    write_verilog_file(param,scm)

########################## SCM design ##########################
def SCM_design(param, scm):
    ADDR_WIDTH = param['ADDR_WIDTH']
    
    ################# define modules, pins and main nets ##################
    
    ##### define the TOP module
    scm['TOP'] = Component(param['TOPLEVEL'])
    TOP = scm['TOP']
    for pin in ['CLK', 'WE', 'RE']:
        TOP.add_pin(Input(pin))
        TOP.add_net(Net(pin))
    for pin in ['WADDR', 'RADDR']:
        for i in range(ADDR_WIDTH):
            TOP.add_pin(Input(pin+str([i])))
            TOP.add_net(Net(pin+str([i])))
    for i in range(param['DATA_WIDTH']):
        TOP.add_pin(Input('DIN'+str([i])))
        TOP.add_pin(Output('DOUT'+str([i])))
        TOP.add_net(Net('DIN'+str([i])))
        TOP.add_net(Net('DOUT'+str([i])))


    ##### define a bitslice    
    scm['bitslice'] = Component('bitslice')
    bitslice = scm['bitslice']
    bitslice.add_pin(Input('DIN'))
    bitslice.add_pin(Output('DOUT'))
    bitslice.add_net(Net('DIN'))
    bitslice.add_net(Net('DOUT'))
    for pin in ['DGWCLK', 'RWL']:
        for i in range(2**ADDR_WIDTH):
            bitslice.add_pin(Input(pin+str([i])))
            bitslice.add_net(Net(pin+str([i])))        


    ##### define a read_mux    
    scm['read_mux'] = Component('read_mux')
    read_mux = scm['read_mux']
    read_mux.add_pin(Output('DOUT'))
    read_mux.add_net(Net('DOUT'))
    for pin in ['MemoryLatch', 'RWL']:
        for i in range(2**ADDR_WIDTH):
            read_mux.add_pin(Input(pin+str([i])))
            read_mux.add_net(Net(pin+str([i])))
    
    ##### define a welltap    
    welltap = standard_cell['well_tap']

    ##### define a MemoryLatch_reg
    MemoryLatch_reg = standard_cell['latch']

    ##### define a GDIN_reg
    GDIN_reg = standard_cell['flipflop']

    ##### define a level_1    
    level_1 = standard_cell['NAND2']


    ################# add components, internal nets and connectivity to modules ##################

    # add components to TOP module
    for i in range(param['DATA_WIDTH']):
        if (i%8) == 0:
            TOP.add_component(welltap, 'welltap'+str([i//8]))
        
        TOP.add_component(bitslice, 'bitslice'+str([i]))
        TOP.connect('DIN'+str([i]), 'bitslice'+str([i])+'.DIN')
        TOP.connect('DOUT'+str([i]), 'bitslice'+str([i])+'.DOUT')
        for pin in ['DGWCLK', 'RWL']:
            for j in range(2**ADDR_WIDTH):
                if i == 0:
                    TOP.add_net(Net(pin+str([j])))
                TOP.connect(pin+str([j]), 'bitslice'+str([i])+'.'+pin+str([j]))
        
    # add components to bitslice module
    bitslice.add_component(read_mux, 'read_mux')
    bitslice.connect('DOUT', 'DOUT')    
    bitslice.connect('DOUT', 'read_mux.DOUT')
    bitslice.add_component(GDIN_reg, 'GDIN_reg')
    bitslice.connect('DIN', 'DIN')    
    bitslice.connect('DIN', 'GDIN_reg.D')
    bitslice.add_net(Net('GDIN'))
    bitslice.connect('GDIN', 'GDIN_reg.Q')

    for i in range(2**ADDR_WIDTH):
        bitslice.add_component(MemoryLatch_reg, 'MemoryLatch_reg'+str([i]))
        for net in ['MemoryLatch']:
            bitslice.add_net(Net(net+str([i])))
        bitslice.connect('GDIN', 'MemoryLatch_reg'+str([i])+'.D')         
        for net in [('MemoryLatch','Q'), ('DGWCLK', 'G')]:
            bitslice.connect(net[0]+str([i]), 'MemoryLatch_reg'+str([i])+'.'+net[1]) #conectivty to MemoryLatch_reg
        for net in ['MemoryLatch', 'RWL']:
            bitslice.connect(net+str([i]), 'read_mux.'+net+str([i]))    #conectivty to read_mux
        for net in ['RWL', 'DGWCLK']:
            bitslice.connect(net+str([i]), net+str([i]))

    # add components to read_mux module
    for i in range(2**ADDR_WIDTH):
        read_mux.add_component(level_1, 'level_1_'+str([i]))
        read_mux.add_net(Net('level_1_out_'+str([i])))
        for pin in [('MemoryLatch', 'A'), ('RWL', 'B'), ('level_1_out_', 'Y')]:
            read_mux.connect(pin[0]+str([i]), 'level_1_'+str([i])+'.'+pin[1])

###################### write verilog file ######################
def write_verilog_file(param,scm):
    verilog_file_name = "%s.post_py.v" %param['TOPLEVEL']
    tcl_file_name = '%s_cells_position.tcl' %param['TOPLEVEL']
    
    header_comment_text = []
    module_scm_text = scm['TOP'].write_verilog()

    header_comment(header_comment_text, param, module_scm_text)    
    
    verilog_file=open(verilog_file_name,'w')

    for line in header_comment_text:
        verilog_file.write(line)
    
    for module in scm.values():
        for line in module.write_verilog():
            verilog_file.write(line)
    
    verilog_file.close()

##################### write header comment #####################
def header_comment(text, param, module_scm_text):
    text.append('/*\n')
    text.append('###############################################################\n')
    text.append('#\tGenerated by:\t\tEnICS SCM Compiler v1.1\n')
    text.append('#\tGenerated on:\t\t'+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'\n')
    text.append('#\tDesign:\t\t\t\t'+param['TOPLEVEL']+'\n')
    text.append('#\n')
    text.append('#\tDimensions:\n')
    text.append('#\tDATA WIDTH:\t\t\t'+str(param['DATA_WIDTH'])+'\n')
    text.append('#\tNUM ROWS:\t\t\t'+str(2**param['ADDR_WIDTH'])+'\n')
    text.append('#\n')
    text.append('#\tlines in lists:\n')    
    text.append('#\tmodule_scm_text:\t'+str(len(module_scm_text))+'\n')
    text.append('###############################################################\n')
    text.append('*/\n')    


if __name__ == '__main__':
    main()

