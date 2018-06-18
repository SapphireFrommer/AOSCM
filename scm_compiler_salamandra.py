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
    SCM_design(param,scm)
    write_verilog_file(param,scm)
    write_tcl(param,scm)


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
    scm['TOP'] = ComponentXY(param['TOPLEVEL'])
    TOP = scm['TOP']
    for pin in ['CLK', 'WE', 'RE', 'SE']:
        TOP.add_pin(Input(pin))
    for pin in ['WADDR', 'RADDR']:
        TOP.add_pinbus(Bus(Input, pin, ADDR_WIDTH))
    TOP.add_pinbus(Bus(Input, 'DIN', param['DATA_WIDTH']))
    TOP.add_pinbus(Bus(Output, 'DOUT', param['DATA_WIDTH']))

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

    ##### define a welltap_strip    
    scm['welltap_strip'] = ComponentXY('welltap_strip')
    welltap_strip = scm['welltap_strip']

    ##### define a rwlBuff_strip    
    scm['rwlBuff_strip'] = ComponentXY('rwlBuff_strip')
    rwlBuff_strip = scm['rwlBuff_strip']
    rwlBuff_strip.add_pinbus(Bus(Input, 'IN', 2**ADDR_WIDTH))
    rwlBuff_strip.add_pinbus(Bus(Output, 'OUT', 2**ADDR_WIDTH))
        

##############################################################################################
###############   add components, internal nets and connectivity to modules   ################
##############################################################################################
def SCM_design_components_instances(param, scm):

    SCM_design_components_instances_MidGap_DGWCLK(param, scm)
    SCM_design_components_instances_Decoder_x_x(param, scm)
    SCM_design_components_instances_row_decoder(param, scm)
    SCM_design_components_instances_welltap_strip(param, scm)
    SCM_design_components_instances_rwlBuff_strip(param, scm)
    SCM_design_components_instances_read_mux(param, scm)
    SCM_design_components_instances_bitslice(param, scm)
    SCM_design_components_instances_TOP(param, scm)


