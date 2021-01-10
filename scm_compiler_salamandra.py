import sys, os
import datetime
sys.path.append(os.path.abspath('submodules/salamandra'))
from salamandra import *
from define_parameters import *

from standard_cell import *


################################################################
###########################   main   ###########################
################################################################
def main():
    scm = {}
    SCM_design(params,scm)
    write_verilog_file(params,scm)
    write_tcl(params,scm)

################################################################
########################   SCM design   ########################
################################################################
def SCM_design(params, scm):
    SCM_design_define_components(params, scm)        # define each component itself
    SCM_design_components_instances(params, scm)     # add components, internal nets and connectivity to modules
    scm['TOP'].uniq()
    for module in sorted(scm['TOP'].get_subcomponents_dict().keys()):
        print(module +'\t->\t'+ str(scm['TOP'].get_subcomponents_dict()[module]))
    #print(scm['TOP'].get_subcomponents_dict())

######################################################################################
###############   define modules, pins and main nets & connectivity   ################
######################################################################################
def SCM_design_define_components(params, scm):
    ADDR_WIDTH = params['ADDR_WIDTH']
    
    ##### define the TOP module
    scm['TOP'] = ComponentXY(params['TOPLEVEL'])
    TOP = scm['TOP']
    TOP.add_pin(Input('DIN'))
    TOP.add_pin(Output('DOUT'))
    TOP.add_pin(Input('clk'))
    for pin in ['DGWCLK', 'RWL']:
        TOP.add_pinbus(Bus(Input, pin, 2**ADDR_WIDTH))

    ##### define a bitslice   
    scm['bitslice'] = ComponentXY('bitslice')
    bitslice = scm['bitslice']
    bitslice.add_pin(Input('DIN'))
    bitslice.add_pin(Output('DOUT'))
    bitslice.add_pin(Input('clk'))
    for pin in ['DGWCLK', 'RWL']:
        bitslice.add_pinbus(Bus(Input, pin, 2**ADDR_WIDTH))
    

    ##### define a read_mux    
    scm['read_mux'] = ComponentXY('read_mux')
    read_mux = scm['read_mux']
    read_mux.add_pin(Output('DOUT'))
    for pin in ['MemoryLatch', 'RWL']:
        read_mux.add_pinbus(Bus(Input, pin, 2**ADDR_WIDTH))
    
        

##############################################################################################
###############   add components, internal nets and connectivity to modules   ################
##############################################################################################
def SCM_design_components_instances(params, scm):

    SCM_design_components_instances_read_mux(params, scm)
    SCM_design_components_instances_bitslice(params, scm)
    SCM_design_components_instances_TOP(params, scm)


##########################################################
# add components to TOP module
##########################################################
def SCM_design_components_instances_TOP(params, scm):
    # aliases:
    ADDR_WIDTH = params['ADDR_WIDTH']
    TOP = scm['TOP']
    
    bitslice = scm['bitslice']
    # latch_clock_gate = sc['latch_clock_gate']['component']

    # instances width:
    bitslice.calc_component_dimensions()

    #########################################################
    #		components										#
    #########################################################
    xcoord = 0.0
    ycoord = 0.0

    
    TOP.add_component(bitslice, 'bitslice', xcoord, ycoord)

    TOP.set_pin_position('DIN', xcoord+3.5, ycoord, 'BOTTOM', 2)     
    TOP.set_pin_position('clk', xcoord+2.5, ycoord, 'BOTTOM', 2)     
    TOP.set_pin_position('DOUT', xcoord+3.7, ycoord, 'TOP', 2)
    for row in range(2**ADDR_WIDTH):
        TOP.set_pin_position('RWL'+str([row]), xcoord, ycoord + 0.65, 'LEFT', 2)
        TOP.set_pin_position('DGWCLK'+str([row]), xcoord, ycoord + 1.15, 'LEFT', 2)
        ycoord += sc['site']



    #########################################################
    #		connectivity									#
    #########################################################

    TOP.connect('DIN', 'bitslice.DIN')
    TOP.connect('DOUT', 'bitslice.DOUT')
    TOP.connect('clk', 'bitslice.clk')
    for row in range(2**ADDR_WIDTH):
        TOP.connect('DGWCLK'+str([row]), 'bitslice.DGWCLK'+str([row]))
        TOP.connect('RWL'+str([row]), 'bitslice.RWL'+str([row]))


