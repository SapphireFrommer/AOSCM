import datetime
from salamandra import *
from define_parameters import *
from standard_cell import *

################################################################
###########################   main   ###########################
################################################################
def main():
    scm = {}
    SCM_design(param,scm)
    write_verilog_file(param,scm)

################################################################
########################   SCM design   ########################
################################################################
def SCM_design(param, scm):
    SCM_design_define_components(param, scm)        # define each component itself
    SCM_design_components_instances(param, scm)     # add components, internal nets and connectivity to modules

######################################################################################
###############   define modules, pins and main nets & connectivity   ################
######################################################################################
def SCM_design_define_components(param, scm):
    ADDR_WIDTH = param['ADDR_WIDTH']
    
    ##### define the TOP module
    scm['TOP'] = Component(param['TOPLEVEL'])
    TOP = scm['TOP']
    for pin in ['CLK', 'WE', 'RE']:
        TOP.add_pin(Input(pin))
        TOP.add_net(Net(pin))
        TOP.connect(pin, pin)
    for pin in ['WADDR', 'RADDR']:
        for i in range(ADDR_WIDTH):
            TOP.add_pin(Input(pin+str([i])))
            TOP.add_net(Net(pin+str([i])))
            TOP.connect(pin+str([i]), pin+str([i]))
    for i in range(param['DATA_WIDTH']):
        TOP.add_pin(Input('DIN'+str([i])))
        TOP.add_pin(Output('DOUT'+str([i])))
        TOP.add_net(Net('DIN'+str([i])))
        TOP.add_net(Net('DOUT'+str([i])))
        TOP.connect('DIN'+str([i]), 'DIN'+str([i]))
        TOP.connect('DOUT'+str([i]), 'DOUT'+str([i]))

    ##### define a bitslice    
    scm['bitslice'] = Component('bitslice')
    bitslice = scm['bitslice']
    bitslice.add_pin(Input('DIN'))
    bitslice.add_pin(Output('DOUT'))
    bitslice.add_net(Net('DIN'))
    bitslice.add_net(Net('DOUT'))
    bitslice.connect('DIN', 'DIN')
    bitslice.connect('DOUT', 'DOUT')
    bitslice.add_pin(Input('clk'))
    bitslice.add_net(Net('clk'))   
    bitslice.connect('clk', 'clk')
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
    
    ##### define a MidGap_DGWCLK    
    scm['MidGap_DGWCLK'] = Component('MidGap_DGWCLK')
    MidGap_DGWCLK = scm['MidGap_DGWCLK']
    MidGap_DGWCLK.add_pin(Input('clk'))
    MidGap_DGWCLK.add_net(Net('clk'))
    MidGap_DGWCLK.connect('clk', 'clk')
    MidGap_DGWCLK.add_pin(Input('SE'))
    MidGap_DGWCLK.add_net(Net('SE'))
    MidGap_DGWCLK.connect('SE', 'SE')
    for i in range(2**ADDR_WIDTH):
        MidGap_DGWCLK.add_pin(Input('E'+str([i])))
        MidGap_DGWCLK.add_net(Net('E'+str([i])))
        MidGap_DGWCLK.connect('E'+str([i]), 'E'+str([i]))
    for pin in ['DGWClkLeftNet', 'DGWClkRightNet']:
        for i in range(2**ADDR_WIDTH):
            MidGap_DGWCLK.add_pin(Output(pin+str([i])))
            MidGap_DGWCLK.add_net(Net(pin+str([i])))
            MidGap_DGWCLK.connect(pin+str([i]), pin+str([i]))

    ##### define a row_decoder    
    scm['row_decoder'] = Component('row_decoder')
    row_decoder = scm['row_decoder']
    for i in range(ADDR_WIDTH):
        row_decoder.add_pin(Input('decoder_in'+str([i])))
        row_decoder.add_net(Net('decoder_in'+str([i])))
        row_decoder.connect('decoder_in'+str([i]), 'decoder_in'+str([i]))
    for i in range(2**ADDR_WIDTH):
        row_decoder.add_pin(Output('decoder_out'+str([i])))
        row_decoder.add_net(Net('decoder_out'+str([i])))
        row_decoder.connect('decoder_out'+str([i]), 'decoder_out'+str([i]))

    ##### define a welltap_strip    
    scm['welltap_strip'] = Component('welltap_strip')
    welltap_strip = scm['welltap_strip']


    ##### define a rwlBuff_strip    
    scm['rwlBuff_strip'] = Component('rwlBuff_strip')
    rwlBuff_strip = scm['rwlBuff_strip']
    for i in range(2**ADDR_WIDTH):
        rwlBuff_strip.add_pin(Input('IN'+str([i])))
        rwlBuff_strip.add_pin(Output('OUT'+str([i])))
        rwlBuff_strip.add_net(Net('IN'+str([i])))
        rwlBuff_strip.add_net(Net('OUT'+str([i])))
        rwlBuff_strip.connect('IN'+str([i]), 'IN'+str([i]))
        rwlBuff_strip.connect('OUT'+str([i]), 'OUT'+str([i]))
        

