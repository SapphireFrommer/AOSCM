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
    for pin in ['CLK', 'WE', 'RE', 'SE']:
        TOP.add_pin(Input(pin))
    for pin in ['WADDR', 'RADDR']:
        TOP.add_pinbus(Bus(Input, pin, ADDR_WIDTH))
    TOP.add_pinbus(Bus(Input, 'DIN', params['DATA_WIDTH']))
    TOP.add_pinbus(Bus(Output, 'DOUT', params['DATA_WIDTH']))

    ##### define a bitslice_evn   
    scm['bitslice_evn'] = ComponentXY('bitslice_evn')
    bitslice = scm['bitslice_evn']
    bitslice.add_pin(Input('DIN'))
    bitslice.add_pin(Output('DOUT'))
    bitslice.add_pin(Input('clk'))
    for pin in ['DGWCLK', 'RWL']:
        bitslice.add_pinbus(Bus(Input, pin, 2**ADDR_WIDTH))
    
    ##### define a bitslice_odd   
    scm['bitslice_odd'] = ComponentXY('bitslice_odd')
    bitslice = scm['bitslice_odd']
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
    
    ##### define a MidGap_DGWCLK    
    scm['MidGap_DGWCLK'] = ComponentXY('MidGap_DGWCLK')
    MidGap_DGWCLK = scm['MidGap_DGWCLK']
    MidGap_DGWCLK.add_pin(Input('clk'))
    MidGap_DGWCLK.add_pin(Input('SE'))
    MidGap_DGWCLK.add_pinbus(Bus(Input, 'E', 2**ADDR_WIDTH))
    for pin in ['DGWClkLeftNet', 'DGWClkRightNet']:
        MidGap_DGWCLK.add_pinbus(Bus(Output, pin, 2**ADDR_WIDTH))

    ###### define a PreDecoder_2_4    
    scm['PreDecoder_2_4'] = ComponentXY('PreDecoder_2_4')
    PreDecoder_2_4 = scm['PreDecoder_2_4']
    PreDecoder_2_4.add_pinbus(Bus(Input, 'decoder_in', 2))
    PreDecoder_2_4.add_pinbus(Bus(Output, 'decoder_out', 4))

    ##### define a PreDecoder_3_8 
    scm['PreDecoder_3_8'] = ComponentXY('PreDecoder_3_8')
    PreDecoder_3_8 = scm['PreDecoder_3_8']
    PreDecoder_3_8.add_pinbus(Bus(Input, 'decoder_in', 3))
    PreDecoder_3_8.add_pinbus(Bus(Output, 'decoder_out', 8))
   
    ##### define a PreDecoder_4_16    
    scm['PreDecoder_4_16'] = ComponentXY('PreDecoder_4_16')
    PreDecoder_4_16 = scm['PreDecoder_4_16']
    PreDecoder_4_16.add_pinbus(Bus(Input, 'decoder_in', 4))
    PreDecoder_4_16.add_pinbus(Bus(Output, 'decoder_out', 16))
    
    ##### define a row_decoder    
    scm['row_decoder'] = ComponentXY('row_decoder')
    row_decoder = scm['row_decoder']
    row_decoder.add_pinbus(Bus(Input, 'decoder_in', ADDR_WIDTH))
    row_decoder.add_pinbus(Bus(Output, 'decoder_out', 2**ADDR_WIDTH))

    ##### define a welltap_stripe    
    scm['welltap_stripe'] = ComponentXY('welltap_stripe')
    welltap_stripe = scm['welltap_stripe']

    ##### define a rwlBuff_stripe    
    scm['rwlBuff_stripe'] = ComponentXY('rwlBuff_stripe')
    rwlBuff_stripe = scm['rwlBuff_stripe']
    rwlBuff_stripe.add_pinbus(Bus(Input, 'IN', 2**ADDR_WIDTH))
    rwlBuff_stripe.add_pinbus(Bus(Output, 'OUT', 2**ADDR_WIDTH))
        

##############################################################################################
###############   add components, internal nets and connectivity to modules   ################
##############################################################################################
def SCM_design_components_instances(params, scm):

    SCM_design_components_instances_MidGap_DGWCLK(params, scm)
    SCM_design_components_instances_Decoder_x_x(params, scm)
    SCM_design_components_instances_row_decoder(params, scm)
    SCM_design_components_instances_welltap_strip(params, scm)
    SCM_design_components_instances_rwlBuff_strip(params, scm)
    SCM_design_components_instances_read_mux(params, scm)
    SCM_design_components_instances_bitslice(params, scm, 'bitslice_evn')
    SCM_design_components_instances_bitslice(params, scm, 'bitslice_odd')
    SCM_design_components_instances_TOP(params, scm)