##########################################################
# add components to bitslice module
##########################################################
def SCM_design_components_instances_bitslice(params, scm):
    # aliases:
    ADDR_WIDTH = params['ADDR_WIDTH']
    bitslice = scm['bitslice']
    read_mux = scm['read_mux']
    MemoryLatch_reg = sc['latch']['component']
    GDIN_reg = sc['flipflop']['component']

    # instances names:
    MemoryLatch_reg_name = 'MemoryLatch_reg_%0'+str(len(str(2**ADDR_WIDTH)))+'d'

    xcoord = 0.0
    ycoord = 0.0

    bitslice.add_component(GDIN_reg, 'GDIN_reg', xcoord, ycoord)
    bitslice.connect('DIN', 'GDIN_reg.'+sc['flipflop']['in'])
    bitslice.add_net(Net('GDIN'))
    bitslice.connect('GDIN', 'GDIN_reg.'+sc['flipflop']['out'])
    bitslice.connect('clk', 'GDIN_reg.'+sc['flipflop']['clk'])

    if params['add_GDIN_out_BUF'] == 1:      # in case of adding GDIN_out_BUF
        bitslice.add_component(sc['buffer_X6']['component'], 'GDIN_BUF', xcoord, ycoord+sc['site'])
        bitslice.connect('GDIN', 'GDIN_BUF.'+sc['buffer']['in'])
        bitslice.add_net(Net('GDIN_BUF_out'))
        bitslice.connect('GDIN_BUF_out', 'GDIN_BUF.'+sc['buffer']['out'])


    xcoord = sc['latch']['width']
    ycoord += 2*sc['site']
    bitslice.add_component(read_mux, 'read_mux', xcoord, ycoord)
    bitslice.connect('DOUT', 'read_mux.DOUT')
    
    bitslice.add_netbus(Bus(Net, 'MemoryLatch', 2**ADDR_WIDTH))
    xcoord = 0.0
    for i in range(2**ADDR_WIDTH):
        if i == (2**ADDR_WIDTH)//2: # gap for DIN buffers
           ycoord += sc['site']*params['middle_horizontal_gap']         	
        bitslice.add_component(MemoryLatch_reg, MemoryLatch_reg_name%(i), xcoord, ycoord)
        ycoord += sc['site']
        
        #for net in ['MemoryLatch']:
            #bitslice.add_net(Net(net+str([i])))
        if params['add_GDIN_out_BUF'] == 1:      # in case of adding GDIN_out_BUF
            bitslice.connect('GDIN_BUF_out', MemoryLatch_reg_name%(i)+'.'+sc['latch']['in'])
        elif params['add_GDIN_out_BUF'] == 0:
            bitslice.connect('GDIN', MemoryLatch_reg_name%(i)+'.'+sc['latch']['in'])

        for net in [('MemoryLatch',sc['latch']['out']), ('DGWCLK', sc['latch']['clk'])]:
            bitslice.connect(net[0]+str([i]), MemoryLatch_reg_name%(i)+'.'+net[1]) #conectivty to MemoryLatch_reg
        for net in ['MemoryLatch', 'RWL']:
            bitslice.connect(net+str([i]), 'read_mux.'+net+str([i]))    #conectivty to read_mux
    
    xcoord = 0.0
    ycoord = 0.0
    for row in range(2**ADDR_WIDTH):
        bitslice.set_pin_position('RWL'+str([row]), xcoord, ycoord + 0.65, 'LEFT', 2)
        bitslice.set_pin_position('DGWCLK'+str([row]), xcoord, ycoord + 1.15, 'LEFT', 2)
        ycoord += sc['site']