##############################################################################################
###############   add components, internal nets and connectivity to modules   ################
##############################################################################################
def SCM_design_components_instances(param, scm):

    SCM_design_components_instances_TOP(param, scm)
    SCM_design_components_instances_bitslice(param, scm)
    SCM_design_components_instances_read_mux(param, scm)
    SCM_design_components_instances_MidGap_DGWCLK(param, scm)
    SCM_design_components_instances_row_decoder(param, scm)
    SCM_design_components_instances_welltap_strip(param, scm)
    SCM_design_components_instances_rwlBuff_strip(param, scm)


##########################################################
# add components to TOP module
##########################################################
def SCM_design_components_instances_TOP(param, scm):
    # aliases:
    ADDR_WIDTH = param['ADDR_WIDTH']
    TOP = scm['TOP']
    welltap_strip = scm['welltap_strip']
    bitslice = scm['bitslice']
    rwlBuff_strip = scm['rwlBuff_strip']
    MidGap_DGWCLK = scm['MidGap_DGWCLK']
    row_decoder = scm['row_decoder']
    read_mux = scm['read_mux']
    latch_clock_gate = sc['latch_clock_gate']['component']

    for i in range(param['DATA_WIDTH']):
        if (i%8) == 0:
            TOP.add_component(welltap_strip, 'welltap_strip'+str([i//8]))

        # rwlBuff_strips (it's only a draft)
        K_RWL = param['DATA_WIDTH']//4
        if (i%K_RWL == 0) & (i != 0) & (i < param['DATA_WIDTH']/2):   # left side
            TOP.add_component(rwlBuff_strip, 'rwlBuff_strip'+str([(i//K_RWL)-1]))
            for row in range(2**ADDR_WIDTH):
                TOP.add_net(Net('rwlBuffNet'+str([(i//K_RWL)-1])+str([row])))
                TOP.connect('rwlBuffNet'+str([(i//K_RWL)-1])+str([row]), 'rwlBuff_strip'+str([(i//K_RWL)-1])+'.OUT'+str([row]))
                TOP.add_net(Net('rwlBuffNet'+str([(i//K_RWL)])+str([row])))
                TOP.connect('rwlBuffNet'+str([(i//K_RWL)])+str([row]), 'rwlBuff_strip'+str([(i//K_RWL)-1])+'.IN'+str([row]))

        if (i == param['DATA_WIDTH']/2):    # 2 middle
            TOP.add_component(rwlBuff_strip, 'rwlBuff_strip'+str([(i//K_RWL)-1]))
            TOP.add_component(rwlBuff_strip, 'rwlBuff_strip'+str([(i//K_RWL)]))
            for row in range(2**ADDR_WIDTH):
                TOP.add_net(Net('decoder_read_out'+str([row])))
                
                TOP.connect('decoder_read_out'+str([row]), 'rwlBuff_strip'+str([(i//K_RWL)-1])+'.IN'+str([row]))                
                TOP.connect('rwlBuffNet'+str([(i//K_RWL)-1])+str([row]), 'rwlBuff_strip'+str([(i//K_RWL)-1])+'.OUT'+str([row]))


                TOP.connect('decoder_read_out'+str([row]), 'rwlBuff_strip'+str([(i//K_RWL)])+'.IN'+str([row]))
                TOP.add_net(Net('rwlBuffNet'+str([(i//K_RWL)])+str([row])))
                TOP.connect('rwlBuffNet'+str([(i//K_RWL)])+str([row]), 'rwlBuff_strip'+str([(i//K_RWL)])+'.OUT'+str([row]))


        if (i%K_RWL == 0) & (i > param['DATA_WIDTH']/2):   # right side
            TOP.add_component(rwlBuff_strip, 'rwlBuff_strip'+str([(i//K_RWL)]))
            for row in range(2**ADDR_WIDTH):
                TOP.connect('rwlBuffNet'+str([(i//K_RWL)-1])+str([row]), 'rwlBuff_strip'+str([(i//K_RWL)])+'.IN'+str([row]))
                TOP.add_net(Net('rwlBuffNet'+str([(i//K_RWL)])+str([row])))
                TOP.connect('rwlBuffNet'+str([(i//K_RWL)])+str([row]), 'rwlBuff_strip'+str([(i//K_RWL)])+'.OUT'+str([row]))
            


        # bitslices
        TOP.add_component(bitslice, 'bitslice'+str([i]))
        TOP.connect('DIN'+str([i]), 'bitslice'+str([i])+'.DIN')
        TOP.connect('DOUT'+str([i]), 'bitslice'+str([i])+'.DOUT')

        # DGWCLK net to bitslice connectivity
        if i < (param['DATA_WIDTH']/2):
            for j in range(2**ADDR_WIDTH):
                if i == 0:
                    TOP.add_net(Net('DGWCLKLeftNet'+str([j])))
                TOP.connect('DGWCLKLeftNet'+str([j]), 'bitslice'+str([i])+'.DGWCLK'+str([j]))
        else:
            for j in range(2**ADDR_WIDTH):
                if i == param['DATA_WIDTH']/2:
                    TOP.add_net(Net('DGWClkRightNet'+str([j])))
                TOP.connect('DGWClkRightNet'+str([j]), 'bitslice'+str([i])+'.DGWCLK'+str([j]))

        if i == ((param['DATA_WIDTH']/2)-1):    # MidGap
            TOP.add_component(MidGap_DGWCLK, 'MidGap_DGWCLK')
            TOP.add_net(Net('MidGap_DGWCLK_clk'))
            TOP.connect('MidGap_DGWCLK_clk', 'MidGap_DGWCLK.clk')
            for j in range(2**ADDR_WIDTH):
                if i < (param['DATA_WIDTH']/2):
                    TOP.connect('DGWCLKLeftNet'+str([j]), 'MidGap_DGWCLK.DGWClkLeftNet'+str([j]))
                else:
                    TOP.connect('DGWClkRightNet'+str([j]), 'MidGap_DGWCLK.DGWClkRightNet'+str([j]))

            TOP.add_component(row_decoder, 'read_decoder')                

            TOP.add_component(row_decoder, 'write_decoder')


    # bitslices RWL connectivity
    for row in range(2**ADDR_WIDTH):
        for col in range(param['DATA_WIDTH']):
            TOP.connect('rwlBuffNet'+str([col//K_RWL])+str([row]), 'bitslice'+str([col])+'.'+'RWL'+str([row]))
        TOP.connect('decoder_read_out'+str([row]), 'read_decoder''.decoder_out'+str([row]))
    
    # first level clock gates
    TOP.add_net(Net('SE'))
    
    for gate in ['GDINCLK_gate', 'GWCLK_gate', 'GRCLK_gate']:
        TOP.add_component(latch_clock_gate, gate)
        TOP.connect('CLK', gate+'.CK')
        TOP.connect('SE', gate+'.SE')

    TOP.connect('WE', 'GDINCLK_gate.E')
    TOP.connect('WE', 'GWCLK_gate.E')
    TOP.connect('RE', 'GRCLK_gate.E')


    TOP.add_net(Net('GDINCLK'))
    TOP.add_net(Net('GWCLK'))
    TOP.add_net(Net('GRCLK'))
    TOP.connect('GDINCLK', 'GDINCLK_gate.ECK')
    TOP.connect('GWCLK', 'GWCLK_gate.ECK')
    TOP.connect('GRCLK', 'GRCLK_gate.ECK')


##########################################################
# add components to bitslice module
##########################################################
def SCM_design_components_instances_bitslice(param, scm):
    # aliases:
    ADDR_WIDTH = param['ADDR_WIDTH']
    bitslice = scm['bitslice']
    read_mux = scm['read_mux']
    MemoryLatch_reg = sc['latch']['component']
    GDIN_reg = sc['flipflop']['component']


    bitslice.add_component(read_mux, 'read_mux')
    bitslice.connect('DOUT', 'read_mux.DOUT')
    bitslice.add_component(GDIN_reg, 'GDIN_reg')
    bitslice.connect('DIN', 'GDIN_reg.'+sc['flipflop']['in'])
    bitslice.add_net(Net('GDIN'))
    bitslice.connect('GDIN', 'GDIN_reg.'+sc['flipflop']['out'])
    bitslice.connect('clk', 'GDIN_reg.'+sc['flipflop']['clk'])

    for i in range(2**ADDR_WIDTH):
        bitslice.add_component(MemoryLatch_reg, 'MemoryLatch_reg'+str([i]))
        for net in ['MemoryLatch']:
            bitslice.add_net(Net(net+str([i])))
        bitslice.connect('GDIN', 'MemoryLatch_reg'+str([i])+'.'+sc['latch']['in'])         
        for net in [('MemoryLatch',sc['latch']['out']), ('DGWCLK', sc['latch']['clk'])]:
            bitslice.connect(net[0]+str([i]), 'MemoryLatch_reg'+str([i])+'.'+net[1]) #conectivty to MemoryLatch_reg
        for net in ['MemoryLatch', 'RWL']:
            bitslice.connect(net+str([i]), 'read_mux.'+net+str([i]))    #conectivty to read_mux
        for net in ['RWL', 'DGWCLK']:
            bitslice.connect(net+str([i]), net+str([i]))


##########################################################
# add components to read_mux module
##########################################################
def SCM_design_components_instances_read_mux(param, scm):
    # aliases:
    ADDR_WIDTH = param['ADDR_WIDTH']
    read_mux = scm['read_mux']
    NAND2 = sc['NAND2']['component']
    NOR2 = sc['NOR2']['component']
    INV_OUT_GATE = sc['inverter']['component']
    buffer = sc['buffer']['component']


    for level in range(1, ADDR_WIDTH+2):

        if level == 1:      # add and connect level_1 NAND2
            for i in range(2**ADDR_WIDTH):
                read_mux.add_component(NAND2, 'level'+str([level])+str([i]))
                read_mux.add_net(Net('w'+str([level-1])+str([i])))
                for pin in [('MemoryLatch', sc['NAND2']['in_1']), ('RWL', sc['NAND2']['in_2']), ('w'+str([level-1]), sc['NAND2']['out'])]:
                    read_mux.connect(pin[0]+str([i]), 'level'+str([level])+str([i])+'.'+pin[1])

        if level == 2:      # add and connect level_2 NAND2
            for i in range((2**ADDR_WIDTH)>>1):
                read_mux.add_component(NAND2, 'level'+str([level])+str([i]))
                read_mux.add_net(Net('w'+str([level-1])+str([i])))
                for pin in [('w'+str([level-2])+str([2*i]), sc['NAND2']['in_1']), ('w'+str([level-2])+str([2*i+1]), sc['NAND2']['in_2']), ('w'+str([level-1])+str([i]), sc['NAND2']['out'])]:
                    read_mux.connect(pin[0], 'level'+str([level])+str([i])+'.'+pin[1])

        if (level%2) & (level != 1):        # add and connect levels 3,5,7..... -> in odd levels there are NOR2 gates
            for i in range((2**ADDR_WIDTH)>>(level-1)):
                read_mux.add_component(NOR2, 'level'+str([level])+str([i]))
                read_mux.add_net(Net('w'+str([level-1])+str([i])))
                for pin in [('w'+str([level-2])+str([2*i]), sc['NOR2']['in_1']), ('w'+str([level-2])+str([2*i+1]), sc['NOR2']['in_2']), ('w'+str([level-1])+str([i]), sc['NOR2']['out'])]:
                    read_mux.connect(pin[0], 'level'+str([level])+str([i])+'.'+pin[1])            

        if (level%2 == 0) & (level != 2):       # add and connect levels 4,6,8..... -> in even levels there are NAND2 gates
            for i in range((2**ADDR_WIDTH)>>(level-1)):
                read_mux.add_component(NOR2, 'level'+str([level])+str([i]))
                read_mux.add_net(Net('w'+str([level-1])+str([i])))
                for pin in [('w'+str([level-2])+str([2*i]), sc['NOR2']['in_1']), ('w'+str([level-2])+str([2*i+1]), sc['NOR2']['in_2']), ('w'+str([level-1])+str([i]), sc['NOR2']['out'])]:
                    read_mux.connect(pin[0], 'level'+str([level])+str([i])+'.'+pin[1])     
    
    # last inverter or buffer
    if ((ADDR_WIDTH+1)%2 == 1):     
        read_mux.add_component(INV_OUT_GATE, 'inv_out')
        for pin in [('w'+str([ADDR_WIDTH])+'[0]', sc['inverter']['in']), ('DOUT', sc['inverter']['out'])]:
            read_mux.connect(pin[0], 'inv_out.'+pin[1])
    elif ((ADDR_WIDTH+1)%2 == 0):
        read_mux.add_component(buffer, 'buffer_out')
        for pin in [('w'+str([ADDR_WIDTH])+'[0]', sc['buffer']['in']), ('DOUT', sc['buffer']['out'])]:
            read_mux.connect(pin[0], 'buffer_out.'+pin[1])


##########################################################
# add components to MidGap_DGWCLK module
##########################################################
def SCM_design_components_instances_MidGap_DGWCLK(param, scm):
    # aliases:
    ADDR_WIDTH = param['ADDR_WIDTH']
    MidGap_DGWCLK = scm['MidGap_DGWCLK']
    buffer = sc['buffer']['component']
    latch_clock_gate = sc['latch_clock_gate']['component']

    for i in range(2**ADDR_WIDTH):
        MidGap_DGWCLK.add_component(buffer, 'DGWClkLeftBuff'+str([i]))
        MidGap_DGWCLK.add_component(latch_clock_gate, 'DGWCLK_gate'+str([i]))
        MidGap_DGWCLK.add_component(buffer, 'DGWClkRightBuff'+str([i]))
        
        MidGap_DGWCLK.add_net(Net('ECK'+str([i])))
        MidGap_DGWCLK.connect('ECK'+str([i]), 'DGWCLK_gate'+str([i])+'.'+sc['latch_clock_gate']['out'])
        MidGap_DGWCLK.connect('ECK'+str([i]), 'DGWClkLeftBuff'+str([i])+'.'+sc['buffer']['in'])
        MidGap_DGWCLK.connect('ECK'+str([i]), 'DGWClkRightBuff'+str([i])+'.'+sc['buffer']['in'])
        
        MidGap_DGWCLK.connect('E'+str([i]), 'DGWCLK_gate'+str([i])+'.'+sc['latch_clock_gate']['E'])
        MidGap_DGWCLK.connect('clk', 'DGWCLK_gate'+str([i])+'.'+sc['latch_clock_gate']['clk'])
        
        for net in ['DGWClkLeft', 'DGWClkRight']:
            MidGap_DGWCLK.connect(net+'Net'+str([i]), net+'Buff'+str([i])+'.'+sc['buffer']['out'])

##########################################################
# add components to row_decoder module
##########################################################
def SCM_design_components_instances_row_decoder(param, scm):
    pass

##########################################################
# add components to welltap_strip module
##########################################################
def SCM_design_components_instances_welltap_strip(param, scm):
    # aliases:
    ADDR_WIDTH = param['ADDR_WIDTH']
    welltap_strip = scm['welltap_strip']

    for i in range(2**ADDR_WIDTH):
        welltap_strip.add_component(sc['well_tap'], 'welltap'+str([i]))

##########################################################
# add components to rwlBuff_strip module
##########################################################
def SCM_design_components_instances_rwlBuff_strip(param, scm):
    # aliases:
    ADDR_WIDTH = param['ADDR_WIDTH']
    rwlBuff_strip = scm['rwlBuff_strip']
    buffer = sc['buffer']['component']

    for i in range(2**ADDR_WIDTH):
        rwlBuff_strip.add_component(buffer, 'rwlBuff'+str([i]))
        for net in [('IN', sc['buffer']['in']), ('OUT', sc['buffer']['out'])]:
            rwlBuff_strip.connect(net[0]+str([i]), 'rwlBuff'+str([i])+'.'+net[1])


################################################################
####################   write verilog file   ####################
################################################################
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

################################################################
###################   write header comment   ###################
################################################################
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