##########################################################
# add components to TOP module
##########################################################
def SCM_design_components_instances_TOP(param, scm):
	# aliases:
	ADDR_WIDTH = param['ADDR_WIDTH']
	TOP = scm['TOP']
	welltap_strip = scm['welltap_strip']
	bitslice = scm['bitslice']
	bitslice_odd = scm['bitslice_odd']	
	rwlBuff_strip = scm['rwlBuff_strip']
	MidGap_DGWCLK = scm['MidGap_DGWCLK']
	row_decoder = scm['row_decoder']
	read_mux = scm['read_mux']
	latch_clock_gate = sc['latch_clock_gate']['component']

	#########################################################
	#		components										#
	#########################################################
	xcoord = 0.0
	ycoord = 0.0

	for i in range(param['DATA_WIDTH']):
		ycoord = 0.0
		if (i%param['WELLTAP']) == 0:
			TOP.add_component(welltap_strip, 'welltap_strip_'+str(i//8), xcoord, ycoord)
			xcoord += sc['well_tap']['width']
		# rwlBuff_strips
		K_RWL = param['DATA_WIDTH']//param['RWL_NUM']	# how many rwl buffer will be
		ycoord += sc['site']
		if (i%K_RWL == 0) & (i != 0) & (i < param['DATA_WIDTH']/2):   # left side
			TOP.add_component(rwlBuff_strip, 'rwlBuff_strip_'+str((i//K_RWL)-1), xcoord, ycoord+sc['site'])
			xcoord += sc['buffer']['width']

		if (i == param['DATA_WIDTH']//2):    # MidGap - 2 middle
			TOP.add_component(rwlBuff_strip, 'rwlBuff_strip_'+str((i//K_RWL)-1), xcoord, ycoord+sc['site'])
			xcoord += sc['buffer']['width']


			ycoord = 0.0
			TOP.add_component(row_decoder, 'read_decoder', xcoord, ycoord)
			for index in range(ADDR_WIDTH):
				pin = 'RADDR'+str([index])
				TOP.set_pin_position(pin, xcoord+0.2+(0.4*index), ycoord, 'BOTTOM', 2)
			
			read_decoder_width = 0.8
			xcoord += read_decoder_width

			t_xcoord = sc['buffer']['width']
			for gate in ['GDINCLK_gate', 'GWCLK_gate', 'GRCLK_gate']:
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
			write_decoder_width = 0.8
			xcoord += write_decoder_width

			ycoord += sc['site']
			TOP.add_component(rwlBuff_strip, 'rwlBuff_strip_'+str((i//K_RWL)), xcoord, ycoord+sc['site'])
			xcoord += sc['buffer']['width']	
					
		if (i%K_RWL == 0) & (i > param['DATA_WIDTH']/2):   # right side
			TOP.add_component(rwlBuff_strip, 'rwlBuff_strip_'+str((i//K_RWL)), xcoord, ycoord+sc['site'])
			xcoord += sc['buffer']['width']	


		t_xcoord = (sc['latch']['width']+sc['NAND2']['width']+sc['NAND2']['width'])-sc['flipflop']['width']
		ycoord = 0.0
		pin = 'DIN'+str([i])
		if (i%2) == 0:
			TOP.add_component(bitslice, 'bitslice_'+str(i), xcoord, ycoord)
			TOP.set_pin_position(pin, xcoord+3.5, ycoord, 'BOTTOM', 2)
		else:
			TOP.add_component(bitslice_odd, 'bitslice_'+str(i), xcoord, ycoord)
			TOP.set_pin_position(pin, xcoord+3.1, ycoord, 'BOTTOM', 2)
			
		pin = 'DOUT'+str([i])
		TOP.set_pin_position(pin, xcoord+3.7, ycoord, 'TOP', 2)
		
		bitslice_width = sc['flipflop']['width']+t_xcoord	# need to write better
		xcoord += bitslice_width	
		



	# last welltap strip:
	ycoord = 0.0
	TOP.add_component(welltap_strip, 'welltap_strip_'+str((param['DATA_WIDTH']//8)), xcoord, ycoord)
				
	#########################################################
	#		connectivity									#
	#########################################################
	
	

	# first level clock gates
    
	for gate in ['GDINCLK_gate', 'GWCLK_gate', 'GRCLK_gate']:
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

	TOP.add_netbus(Bus(Net, 'decoder_write_out', 2**ADDR_WIDTH))

	

	for i in range(param['DATA_WIDTH']):	
        # rwlBuff_strips (it's only a draft)
		K_RWL = param['DATA_WIDTH']//4
		if (i%K_RWL == 0) & (i != 0) & (i < param['DATA_WIDTH']/2):   # left side
			TOP.add_netbus(Bus(Net, 'rwlBuffNet_'+str((i//K_RWL)-1), 2**ADDR_WIDTH))
			TOP.add_netbus(Bus(Net, 'rwlBuffNet_'+str((i//K_RWL)), 2**ADDR_WIDTH))
			for row in range(2**ADDR_WIDTH):
				TOP.connect('rwlBuffNet_'+str((i//K_RWL)-1)+str([row]), 'rwlBuff_strip_'+str((i//K_RWL)-1)+'.OUT'+str([row]))
				TOP.connect('rwlBuffNet_'+str((i//K_RWL))+str([row]), 'rwlBuff_strip_'+str((i//K_RWL)-1)+'.IN'+str([row]))

		if (i == param['DATA_WIDTH']/2):    # 2 middle
			TOP.add_netbus(Bus(Net, 'decoder_read_out', 2**ADDR_WIDTH))
			TOP.add_netbus(Bus(Net, 'rwlBuffNet_'+str((i//K_RWL)), 2**ADDR_WIDTH))
			for row in range(2**ADDR_WIDTH):       
				TOP.connect('decoder_read_out'+str([row]), 'rwlBuff_strip_'+str((i//K_RWL)-1)+'.IN'+str([row]))                
				TOP.connect('rwlBuffNet_'+str((i//K_RWL)-1)+str([row]), 'rwlBuff_strip_'+str((i//K_RWL)-1)+'.OUT'+str([row]))

				TOP.connect('decoder_read_out'+str([row]), 'rwlBuff_strip_'+str((i//K_RWL))+'.IN'+str([row]))
				TOP.connect('rwlBuffNet_'+str((i//K_RWL))+str([row]), 'rwlBuff_strip_'+str((i//K_RWL))+'.OUT'+str([row]))


		if (i%K_RWL == 0) & (i > param['DATA_WIDTH']/2):   # right side
			TOP.add_netbus(Bus(Net, 'rwlBuffNet_'+str((i//K_RWL)), 2**ADDR_WIDTH))
			for row in range(2**ADDR_WIDTH):
				TOP.connect('rwlBuffNet_'+str((i//K_RWL)-1)+str([row]), 'rwlBuff_strip_'+str((i//K_RWL))+'.IN'+str([row]))
				TOP.connect('rwlBuffNet_'+str((i//K_RWL))+str([row]), 'rwlBuff_strip_'+str((i//K_RWL))+'.OUT'+str([row]))
            


        # bitslices
		TOP.connect('DIN'+str([i]), 'bitslice_'+str(i)+'.DIN')
		TOP.connect('DOUT'+str([i]), 'bitslice_'+str(i)+'.DOUT')
		TOP.connect('GDINCLK', 'bitslice_'+str(i)+'.clk')

        # DGWCLK net to bitslice connectivity
		if i < (param['DATA_WIDTH']/2):
			if i == 0:
				TOP.add_netbus(Bus(Net, 'DGWCLKLeftNet', 2**ADDR_WIDTH))
				TOP.add_netbus(Bus(Net, 'DGWClkRightNet', 2**ADDR_WIDTH))
			for j in range(2**ADDR_WIDTH):
				TOP.connect('DGWCLKLeftNet'+str([j]), 'bitslice_'+str(i)+'.DGWCLK'+str([j]))
		else:
			for j in range(2**ADDR_WIDTH):
				TOP.connect('DGWClkRightNet'+str([j]), 'bitslice_'+str(i)+'.DGWCLK'+str([j]))

		if i == ((param['DATA_WIDTH']/2)-1):    # MidGap
			TOP.connect('GWCLK', 'MidGap_DGWCLK.clk')
			TOP.connect('SE', 'MidGap_DGWCLK.SE')
			for j in range(2**ADDR_WIDTH):
				TOP.connect('DGWCLKLeftNet'+str([j]), 'MidGap_DGWCLK.DGWClkLeftNet'+str([j]))
				TOP.connect('DGWClkRightNet'+str([j]), 'MidGap_DGWCLK.DGWClkRightNet'+str([j]))
				TOP.connect('decoder_write_out'+str([j]), 'MidGap_DGWCLK.E'+str([j]))
			
			

	
	
	# bitslices RWL connectivity
	for row in range(2**ADDR_WIDTH):
		for col in range(param['DATA_WIDTH']):
			TOP.connect('rwlBuffNet_'+str(col//K_RWL)+str([row]), 'bitslice_'+str(col)+'.'+'RWL'+str([row]))
		TOP.connect('decoder_read_out'+str([row]), 'read_decoder''.decoder_out'+str([row]))
		TOP.connect('decoder_write_out'+str([row]), 'write_decoder''.decoder_out'+str([row]))

	for ADDR in range(ADDR_WIDTH):
		TOP.connect('RADDR'+str([ADDR]), 'read_decoder''.decoder_in'+str([ADDR]))
		TOP.connect('WADDR'+str([ADDR]), 'write_decoder''.decoder_in'+str([ADDR]))


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
		bitslice.add_component(MemoryLatch_reg, 'MemoryLatch_reg_'+str(i), xcoord, ycoord)
		ycoord += sc['site']
		#for net in ['MemoryLatch']:
			#bitslice.add_net(Net(net+str([i])))
		bitslice.connect('GDIN', 'MemoryLatch_reg_'+str(i)+'.'+sc['latch']['in'])         
		for net in [('MemoryLatch',sc['latch']['out']), ('DGWCLK', sc['latch']['clk'])]:
			bitslice.connect(net[0]+str([i]), 'MemoryLatch_reg_'+str(i)+'.'+net[1]) #conectivty to MemoryLatch_reg
		for net in ['MemoryLatch', 'RWL']:
			bitslice.connect(net+str([i]), 'read_mux.'+net+str([i]))    #conectivty to read_mux
    

	scm['bitslice_odd'] = bitslice.copy('bitslice_odd')
	xcoord = (sc['latch']['width']+sc['NAND2']['width']+sc['NAND2']['width'])-sc['flipflop']['width']
	scm['bitslice_odd'].set_position('GDIN_reg', xcoord, sc['site'])
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

    xcoord = 0.0
    ycoord = 0.0

    for level in range(1, ADDR_WIDTH+2):
        ycoord = 0.0
        if (level != 1):
            initial_Offset = ((2**(level-2))-1)     # is used to figure out what the first row for this level is
            gap_Between_Gates = (2**(level-1))      # is how many rows between gates at this level
            ycoord += initial_Offset*sc['site']            

        if level == 1:      # add and connect level_1 NAND2
            read_mux.add_netbus(Bus(Net, 'w'+str(level-1), 2**ADDR_WIDTH))
            for i in range(2**ADDR_WIDTH):
                read_mux.add_component(NAND2, 'level_'+str(level)+'_'+str(i), xcoord, ycoord)
                ycoord += sc['site']
                #read_mux.add_net(Net('w'+str(level-1)+str([i])))
                for pin in [('MemoryLatch', sc['NAND2']['in_1']), ('RWL', sc['NAND2']['in_2']), ('w'+str(level-1), sc['NAND2']['out'])]:
                    read_mux.connect(pin[0]+str([i]), 'level_'+str(level)+'_'+str(i)+'.'+pin[1])

        if level == 2:      # add and connect level_2 NAND2
            xcoord += sc['NAND2']['width']
            read_mux.add_netbus(Bus(Net, 'w'+str(level-1), (2**ADDR_WIDTH)>>1))
            for i in range((2**ADDR_WIDTH)>>1):
                read_mux.add_component(NAND2, 'level_'+str(level)+'_'+str(i), xcoord, ycoord)
                ycoord += gap_Between_Gates*sc['site']
                #read_mux.add_net(Net('w'+str(level-1)+str([i])))
                for pin in [('w'+str(level-2)+str([2*i]), sc['NAND2']['in_1']), ('w'+str(level-2)+str([2*i+1]), sc['NAND2']['in_2']), ('w'+str(level-1)+str([i]), sc['NAND2']['out'])]:
                    read_mux.connect(pin[0], 'level_'+str(level)+'_'+str(i)+'.'+pin[1])

        if (level%2) & (level != 1):        # add and connect levels 3,5,7..... -> in odd levels there are NOR2 gates
            read_mux.add_netbus(Bus(Net, 'w'+str(level-1), (2**ADDR_WIDTH)>>(level-1)))   
            for i in range((2**ADDR_WIDTH)>>(level-1)):
                read_mux.add_component(NOR2, 'level_'+str(level)+'_'+str(i), xcoord, ycoord)
                ycoord += gap_Between_Gates*sc['site']            
                #read_mux.add_net(Net('w'+str(level-1)+str([i])))
                for pin in [('w'+str(level-2)+str([2*i]), sc['NOR2']['in_1']), ('w'+str(level-2)+str([2*i+1]), sc['NOR2']['in_2']), ('w'+str(level-1)+str([i]), sc['NOR2']['out'])]:
                    read_mux.connect(pin[0], 'level_'+str(level)+'_'+str(i)+'.'+pin[1])            

        if (level%2 == 0) & (level != 2):       # add and connect levels 4,6,8..... -> in even levels there are NAND2 gates
            read_mux.add_netbus(Bus(Net, 'w'+str(level-1), (2**ADDR_WIDTH)>>(level-1)))
            for i in range((2**ADDR_WIDTH)>>(level-1)):
                read_mux.add_component(NAND2, 'level_'+str(level)+'_'+str(i), xcoord, ycoord)
                ycoord += gap_Between_Gates*sc['site']
                #read_mux.add_net(Net('w'+str(level-1)+str([i])))
                for pin in [('w'+str(level-2)+str([2*i]), sc['NAND2']['in_1']), ('w'+str(level-2)+str([2*i+1]), sc['NAND2']['in_2']), ('w'+str(level-1)+str([i]), sc['NAND2']['out'])]:
                    read_mux.connect(pin[0], 'level_'+str(level)+'_'+str(i)+'.'+pin[1])     
    
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
def SCM_design_components_instances_MidGap_DGWCLK(param, scm):
	# aliases:
	ADDR_WIDTH = param['ADDR_WIDTH']
	MidGap_DGWCLK = scm['MidGap_DGWCLK']
	buffer = sc['buffer']['component']
	latch_clock_gate = sc['latch_clock_gate']['component']
    
	xcoord = 0.0
	ycoord = 0.0

	xcoord_LeftBuff = xcoord
	xcoord_DGWCLK_gate = xcoord_LeftBuff+sc['buffer']['width']
	xcoord_RightBuff = xcoord_DGWCLK_gate+sc['latch_clock_gate']['width']
	
	MidGap_DGWCLK.add_netbus(Bus(Net, 'ECK', 2**ADDR_WIDTH))
	for i in range(2**ADDR_WIDTH):
		MidGap_DGWCLK.add_component(buffer, 'DGWClkLeftBuff_'+str(i), xcoord_LeftBuff, ycoord)
		MidGap_DGWCLK.add_component(latch_clock_gate, 'DGWCLK_gate_'+str(i), xcoord_DGWCLK_gate, ycoord)
		MidGap_DGWCLK.add_component(buffer, 'DGWClkRightBuff_'+str(i), xcoord_RightBuff, ycoord)
		ycoord += sc['site']
        
		MidGap_DGWCLK.connect('ECK'+str([i]), 'DGWCLK_gate_'+str(i)+'.'+sc['latch_clock_gate']['out'])
		MidGap_DGWCLK.connect('ECK'+str([i]), 'DGWClkLeftBuff_'+str(i)+'.'+sc['buffer']['in'])
		MidGap_DGWCLK.connect('ECK'+str([i]), 'DGWClkRightBuff_'+str(i)+'.'+sc['buffer']['in'])
		
		MidGap_DGWCLK.connect('E'+str([i]), 'DGWCLK_gate_'+str(i)+'.'+sc['latch_clock_gate']['E'])
		MidGap_DGWCLK.connect('clk', 'DGWCLK_gate_'+str(i)+'.'+sc['latch_clock_gate']['clk'])
		MidGap_DGWCLK.connect('SE', 'DGWCLK_gate_'+str(i)+'.'+sc['latch_clock_gate']['SE'])
        
		for net in ['DGWClkLeft', 'DGWClkRight']:
			MidGap_DGWCLK.connect(net+'Net'+str([i]), net+'Buff_'+str(i)+'.'+sc['buffer']['out'])



##########################################################
# add components to PreDecoder_x_x module
##########################################################
def SCM_design_components_instances_Decoder_x_x(param, scm):
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
			xcoord += sc['NAND3']['width']
			PreDecoder.connect('decoder_out'+str([n]), 'NAND'+str(ADDR_W)+'_'+str(n)+'.' + sc['NAND'+str(ADDR_W)]['out'])
		
			for a in range(ADDR_W):		# ----> this connects each input of the nand to this nand			
				if (n & 1<<(ADDR_W-1-a)):
					PreDecoder.connect('decoder_in'+str([ADDR_W-1-a]), 'NAND'+str(ADDR_W)+'_'+str(n)+'.' + sc['NAND'+str(ADDR_W)]['in_'+str(a+1)])										
				else: 
					PreDecoder.connect('in_not'+str([ADDR_W-1-a]), 'NAND'+str(ADDR_W)+'_'+str(n)+'.' + sc['NAND'+str(ADDR_W)]['in_'+str(a+1)])					


##########################################################
# add components to row_decoder module
##########################################################
def SCM_design_components_instances_row_decoder(param, scm):
	# aliases:
	ADDR_WIDTH = param['ADDR_WIDTH']
	PreDecoder_2_4 = scm['PreDecoder_2_4']
	PreDecoder_3_8 = scm['PreDecoder_3_8']	
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
		PreDec_list = [4,4]		
	
	NUM_PREDECS = len(PreDec_list)
	Num_PreDec_out_wires = 0
	for i in PreDec_list:
		Num_PreDec_out_wires += 2**i
	row_decoder.add_netbus(Bus(Net, 'PreDec_out', Num_PreDec_out_wires))
	xcoord = 0.0
	ycoord = 0.0
	
	for i in range(NUM_PREDECS):
		ycoord += i*sc['site']
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
	for row in range(2**ADDR_WIDTH):
		row_decoder.add_component(sc['NOR'+str(NUM_PREDECS)]['component'], 'PostDec_%02d'%(row), xcoord, ycoord)
		ycoord += sc['site']
		row_decoder.connect('decoder_out'+str([row]), 'PostDec_%02d'%(row)+'.' + sc['NOR'+str(NUM_PREDECS)]['out'])

	
	NUM_LOWER_BITS = 0
	NUM_CURRENT_BITS = 0
	for predec_num in range(NUM_PREDECS):
		NUM_LOWER_BITS += NUM_CURRENT_BITS				#---> increases the count of how many bits were in the last iteration
		NUM_CURRENT_BITS = PreDec_list[predec_num]			#---> can be passed in a list
		for row in range(2**ADDR_WIDTH):
			if NUM_LOWER_BITS ==0:
				WHICH_PREDEC_OUT = ((row >> NUM_LOWER_BITS) % (2**NUM_CURRENT_BITS))
			else:
				WHICH_PREDEC_OUT = ((row >> NUM_LOWER_BITS) % (2**NUM_CURRENT_BITS))+(2**NUM_LOWER_BITS)					
			row_decoder.connect('PreDec_out'+str([WHICH_PREDEC_OUT]), 'PostDec_%02d'%(row)+'.' + sc['NOR'+str(NUM_PREDECS)]['in_'+str(predec_num+1)])
			print(WHICH_PREDEC_OUT,row)
	
	"""
	if (ADDR_WIDTH == 4):
		##########  for PreDecoder_4_16 (predec = 2 x 2_4)   #############
		###############################################################
	
		########  Pre Decoder  ########
		row_decoder.add_netbus(Bus(Net, 'PreDec_out', 8))
		xcoord = 0.0
		ycoord = 0.0
		for i in range(2):
			ycoord += i*sc['site']
			t_xcoord = sc['buffer']['width']
			row_decoder.add_component(PreDecoder_2_4, 'PreDec_'+str(i), xcoord-t_xcoord, ycoord)
			#xcoord += 4.4

		for i in range(2):
			for j in range(2):
				if i==0:
					row_decoder.connect('decoder_in'+str([j]), 'PreDec_'+str(i)+'.decoder_in'+str([j]))
				else:
					row_decoder.connect('decoder_in'+str([j+2]), 'PreDec_'+str(i)+'.decoder_in'+str([j]))            
			for j in range(4):
				if i==0:
					row_decoder.connect('PreDec_out'+str([j]), 'PreDec_'+str(i)+'.decoder_out'+str([j]))
				else:
					row_decoder.connect('PreDec_out'+str([j+4]), 'PreDec_'+str(i)+'.decoder_out'+str([j]))
 
		########  Post Decoder  ########
		#row_decoder.add_netbus(Bus(Net, 'nand_out', 16)) 
		#for i in range(16):
		    #row_decoder.add_component(INV, 'INV_out_'+str(i))
		    #row_decoder.connect('decoder_out'+str([i]), 'INV_out_'+str(i)+'.' + sc['inverter']['out'])
		    #row_decoder.connect('nand_out'+str([i]), 'INV_out_'+str(i)+'.' + sc['inverter']['in'])

		xcoord = 0.0
		ycoord = 0.0
		ycoord += 2*sc['site']
		
		for row in range(16):
			row_decoder.add_component(NOR2, 'PostDec_'+str(row), xcoord, ycoord)
			ycoord += sc['site']
			row_decoder.connect('decoder_out'+str([row]), 'PostDec_'+str(row)+'.' + sc['NOR2']['out'])

		for row in range(16):
			if (row>=0)&(row<4):
				row_decoder.connect('PreDec_out'+str([4]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_1'])
			elif (row>=4)&(row<8):
				row_decoder.connect('PreDec_out'+str([5]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_1'])
			elif (row>=8)&(row<12):
				row_decoder.connect('PreDec_out'+str([6]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_1'])
			elif (row>=12)&(row<16):
				row_decoder.connect('PreDec_out'+str([7]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_1'])

			if (row%4)==0:
				row_decoder.connect('PreDec_out'+str([0]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_2'])
			elif (row%4)==1:
				row_decoder.connect('PreDec_out'+str([1]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_2'])
			elif (row%4)==2:
				row_decoder.connect('PreDec_out'+str([2]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_2'])
			elif (row%4)==3:
				row_decoder.connect('PreDec_out'+str([3]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_2'])

	elif (ADDR_WIDTH==5):
		#########  for Decoder_5_32 (predec = 2_4 + 3_8)   ############
		###############################################################
	
		########  Pre Decoder  ########
		row_decoder.add_netbus(Bus(Net, 'PreDec_out', 12))
		xcoord = 0.0
		ycoord = 0.0

		t_xcoord = sc['buffer']['width']
		row_decoder.add_component(PreDecoder_2_4, 'PreDec_'+str(0), xcoord-t_xcoord, ycoord)
		ycoord += sc['site']		
		row_decoder.add_component(PreDecoder_3_8, 'PreDec_'+str(1), xcoord-t_xcoord, ycoord)

		for i in range(5):
			if i<2:
				row_decoder.connect('decoder_in'+str([i]), 'PreDec_'+str(0)+'.decoder_in'+str([i]))
			else:
				row_decoder.connect('decoder_in'+str([i]), 'PreDec_'+str(1)+'.decoder_in'+str([i-2]))
				 
		for i in range(12):
			if i<4:
				row_decoder.connect('PreDec_out'+str([i]), 'PreDec_'+str(0)+'.decoder_out'+str([i]))
			else:
				row_decoder.connect('PreDec_out'+str([i]), 'PreDec_'+str(1)+'.decoder_out'+str([i-4]))
 
		########  Post Decoder  ########
		xcoord = 0.0
		ycoord = 0.0
		ycoord += 2*sc['site']

		for row in range(32):
			row_decoder.add_component(NOR2, 'PostDec_'+str(row), xcoord, ycoord)
			ycoord += sc['site']
			row_decoder.connect('decoder_out'+str([row]), 'PostDec_'+str(row)+'.' + sc['NOR2']['out'])

		for row in range(32):
			if (row>=0)&(row<4):
				row_decoder.connect('PreDec_out'+str([4]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_1'])
			elif (row>=4)&(row<8):
				row_decoder.connect('PreDec_out'+str([5]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_1'])
			elif (row>=8)&(row<12):
				row_decoder.connect('PreDec_out'+str([6]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_1'])
			elif (row>=12)&(row<16):
				row_decoder.connect('PreDec_out'+str([7]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_1'])
			elif (row>=16)&(row<20):
				row_decoder.connect('PreDec_out'+str([8]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_1'])
			elif (row>=20)&(row<24):
				row_decoder.connect('PreDec_out'+str([9]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_1'])
			elif (row>=24)&(row<28):
				row_decoder.connect('PreDec_out'+str([10]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_1'])
			elif (row>=28)&(row<32):
				row_decoder.connect('PreDec_out'+str([11]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_1'])

			if (row%4)==0:
				row_decoder.connect('PreDec_out'+str([0]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_2'])
			elif (row%4)==1:
				row_decoder.connect('PreDec_out'+str([1]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_2'])
			elif (row%4)==2:
				row_decoder.connect('PreDec_out'+str([2]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_2'])
			elif (row%4)==3:
				row_decoder.connect('PreDec_out'+str([3]), 'PostDec_'+str(row)+'.' + sc['NOR2']['in_2'])


	"""

##########################################################
# add components to welltap_strip module
##########################################################
def SCM_design_components_instances_welltap_strip(param, scm):
    # aliases:
	ADDR_WIDTH = param['ADDR_WIDTH']
	welltap_strip = scm['welltap_strip']
	xcoord = 0.0
	ycoord = 0.0

	for i in range((2**ADDR_WIDTH)+2):
		welltap_strip.add_component(sc['well_tap']['component'], 'welltap_'+str(i), xcoord, ycoord)
		ycoord += sc['site']

##########################################################
# add components to rwlBuff_strip module
##########################################################
def SCM_design_components_instances_rwlBuff_strip(param, scm):
    # aliases:
	ADDR_WIDTH = param['ADDR_WIDTH']
	rwlBuff_strip = scm['rwlBuff_strip']
	buffer = sc['buffer']['component']
	xcoord = 0.0
	ycoord = 0.0

	for i in range(2**ADDR_WIDTH):
		rwlBuff_strip.add_component(buffer, 'rwlBuff_'+str(i), xcoord, ycoord)
		ycoord += sc['site']		
		for net in [('IN', sc['buffer']['in']), ('OUT', sc['buffer']['out'])]:
			rwlBuff_strip.connect(net[0]+str([i]), 'rwlBuff_'+str(i)+'.'+net[1])


################################################################
####################   write verilog file   ####################
################################################################
def write_verilog_file(param,scm):
    export_folder = 'export'
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)

    verilog_file_name = export_folder + '/' + param['TOPLEVEL'] + '.post_py.v'
    
    header_comment_text = []
    module_scm_text = scm['TOP'].write_verilog()

    header_comment(header_comment_text, param, module_scm_text)    
    
    verilog_file=open(verilog_file_name,'w')

    for line in header_comment_text:
        verilog_file.write(line)
    
    for module in scm.values():
        for line in module.write_verilog():
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

    ##########  write python param as verilog define  ##########
    verilog_file_name = verilog_files_folder + '/define.v'
    verilog_file=open(verilog_file_name,'w')
    verilog_file.write("//####################### define parameter #######################\n")
    for p in sorted(param.keys()):
        s = '`define ' + p + ' ' + str(param[p])
        verilog_file.write(s + '\n')
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


################################################################
############   write tcl placement commands file   #############
################################################################
def write_tcl(param,scm):
	export_folder = 'export'
	if not os.path.exists(export_folder):
		os.makedirs(export_folder)

	tcl_file_name = export_folder + '/' + param['TOPLEVEL'] + '_cells_position.tcl'
    
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

	

if __name__ == '__main__':
    main()