##########################################################
# add components to read_mux module
##########################################################
def SCM_design_components_instances_read_mux(params, scm):
    # aliases:
    ADDR_WIDTH = params['ADDR_WIDTH']
    read_mux = scm['read_mux']
    #NAND2 = sc['NAND2']['component']
    #NOR2 = sc['NOR2']['component']
    #INV_OUT_GATE = sc['inverter_X4']['component']
    #buffer = sc['buffer_X4']['component']
    MUX_DRIVE_STRENGTH = params['MUX_DRIVE_STRENGTH']

    # instances names:
    level_first_name = 'level_%0'+str(len(str(ADDR_WIDTH+1)))+'d'

    xcoord = 0.0
    ycoord = 0.0

    for level in range(1, ADDR_WIDTH+2):
        # instances names:
        level_second_name = '_%0'+str(len(str((2**ADDR_WIDTH)>>(level-1))))+'d'	
			
        ycoord = 0.0

        if (level != 1):
            initial_Offset = ((2**(level-2))-1)     # is used to figure out what the first row for this level is
            gap_Between_Gates = (2**(level-1))      # is how many rows between gates at this level
            ycoord += initial_Offset*sc['site']            

        if level == 1:      # add and connect level_1 NAND2
            NAND2_str = 'NAND2_X'+str(MUX_DRIVE_STRENGTH[level-1])
            NAND2 = sc[NAND2_str]['component']
            read_mux.add_netbus(Bus(Net, 'w'+str(level-1), 2**ADDR_WIDTH))
            for i in range(2**ADDR_WIDTH):
                if i == (2**ADDR_WIDTH)//2: # gap for DIN buffers
                    ycoord += sc['site']*params['middle_horizontal_gap']              
                read_mux.add_component(NAND2, level_first_name%(level)+level_second_name%(i), xcoord, ycoord)
                ycoord += sc['site']
                #read_mux.add_net(Net('w'+str(level-1)+str([i])))
                for pin in [('MemoryLatch', sc[NAND2_str]['in_1']), ('RWL', sc[NAND2_str]['in_2']), ('w'+str(level-1), sc[NAND2_str]['out'])]:
                    read_mux.connect(pin[0]+str([i]), level_first_name%(level)+level_second_name%(i)+'.'+pin[1])

        if level == 2:      # add and connect level_2 NAND2
            xcoord += sc['NAND2_X'+str(MUX_DRIVE_STRENGTH[0])]['width']
            NAND2_str = 'NAND2_X'+str(MUX_DRIVE_STRENGTH[level-1])
            NAND2 = sc[NAND2_str]['component']
            read_mux.add_netbus(Bus(Net, 'w'+str(level-1), (2**ADDR_WIDTH)>>1))
            for i in range((2**ADDR_WIDTH)>>1):
                if i == ((2**ADDR_WIDTH)>>1)//2:    # gap for DIN buffers
                    ycoord += sc['site']*params['middle_horizontal_gap']
                read_mux.add_component(NAND2, level_first_name%(level)+level_second_name%(i), xcoord, ycoord)
                ycoord += gap_Between_Gates*sc['site']
                #read_mux.add_net(Net('w'+str(level-1)+str([i])))
                for pin in [('w'+str(level-2)+str([2*i]), sc[NAND2_str]['in_1']), ('w'+str(level-2)+str([2*i+1]), sc[NAND2_str]['in_2']), ('w'+str(level-1)+str([i]), sc[NAND2_str]['out'])]:
                    read_mux.connect(pin[0], level_first_name%(level)+level_second_name%(i)+'.'+pin[1])

        # if (level%2) and (level != 1):

        if (level%2) & (level != 1):        # add and connect levels 3,5,7..... -> in odd levels there are NOR2 gates
            NOR2_str = 'NOR2_X'+str(MUX_DRIVE_STRENGTH[level-1])
            NOR2 = sc[NOR2_str]['component']
            read_mux.add_netbus(Bus(Net, 'w'+str(level-1), (2**ADDR_WIDTH)>>(level-1)))   
            for i in range((2**ADDR_WIDTH)>>(level-1)):
                read_mux.add_component(NOR2, level_first_name%(level)+level_second_name%(i), xcoord, ycoord)
                ycoord += gap_Between_Gates*sc['site']
                if i == (((2**ADDR_WIDTH)>>(level-1))//2)-1:    # gap for DIN buffers
                    ycoord += sc['site']*params['middle_horizontal_gap']
                #read_mux.add_net(Net('w'+str(level-1)+str([i])))
                for pin in [('w'+str(level-2)+str([2*i]), sc[NOR2_str]['in_1']), ('w'+str(level-2)+str([2*i+1]), sc[NOR2_str]['in_2']), ('w'+str(level-1)+str([i]), sc[NOR2_str]['out'])]:
                    read_mux.connect(pin[0], level_first_name%(level)+level_second_name%(i)+'.'+pin[1])            

        if (level%2 == 0) & (level != 2):       # add and connect levels 4,6,8..... -> in even levels there are NAND2 gates
            NAND2_str = 'NAND2_X'+str(MUX_DRIVE_STRENGTH[level-1])
            NAND2 = sc[NAND2_str]['component']
            read_mux.add_netbus(Bus(Net, 'w'+str(level-1), (2**ADDR_WIDTH)>>(level-1)))
            for i in range((2**ADDR_WIDTH)>>(level-1)):
                if i == ((2**ADDR_WIDTH)>>(level-1))//2:    # gap for DIN buffers
                    ycoord += sc['site']*params['middle_horizontal_gap']
                read_mux.add_component(NAND2, level_first_name%(level)+level_second_name%(i), xcoord, ycoord)
                ycoord += gap_Between_Gates*sc['site']
                #read_mux.add_net(Net('w'+str(level-1)+str([i])))
                for pin in [('w'+str(level-2)+str([2*i]), sc[NAND2_str]['in_1']), ('w'+str(level-2)+str([2*i+1]), sc[NAND2_str]['in_2']), ('w'+str(level-1)+str([i]), sc[NAND2_str]['out'])]:
                    read_mux.connect(pin[0], level_first_name%(level)+level_second_name%(i)+'.'+pin[1])     
    
    # last inverter or buffer
    level += 1
    ycoord = 0.0
    initial_Offset = ((2**(level-2))-1)     # is used to figure out what the first row for this level is
    ycoord += (initial_Offset+params['middle_horizontal_gap'])*sc['site']            

    if ((ADDR_WIDTH+1)%2 == 1):     
        INV_OUT_GATE_str = 'inverter_X'+str(MUX_DRIVE_STRENGTH[-1])
        INV_OUT_GATE = sc[INV_OUT_GATE_str]['component']
        read_mux.add_component(INV_OUT_GATE, 'inv_out', xcoord, ycoord)
        for pin in [('w'+str(ADDR_WIDTH)+'[0]', sc[INV_OUT_GATE_str]['in']), ('DOUT', sc[INV_OUT_GATE_str]['out'])]:
            read_mux.connect(pin[0], 'inv_out.'+pin[1])
    elif ((ADDR_WIDTH+1)%2 == 0):
        buffer_str = 'buffer_X'+str(MUX_DRIVE_STRENGTH[-1])
        buffer = sc[buffer_str]['component']
        read_mux.add_component(buffer, 'buffer_out', xcoord, ycoord)
        for pin in [('w'+str(ADDR_WIDTH)+'[0]', sc[buffer_str]['in']), ('DOUT', sc[buffer_str]['out'])]:
            read_mux.connect(pin[0], 'buffer_out.'+pin[1])



################################################################
####################   write verilog file   ####################
################################################################
def write_verilog_file(params,scm):
    export_folder = 'export'
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)

    export_design_folder = export_folder+'/'+params['TOPLEVEL']
    if not os.path.exists(export_design_folder):
        os.makedirs(export_design_folder)

    verilog_file_name = export_design_folder + '/' + params['TOPLEVEL'] + '.post_py.v'
    
    header_comment_text = []
    module_scm_text = scm['TOP'].write_verilog()

    header_comment(header_comment_text, params, module_scm_text)    
    
    verilog_file=open(verilog_file_name,'w')

    for line in header_comment_text:
        verilog_file.write(line)


    #for line in scm['TOP'].write_verilog():
    #        verilog_file.write(line+"\n")
    for module in scm['TOP'].get_subcomponents_recursive(inclusive=True):
        if not module.get_dont_write_verilog():
            for line in module.write_verilog():
                #for line in module.write_verilog():
                verilog_file.write(line+"\n")
    
    verilog_file.close()
    
    ##########  write verilog in split files  ##########
    verilog_files_folder = 'verilog_modules'
    if not os.path.exists(verilog_files_folder):
        os.makedirs(verilog_files_folder)

    for module in scm.values():
        verilog_module_folder = verilog_files_folder+'/'+str(module)
        if not os.path.exists(verilog_module_folder):
            os.makedirs(verilog_module_folder)
        
        verilog_file_name = verilog_module_folder+'/'+str(module)+'.v'
        verilog_file=open(verilog_file_name,'w')

        for line in module.write_verilog():
            verilog_file.write(line+"\n")
        verilog_file.close()

    ##########  write python params as verilog define  ##########
    verilog_file_name = verilog_files_folder + '/define.v'
    verilog_file=open(verilog_file_name,'w')
    verilog_file.write("//####################### define parameter #######################\n")
    for p in sorted(params.keys()):
        s = '`define ' + p + ' ' + str(params[p])
        verilog_file.write(s + '\n')
    verilog_file.close()