##########################################################
# add components to TOP module
##########################################################
def SCM_design_components_instances_TOP(params, scm):
    # aliases:
    ADDR_WIDTH = params['ADDR_WIDTH']
    TOP = scm['TOP']
    welltap_stripe = scm['welltap_stripe']
    bitslice = scm['bitslice_evn']
    bitslice_odd = scm['bitslice_odd']	
    rwlBuff_stripe = scm['rwlBuff_stripe']
    MidGap_DGWCLK = scm['MidGap_DGWCLK']
    row_decoder = scm['row_decoder']
    read_mux = scm['read_mux']
    latch_clock_gate = sc['latch_clock_gate']['component']

    # instances names:
    bitslice_name = 'bitslice_%0'+str(len(str(params['DATA_WIDTH'])))+'d'
    rwlBuff_stripe_name = 'rwlBuff_stripe_%0'+str(len(str(params['DATA_WIDTH']//params['RWL_NUM'])))+'d'
    welltap_stripe_name = 'welltap_stripe_%0'+str(len(str(params['DATA_WIDTH']//params['WELLTAP'])))+'d'

    #########################################################
    #		components										#
    #########################################################
    xcoord = 0.0
    ycoord = 0.0

    for i in range(params['DATA_WIDTH']):
        ycoord = 0.0
        
        if (i%params['WELLTAP']) == 0:
            if (i%2) == 1:
                xcoord += sc['well_tap']['width']								
            TOP.add_component(welltap_stripe, welltap_stripe_name%(i//params['WELLTAP']), xcoord, ycoord)
            if (i%2) == 0:	
                xcoord += sc['well_tap']['width']
            else:
                xcoord += sc['well_tap']['width']+0.4
        # rwlBuff_strips
        K_RWL = params['DATA_WIDTH']//params['RWL_NUM']	# after how many bitslice, rwl buffer will be
        ycoord += sc['site']
        if (((params['DATA_WIDTH']//2)-i)%K_RWL == 0) & (i != 0) & (i < params['DATA_WIDTH']//2):   # left side
            TOP.add_component(rwlBuff_stripe, rwlBuff_stripe_name%((i//K_RWL)-1), xcoord, ycoord+sc['site'])
            xcoord += sc['buffer']['width']

        if (i == params['DATA_WIDTH']//2):    # MidGap - 2 middle
            TOP.add_component(rwlBuff_stripe, rwlBuff_stripe_name%((i//K_RWL)-1), xcoord, ycoord+sc['site'])
            xcoord += sc['buffer']['width']


            ycoord = 0.0
            TOP.add_component(row_decoder, 'read_decoder', xcoord, ycoord)
            for index in range(ADDR_WIDTH):
                pin = 'RADDR'+str([index])
                TOP.set_pin_position(pin, xcoord+0.2+(0.4*index), ycoord, 'BOTTOM', 2)
            
            if	ADDR_WIDTH==4 or ADDR_WIDTH==5 or ADDR_WIDTH==8:
                read_decoder_width = sc['NOR2']['width']
            else:
                read_decoder_width = sc['NOR3']['width']
                
            xcoord += read_decoder_width

            t_xcoord = sc['buffer']['width']

            #for gate in ['GDINCLK_gate', 'GWCLK_gate', 'GRCLK_gate']:
            for gate in ['GDINCLK_gate', 'GWCLK_gate']:
                TOP.add_component(latch_clock_gate, gate, xcoord+t_xcoord , ycoord)
                ycoord += sc['site']
                #xcoord += sc['latch_clock_gate']['width']
            #xcoord -= 3*(sc['latch_clock_gate']['width'])
            ycoord = 0.0

            pin = 'RE'
            TOP.set_pin_position(pin, xcoord+1, ycoord, 'BOTTOM', 2)
            pin = 'WE'
            TOP.set_pin_position(pin, xcoord+2, ycoord, 'BOTTOM', 2)

            ycoord += 2*sc['site']
            TOP.add_component(MidGap_DGWCLK, 'MidGap_DGWCLK', xcoord, ycoord)
            MidGap_DGWCLK_width = sc['buffer']['width']+ sc['latch_clock_gate']['width']+sc['buffer']['width']	# need to write better
            pin = 'CLK'
            TOP.set_pin_position(pin, xcoord+3.7, ycoord, 'BOTTOM', 2)
            pin = 'SE'
            TOP.set_pin_position(pin, xcoord+3.7, ycoord, 'TOP', 2)

            xcoord += MidGap_DGWCLK_width
            
            
            ycoord = 0.0
            TOP.add_component(row_decoder, 'write_decoder', xcoord, ycoord)
            for index in range(ADDR_WIDTH):
                pin = 'WADDR'+str([index])
                TOP.set_pin_position(pin, xcoord+0.2+(0.4*index), ycoord, 'BOTTOM', 2)

            if	ADDR_WIDTH==4 or ADDR_WIDTH==5 or ADDR_WIDTH==8:
                write_decoder_width = sc['NOR2']['width']
            else:
                write_decoder_width = sc['NOR3']['width']
            
            xcoord += write_decoder_width

            ycoord += sc['site']
            TOP.add_component(rwlBuff_stripe, rwlBuff_stripe_name%((i//K_RWL)), xcoord, ycoord+sc['site'])
            xcoord += sc['buffer']['width']	
            
        if (i%K_RWL == 0) & (i > params['DATA_WIDTH']//2):   # right side
            TOP.add_component(rwlBuff_stripe, rwlBuff_stripe_name%((i//K_RWL)), xcoord, ycoord+sc['site'])
            xcoord += sc['buffer']['width']	

        
        ycoord = 0.0
        pin = 'DIN'+str([i])
        if (i%2) == 0:	
            TOP.add_component(bitslice, bitslice_name%(i), xcoord, ycoord)
            TOP.set_pin_position(pin, xcoord+3.5, ycoord, 'BOTTOM', 2)
        else:
            TOP.add_component(bitslice_odd, bitslice_name%(i), xcoord, ycoord)
            TOP.set_pin_position(pin, xcoord+3.1, ycoord, 'BOTTOM', 2)
            
        pin = 'DOUT'+str([i])
        TOP.set_pin_position(pin, xcoord+3.7, ycoord, 'TOP', 2)

        if (ADDR_WIDTH%2)==0:
            t_xcoord = (sc['latch']['width']+sc['NAND2']['width']+sc['NAND2']['width'])-sc['flipflop']['width']
        else:
            t_xcoord = (sc['latch']['width']+sc['buffer']['width']+sc['NAND2']['width'])-sc['flipflop']['width']
            
        bitslice_width = sc['flipflop']['width']+t_xcoord	# need to write better
        xcoord += bitslice_width	
        



    # last welltap strip:
    ycoord = 0.0
    TOP.add_component(welltap_stripe, welltap_stripe_name%((params['DATA_WIDTH']//params['WELLTAP'])+1), xcoord, ycoord)
    			
    #########################################################
    #		connectivity									#
    #########################################################
    
    

    # first level clock gates

    #for gate in ['GDINCLK_gate', 'GWCLK_gate', 'GRCLK_gate']:    
    for gate in ['GDINCLK_gate', 'GWCLK_gate']:
        TOP.connect('CLK', gate+'.CK')
        TOP.connect('SE', gate+'.SE')

    TOP.connect('WE', 'GDINCLK_gate.'+sc['latch_clock_gate']['E'])
    TOP.connect('WE', 'GWCLK_gate.'+sc['latch_clock_gate']['E'])
    #TOP.connect('RE', 'GRCLK_gate.E')


    TOP.add_net(Net('GDINCLK'))
    TOP.add_net(Net('GWCLK'))
    #TOP.add_net(Net('GRCLK'))
    TOP.connect('GDINCLK', 'GDINCLK_gate.'+sc['latch_clock_gate']['out'])
    TOP.connect('GWCLK', 'GWCLK_gate.'+sc['latch_clock_gate']['out'])
    #TOP.connect('GRCLK', 'GRCLK_gate.ECK')

    TOP.add_netbus(Bus(Net, 'decoder_write_out', 2**ADDR_WIDTH))


    for i in range(params['DATA_WIDTH']):	
        # rwlBuff_strips (it's only a draft)
        if (((params['DATA_WIDTH']//2)-i)%K_RWL == 0) & (i != 0) & (i < params['DATA_WIDTH']//2):   # left side
            if (i==K_RWL):
                TOP.add_netbus(Bus(Net, 'rwlBuffNet_'+str((i//K_RWL)-1), 2**ADDR_WIDTH))
            TOP.add_netbus(Bus(Net, 'rwlBuffNet_'+str((i//K_RWL)), 2**ADDR_WIDTH))
            for row in range(2**ADDR_WIDTH):
                TOP.connect('rwlBuffNet_'+str((i//K_RWL))+str([row]), rwlBuff_stripe_name%((i//K_RWL)-1)+'.IN'+str([row]))
                TOP.connect('rwlBuffNet_'+str((i//K_RWL)-1)+str([row]), rwlBuff_stripe_name%((i//K_RWL)-1)+'.OUT'+str([row]))

        if (i == params['DATA_WIDTH']//2):    # 2 middle
            TOP.add_netbus(Bus(Net, 'decoder_read_out', 2**ADDR_WIDTH))
            TOP.add_netbus(Bus(Net, 'rwlBuffNet_'+str((i//K_RWL)), 2**ADDR_WIDTH))
            for row in range(2**ADDR_WIDTH):       
                TOP.connect('decoder_read_out'+str([row]), rwlBuff_stripe_name%((i//K_RWL)-1)+'.IN'+str([row]))                
                TOP.connect('rwlBuffNet_'+str((i//K_RWL)-1)+str([row]), rwlBuff_stripe_name%((i//K_RWL)-1)+'.OUT'+str([row]))

                TOP.connect('decoder_read_out'+str([row]), rwlBuff_stripe_name%((i//K_RWL))+'.IN'+str([row]))
                TOP.connect('rwlBuffNet_'+str((i//K_RWL))+str([row]), rwlBuff_stripe_name%((i//K_RWL))+'.OUT'+str([row]))


        if (i%K_RWL == 0) & (i > params['DATA_WIDTH']//2):   # right side
            TOP.add_netbus(Bus(Net, 'rwlBuffNet_'+str((i//K_RWL)), 2**ADDR_WIDTH))
            for row in range(2**ADDR_WIDTH):
                TOP.connect('rwlBuffNet_'+str((i//K_RWL)-1)+str([row]), rwlBuff_stripe_name%((i//K_RWL))+'.IN'+str([row]))
                TOP.connect('rwlBuffNet_'+str((i//K_RWL))+str([row]), rwlBuff_stripe_name%((i//K_RWL))+'.OUT'+str([row]))



        # bitslices
        TOP.connect('DIN'+str([i]), bitslice_name%(i)+'.DIN')
        TOP.connect('DOUT'+str([i]), bitslice_name%(i)+'.DOUT')
        TOP.connect('GDINCLK', bitslice_name%(i)+'.clk')

        # DGWCLK net to bitslice connectivity
        if i < (params['DATA_WIDTH']/2):
            if i == 0:
                TOP.add_netbus(Bus(Net, 'DGWCLKLeftNet', 2**ADDR_WIDTH))
                TOP.add_netbus(Bus(Net, 'DGWClkRightNet', 2**ADDR_WIDTH))
            for j in range(2**ADDR_WIDTH):
                TOP.connect('DGWCLKLeftNet'+str([j]), bitslice_name%(i)+'.DGWCLK'+str([j]))
        else:
            for j in range(2**ADDR_WIDTH):
                TOP.connect('DGWClkRightNet'+str([j]), bitslice_name%(i)+'.DGWCLK'+str([j]))

        if i == ((params['DATA_WIDTH']//2)-1):    # MidGap
            TOP.connect('GWCLK', 'MidGap_DGWCLK.clk')
            TOP.connect('SE', 'MidGap_DGWCLK.SE')
            for j in range(2**ADDR_WIDTH):
                TOP.connect('DGWCLKLeftNet'+str([j]), 'MidGap_DGWCLK.DGWClkLeftNet'+str([j]))
                TOP.connect('DGWClkRightNet'+str([j]), 'MidGap_DGWCLK.DGWClkRightNet'+str([j]))
                TOP.connect('decoder_write_out'+str([j]), 'MidGap_DGWCLK.E'+str([j]))





    # bitslices RWL connectivity
    for row in range(2**ADDR_WIDTH):
        for col in range(params['DATA_WIDTH']):
            TOP.connect('rwlBuffNet_'+str(col//K_RWL)+str([row]), bitslice_name%(col)+'.'+'RWL'+str([row]))
        TOP.connect('decoder_read_out'+str([row]), 'read_decoder''.decoder_out'+str([row]))
        TOP.connect('decoder_write_out'+str([row]), 'write_decoder''.decoder_out'+str([row]))

    for ADDR in range(ADDR_WIDTH):
        TOP.connect('RADDR'+str([ADDR]), 'read_decoder''.decoder_in'+str([ADDR]))
        TOP.connect('WADDR'+str([ADDR]), 'write_decoder''.decoder_in'+str([ADDR]))


##########################################################
# add components to bitslice module
##########################################################
def SCM_design_components_instances_bitslice(params, scm, b_name):
    # aliases:
    ADDR_WIDTH = params['ADDR_WIDTH']
    bitslice = scm[b_name]
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
    xcoord = sc['latch']['width']
    ycoord += 2*sc['site']
    bitslice.add_component(read_mux, 'read_mux', xcoord, ycoord)
    bitslice.connect('DOUT', 'read_mux.DOUT')
    
    bitslice.add_netbus(Bus(Net, 'MemoryLatch', 2**ADDR_WIDTH))
    xcoord = 0.0
    for i in range(2**ADDR_WIDTH):	
        bitslice.add_component(MemoryLatch_reg, MemoryLatch_reg_name%(i), xcoord, ycoord)
        ycoord += sc['site']
        #for net in ['MemoryLatch']:
            #bitslice.add_net(Net(net+str([i])))
        bitslice.connect('GDIN', MemoryLatch_reg_name%(i)+'.'+sc['latch']['in'])         
        for net in [('MemoryLatch',sc['latch']['out']), ('DGWCLK', sc['latch']['clk'])]:
            bitslice.connect(net[0]+str([i]), MemoryLatch_reg_name%(i)+'.'+net[1]) #conectivty to MemoryLatch_reg
        for net in ['MemoryLatch', 'RWL']:
            bitslice.connect(net+str([i]), 'read_mux.'+net+str([i]))    #conectivty to read_mux
    

    #scm['bitslice_odd'] = bitslice.copy('bitslice_odd')
    if b_name == 'bitslice_odd':
        xcoord = (sc['latch']['width']+sc['NAND2']['width']+sc['NAND2']['width'])-sc['flipflop']['width']
        scm[b_name].set_position('GDIN_reg', xcoord, sc['site'])
##########################################################
# add components to read_mux module
##########################################################
def SCM_design_components_instances_read_mux(params, scm):
    # aliases:
    ADDR_WIDTH = params['ADDR_WIDTH']
    read_mux = scm['read_mux']
    NAND2 = sc['NAND2']['component']
    NOR2 = sc['NOR2']['component']
    INV_OUT_GATE = sc['inverter']['component']
    buffer = sc['buffer']['component']

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
            read_mux.add_netbus(Bus(Net, 'w'+str(level-1), 2**ADDR_WIDTH))
            for i in range(2**ADDR_WIDTH):
                read_mux.add_component(NAND2, level_first_name%(level)+level_second_name%(i), xcoord, ycoord)
                ycoord += sc['site']
                #read_mux.add_net(Net('w'+str(level-1)+str([i])))
                for pin in [('MemoryLatch', sc['NAND2']['in_1']), ('RWL', sc['NAND2']['in_2']), ('w'+str(level-1), sc['NAND2']['out'])]:
                    read_mux.connect(pin[0]+str([i]), level_first_name%(level)+level_second_name%(i)+'.'+pin[1])

        if level == 2:      # add and connect level_2 NAND2
            xcoord += sc['NAND2']['width']
            read_mux.add_netbus(Bus(Net, 'w'+str(level-1), (2**ADDR_WIDTH)>>1))
            for i in range((2**ADDR_WIDTH)>>1):
                read_mux.add_component(NAND2, level_first_name%(level)+level_second_name%(i), xcoord, ycoord)
                ycoord += gap_Between_Gates*sc['site']
                #read_mux.add_net(Net('w'+str(level-1)+str([i])))
                for pin in [('w'+str(level-2)+str([2*i]), sc['NAND2']['in_1']), ('w'+str(level-2)+str([2*i+1]), sc['NAND2']['in_2']), ('w'+str(level-1)+str([i]), sc['NAND2']['out'])]:
                    read_mux.connect(pin[0], level_first_name%(level)+level_second_name%(i)+'.'+pin[1])

        if (level%2) & (level != 1):        # add and connect levels 3,5,7..... -> in odd levels there are NOR2 gates
            read_mux.add_netbus(Bus(Net, 'w'+str(level-1), (2**ADDR_WIDTH)>>(level-1)))   
            for i in range((2**ADDR_WIDTH)>>(level-1)):
                read_mux.add_component(NOR2, level_first_name%(level)+level_second_name%(i), xcoord, ycoord)
                ycoord += gap_Between_Gates*sc['site']            
                #read_mux.add_net(Net('w'+str(level-1)+str([i])))
                for pin in [('w'+str(level-2)+str([2*i]), sc['NOR2']['in_1']), ('w'+str(level-2)+str([2*i+1]), sc['NOR2']['in_2']), ('w'+str(level-1)+str([i]), sc['NOR2']['out'])]:
                    read_mux.connect(pin[0], level_first_name%(level)+level_second_name%(i)+'.'+pin[1])            

        if (level%2 == 0) & (level != 2):       # add and connect levels 4,6,8..... -> in even levels there are NAND2 gates
            read_mux.add_netbus(Bus(Net, 'w'+str(level-1), (2**ADDR_WIDTH)>>(level-1)))
            for i in range((2**ADDR_WIDTH)>>(level-1)):
                read_mux.add_component(NAND2, level_first_name%(level)+level_second_name%(i), xcoord, ycoord)
                ycoord += gap_Between_Gates*sc['site']
                #read_mux.add_net(Net('w'+str(level-1)+str([i])))
                for pin in [('w'+str(level-2)+str([2*i]), sc['NAND2']['in_1']), ('w'+str(level-2)+str([2*i+1]), sc['NAND2']['in_2']), ('w'+str(level-1)+str([i]), sc['NAND2']['out'])]:
                    read_mux.connect(pin[0], level_first_name%(level)+level_second_name%(i)+'.'+pin[1])     
    
    # last inverter or buffer
    level += 1
    ycoord = 0.0
    initial_Offset = ((2**(level-2))-1)     # is used to figure out what the first row for this level is
    ycoord += initial_Offset*sc['site']            

    if ((ADDR_WIDTH+1)%2 == 1):     
        read_mux.add_component(INV_OUT_GATE, 'inv_out', xcoord, ycoord)
        for pin in [('w'+str(ADDR_WIDTH)+'[0]', sc['inverter']['in']), ('DOUT', sc['inverter']['out'])]:
            read_mux.connect(pin[0], 'inv_out.'+pin[1])
    elif ((ADDR_WIDTH+1)%2 == 0):
        read_mux.add_component(buffer, 'buffer_out', xcoord, ycoord)
        for pin in [('w'+str(ADDR_WIDTH)+'[0]', sc['buffer']['in']), ('DOUT', sc['buffer']['out'])]:
            read_mux.connect(pin[0], 'buffer_out.'+pin[1])


##########################################################
# add components to MidGap_DGWCLK module
##########################################################
def SCM_design_components_instances_MidGap_DGWCLK(params, scm):
    # aliases:
    ADDR_WIDTH = params['ADDR_WIDTH']
    MidGap_DGWCLK = scm['MidGap_DGWCLK']
    buffer = sc['buffer']['component']
    latch_clock_gate = sc['latch_clock_gate']['component']

    # instances names:
    DGWClkLeftBuff_name = 'DGWClkLeftBuff_%0'+str(len(str(2**ADDR_WIDTH)))+'d'
    DGWClkRightBuff_name = 'DGWClkRightBuff_%0'+str(len(str(2**ADDR_WIDTH)))+'d'
    DGWCLK_gate_name = 'DGWCLK_gate_%0'+str(len(str(2**ADDR_WIDTH)))+'d'
    Buff_name = 'Buff_%0'+str(len(str(2**ADDR_WIDTH)))+'d'
    
    xcoord = 0.0
    ycoord = 0.0

    xcoord_LeftBuff = xcoord
    xcoord_DGWCLK_gate = xcoord_LeftBuff+sc['buffer']['width']
    xcoord_RightBuff = xcoord_DGWCLK_gate+sc['latch_clock_gate']['width']
    
    MidGap_DGWCLK.add_netbus(Bus(Net, 'ECK', 2**ADDR_WIDTH))
    for i in range(2**ADDR_WIDTH):
        MidGap_DGWCLK.add_component(buffer, DGWClkLeftBuff_name%(i), xcoord_LeftBuff, ycoord)
        MidGap_DGWCLK.add_component(latch_clock_gate, DGWCLK_gate_name%(i), xcoord_DGWCLK_gate, ycoord)
        MidGap_DGWCLK.add_component(buffer, DGWClkRightBuff_name%(i), xcoord_RightBuff, ycoord)
        ycoord += sc['site']
        
        MidGap_DGWCLK.connect('ECK'+str([i]), DGWCLK_gate_name%(i)+'.'+sc['latch_clock_gate']['out'])
        MidGap_DGWCLK.connect('ECK'+str([i]), DGWClkLeftBuff_name%(i)+'.'+sc['buffer']['in'])
        MidGap_DGWCLK.connect('ECK'+str([i]), DGWClkRightBuff_name%(i)+'.'+sc['buffer']['in'])
        
        MidGap_DGWCLK.connect('E'+str([i]), DGWCLK_gate_name%(i)+'.'+sc['latch_clock_gate']['E'])
        MidGap_DGWCLK.connect('clk', DGWCLK_gate_name%(i)+'.'+sc['latch_clock_gate']['clk'])
        MidGap_DGWCLK.connect('SE', DGWCLK_gate_name%(i)+'.'+sc['latch_clock_gate']['SE'])
        
        for net in ['DGWClkLeft', 'DGWClkRight']:
            MidGap_DGWCLK.connect(net+'Net'+str([i]), net+Buff_name%(i)+'.'+sc['buffer']['out'])



##########################################################
# add components to PreDecoder_x_x module
##########################################################
def SCM_design_components_instances_Decoder_x_x(params, scm):
    # aliases:
    INV = sc['inverter']['component']

    for ADDR_W in [2,3,4]:
        PreDecoder = scm['PreDecoder_'+str(ADDR_W)+'_'+str(2**ADDR_W)]
        xcoord = 0.0
        ycoord = 0.0
        PreDecoder.add_netbus(Bus(Net, 'in_not', ADDR_W)) 
        for i in range(ADDR_W):
            PreDecoder.add_component(INV, 'in_'+str(i)+'_not', xcoord, ycoord, 1)
            xcoord += sc['inverter']['width']
            PreDecoder.connect('decoder_in'+str([i]), 'in_'+str(i)+'_not.' + sc['inverter']['in'])
            PreDecoder.connect('in_not'+str([i]), 'in_'+str(i)+'_not.' + sc['inverter']['out'])
            
        #	a: iterates over the address
        #	n: iterates over the NAND gates
        for n in range(2**ADDR_W):		# ---> this creates every NAND
            nn = 2**ADDR_W-n
            PreDecoder.add_component(sc['NAND'+str(ADDR_W)]['component'], 'NAND'+str(ADDR_W)+'_'+str(n), xcoord, ycoord, 1)
            xcoord += sc['NAND'+str(ADDR_W)]['width']
            PreDecoder.connect('decoder_out'+str([n]), 'NAND'+str(ADDR_W)+'_'+str(n)+'.' + sc['NAND'+str(ADDR_W)]['out'])
        
            for a in range(ADDR_W):		# ----> this connects each input of the nand to this nand			
                if (n & 1<<(ADDR_W-1-a)):
                    PreDecoder.connect('decoder_in'+str([ADDR_W-1-a]), 'NAND'+str(ADDR_W)+'_'+str(n)+'.' + sc['NAND'+str(ADDR_W)]['in_'+str(a+1)])										
                else: 
                    PreDecoder.connect('in_not'+str([ADDR_W-1-a]), 'NAND'+str(ADDR_W)+'_'+str(n)+'.' + sc['NAND'+str(ADDR_W)]['in_'+str(a+1)])					


##########################################################
# add components to row_decoder module
##########################################################
def SCM_design_components_instances_row_decoder(params, scm):
    # aliases:
    ADDR_WIDTH = params['ADDR_WIDTH']
    PreDecoder_2_4 = scm['PreDecoder_2_4']
    PreDecoder_3_8 = scm['PreDecoder_3_8']
    PreDecoder_4_16 = scm['PreDecoder_4_16']
    row_decoder = scm['row_decoder']
    buffer = sc['buffer']['component']
    NAND2 = sc['NAND2']['component']
    NOR2 = sc['NOR2']['component']
    INV = sc['inverter']['component']
    

    ###########         PreDecoders instances         ############
    ##############################################################	
    PreDec_list = []	# lookup table
    if (ADDR_WIDTH == 4):
        PreDec_list = [2,2]
    elif (ADDR_WIDTH == 5):
        PreDec_list = [2,3]
    elif (ADDR_WIDTH == 6):
        PreDec_list = [2,2,2]
    elif (ADDR_WIDTH == 7):
        PreDec_list = [2,2,3]
    elif (ADDR_WIDTH == 8):
        PreDec_list = [4,2,2]		
    
    NUM_PREDECS = len(PreDec_list)
    Num_PreDec_out_wires = 0
    for i in PreDec_list:
        Num_PreDec_out_wires += 2**i
    row_decoder.add_netbus(Bus(Net, 'PreDec_out', Num_PreDec_out_wires))
    xcoord = 0.0
    ycoord = 0.0
    
    for i in range(NUM_PREDECS):
        ycoord = 0  # if we want that placment tool do his job.
        #ycoord = i*sc['site']
        t_xcoord = sc['buffer']['width']
        row_decoder.add_component(scm['PreDecoder_'+str(PreDec_list[i])+'_'+str(2**(PreDec_list[i]))], 'PreDec_'+str(i), xcoord-t_xcoord, ycoord)	# creates the PreDecoders instances
    
    temp_dec_in_port = 0
    temp_dec_out_port = 0
    for i in range(NUM_PREDECS):
        for j in range(PreDec_list[i]):
            row_decoder.connect('decoder_in'+str([j+temp_dec_in_port]), 'PreDec_'+str(i)+'.decoder_in'+str([j]))
        temp_dec_in_port += j+1
        for k in range(2**PreDec_list[i]):
            row_decoder.connect('PreDec_out'+str([k+temp_dec_out_port]), 'PreDec_'+str(i)+'.decoder_out'+str([k]))
        temp_dec_out_port += k+1

    ##################       Post Decoder       ##################
    ##############################################################
    ycoord = 2*sc['site']
    for row in range(2**ADDR_WIDTH):
        row_decoder.add_component(sc['NOR'+str(NUM_PREDECS)]['component'], 'PostDec_%02d'%(row), xcoord, ycoord)
        ycoord += sc['site']
        row_decoder.connect('decoder_out'+str([row]), 'PostDec_%02d'%(row)+'.' + sc['NOR'+str(NUM_PREDECS)]['out'])
    
    NUM_LOWER_BITS = 0
    NUM_LOWER_BITS_OUT = 0	
    NUM_CURRENT_BITS = 0
    for predec_num in range(NUM_PREDECS):
        NUM_LOWER_BITS += NUM_CURRENT_BITS				#---> increases the count of how many bits were in the last iteration
        NUM_CURRENT_BITS = PreDec_list[predec_num]			#---> can be passed in a list
        for row in range(2**ADDR_WIDTH):
            if NUM_LOWER_BITS == 0:
                WHICH_PREDEC_OUT = ((row >> NUM_LOWER_BITS) % (2**NUM_CURRENT_BITS))
                print('if')
            else:
                WHICH_PREDEC_OUT = (((row >> NUM_LOWER_BITS) % (2**NUM_CURRENT_BITS))+((NUM_LOWER_BITS_OUT)))				
                print('else')
            row_decoder.connect('PreDec_out'+str([WHICH_PREDEC_OUT]), 'PostDec_%02d'%(row)+'.' + sc['NOR'+str(NUM_PREDECS)]['in_'+str(predec_num+1)])
            print(WHICH_PREDEC_OUT,row)
        print('===========  End of connecting PreDec: '+str(predec_num)+'  ============')
        NUM_LOWER_BITS_OUT += 2**NUM_CURRENT_BITS
        


##########################################################
# add components to welltap_stripe module
##########################################################
def SCM_design_components_instances_welltap_strip(params, scm):
    # aliases:
    ADDR_WIDTH = params['ADDR_WIDTH']
    welltap_stripe = scm['welltap_stripe']
    xcoord = 0.0
    ycoord = 0.0
    
    welltap_name = 'welltap_%0'+str(len(str(2**ADDR_WIDTH+2)))+'d'
    
    for i in range((2**ADDR_WIDTH)+2):
        welltap_stripe.add_component(sc['well_tap']['component'], welltap_name%(i), xcoord, ycoord)
        ycoord += sc['site']
    
##########################################################
# add components to rwlBuff_stripe module
##########################################################
def SCM_design_components_instances_rwlBuff_strip(params, scm):
    # aliases:
    ADDR_WIDTH = params['ADDR_WIDTH']
    rwlBuff_stripe = scm['rwlBuff_stripe']
    buffer = sc['buffer']['component']

    # instances names:
    rwlBuff_name = 'rwlBuff_%0'+str(len(str(2**ADDR_WIDTH)))+'d'
    
    xcoord = 0.0
    ycoord = 0.0

    for i in range(2**ADDR_WIDTH):
        rwlBuff_stripe.add_component(buffer, rwlBuff_name%(i), xcoord, ycoord)
        ycoord += sc['site']		
        for net in [('IN', sc['buffer']['in']), ('OUT', sc['buffer']['out'])]:
            rwlBuff_stripe.connect(net[0]+str([i]), rwlBuff_name%(i)+'.'+net[1])


################################################################
####################   write verilog file   ####################
################################################################
def write_verilog_file(params,scm):
    export_folder = 'export'
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)

    verilog_file_name = export_folder + '/' + params['TOPLEVEL'] + '.post_py.v'
    
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
    
    for module_name in scm.values():
        verilog_module_folder = verilog_files_folder+'/'+str(module_name)
        if not os.path.exists(verilog_module_folder):
            os.makedirs(verilog_module_folder)
        
        verilog_file_name = verilog_module_folder+'/'+str(module_name)+'.v'
        verilog_file=open(verilog_file_name,'w')

        for line in module_name.write_verilog():
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

    tcl_file_name = export_folder + '/' + params['TOPLEVEL'] + '_cells_position.tcl'
    
    tcl_file=open(tcl_file_name,'w')
    
    #for module in scm.values():
    for module in [scm['TOP']]:
        tcl_file.write('######' + str(module) + '\n')
        tcl_file.write(module.write_floorPlan_tcl_commands('sc12_cln65lp') + '\n\n')
        
        for line in module.write_tcl_placement_commands():	# standatd cells placement
            tcl_file.write(line + '\n')
        tcl_file.write('\n\n\n')
        for line in module.write_pin_tcl_placement_commands():	# pin placement
            tcl_file.write(line + '\n')
        tcl_file.write('\n\n\n')

        for line in module.write_addStripe_tcl_commands():	# addStripe commands
            tcl_file.write(line + '\n')



if __name__ == '__main__':
    main()