################################################################
###################   write header comment   ###################
################################################################
def header_comment(text, params, module_scm_text):
    text.append('/*\n')
    text.append('###############################################################\n')
    text.append('#\tGenerated by:\t\tEnICS SCM Compiler v1.1\n')
    text.append('#\tGenerated on:\t\t'+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'\n')
    text.append('#\tDesign:\t\t\t\t'+params['TOPLEVEL']+'\n')
    text.append('#\n')
    text.append('#\tDimensions:\n')
    text.append('#\tDATA WIDTH:\t\t\t'+str(params['DATA_WIDTH'])+'\n')
    text.append('#\tNUM ROWS:\t\t\t'+str(2**params['ADDR_WIDTH'])+'\n')
    text.append('#\n')
    text.append('#\tlines in lists:\n')    
    text.append('#\tmodule_scm_text:\t'+str(len(module_scm_text))+'\n')
    text.append('###############################################################\n')
    text.append('*/\n')    


################################################################
############   write tcl placement commands file   #############
################################################################
def write_tcl(params,scm):
    export_folder = 'export'
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)
    
    export_design_folder = export_folder+'/'+params['TOPLEVEL']
    if not os.path.exists(export_design_folder):
        os.makedirs(export_design_folder)
        
    tcl_FloorPlan_file_name = export_design_folder + '/' + params['TOPLEVEL'] + '_FloorPlan_command.tcl'
    tcl_cells_position_file_name = export_design_folder + '/' + params['TOPLEVEL'] + '_cells_position.tcl'
    tcl_pin_position_file_name = export_design_folder + '/' + params['TOPLEVEL'] + '_pin_position.tcl'
    
    
    #for module in scm.values():
    for module in [scm['TOP']]:
        tcl_file=open(tcl_FloorPlan_file_name,'w')
        tcl_file.write('###### module: ' + str(module) + '\n')
        tcl_file.write('###### TCL commands tool: '+params['TCL_tool']+'\n###### File: '+tcl_FloorPlan_file_name+'\n\n')     
        tcl_file.write('set floorPlan_margin_x 0.0\n')
        tcl_file.write('# y_coordinate must be product of site\n')        
        tcl_file.write('set floorPlan_margin_y 0.0\n')
        tcl_file.write(module.write_floorPlan_tcl_commands('sc'+params['TRACKS']+'_cln65lp') + '\n\n')  # FloorPlan
        tcl_file.close()

        tcl_file=open(tcl_cells_position_file_name,'w')
        tcl_file.write('###### module: ' + str(module) + '\n')
        tcl_file.write('###### TCL commands: '+params['TCL_tool']+' ######\n\n')                
        tcl_file.write('set x_coordinate 0.0\n')
        tcl_file.write('# y_coordinate must be product of site\n')
        tcl_file.write('set y_coordinate 0.0\n\n')        
        for line in module.write_tcl_placement_commands(params['TCL_tool'])[0]:	# standatd cells placement
            tcl_file.write(str(line) + '\n')
        tcl_file.close()

        tcl_file=open(tcl_pin_position_file_name,'w')
        tcl_file.write('###### module: ' + str(module) + '\n')
        tcl_file.write('###### TCL commands: '+params['TCL_tool']+' ######\n\n')                
        for line in module.write_pin_tcl_placement_commands():	# pin placement
            tcl_file.write(str(line) + '\n')
        tcl_file.close()


if __name__ == '__main__':
    main()

