####################### standard_cell #######################
import sys, os
from salamandra import *
from define_parameters import *

TRACKS = 12

sc = {}     # standard_cell

if param['technology'] == 'tsmc65':
	sc['site'] = 2.4
	#sc['site'] = 1

	sc['latch'] = {}
	sc['latch']['component'] = ComponentXY('LATQ_X1M_A'+str(TRACKS)+'TR')
	sc['latch']['in'] = 'D'
	sc['latch']['component'].add_pin(Input(sc['latch']['in']))
	sc['latch']['clk'] = 'G'     
	sc['latch']['component'].add_pin(Input(sc['latch']['clk']))
	sc['latch']['out'] = 'Q'    
	sc['latch']['component'].add_pin(Output(sc['latch']['out']))
	sc['latch']['width'] = 2.4
	sc['latch']['component'].set_component_dimensions(sc['latch']['width'], sc['site'])

	sc['flipflop'] = {}
	sc['flipflop']['component'] = ComponentXY('DFFQ_X2M_A'+str(TRACKS)+'TR')
	sc['flipflop']['in'] = 'D'
	sc['flipflop']['component'].add_pin(Input(sc['flipflop']['in'])) 
	sc['flipflop']['clk'] = 'CK'
	sc['flipflop']['component'].add_pin(Input(sc['flipflop']['clk']))
	sc['flipflop']['out'] = 'Q'
	sc['flipflop']['component'].add_pin(Output(sc['flipflop']['out']))    
	sc['flipflop']['width'] = 4.4
	sc['flipflop']['component'].set_component_dimensions(sc['flipflop']['width'], sc['site'])
    
	sc['buffer'] = {}
	sc['buffer']['component'] = ComponentXY('BUFH_X3M_A'+str(TRACKS)+'TR')
	sc['buffer']['in'] = 'A'
	sc['buffer']['component'].add_pin(Input(sc['buffer']['in']))    
	sc['buffer']['out'] = 'Y'
	sc['buffer']['component'].add_pin(Output(sc['buffer']['out']))    
	sc['buffer']['width'] = 1.6
	sc['buffer']['component'].set_component_dimensions(sc['buffer']['width'], sc['site'])

	sc['inverter'] = {}
	sc['inverter']['component'] = ComponentXY('INV_X1B_A'+str(TRACKS)+'TR')
	sc['inverter']['in'] = 'A'
	sc['inverter']['component'].add_pin(Input(sc['inverter']['in']))
	sc['inverter']['out'] = 'Y'
	sc['inverter']['component'].add_pin(Input(sc['inverter']['out']))
	sc['inverter']['width'] = 0.6
	sc['inverter']['component'].set_component_dimensions(sc['inverter']['width'], sc['site'])

	sc['NAND2'] = {}
	sc['NAND2']['component'] = ComponentXY('NAND2_X1A_A'+str(TRACKS)+'TR')
	sc['NAND2']['in_1'] = 'A'
	sc['NAND2']['component'].add_pin(Input(sc['NAND2']['in_1']))  
	sc['NAND2']['in_2'] = 'B'
	sc['NAND2']['component'].add_pin(Input(sc['NAND2']['in_2'])) 
	sc['NAND2']['out'] = 'Y'   
	sc['NAND2']['component'].add_pin(Output(sc['NAND2']['out']))    
	sc['NAND2']['width'] = 0.8
	sc['NAND2']['component'].set_component_dimensions(sc['NAND2']['width'], sc['site'])

	sc['NAND3'] = {}
	sc['NAND3']['component'] = ComponentXY('NAND3_X1A_A'+str(TRACKS)+'TR')
	sc['NAND3']['in_1'] = 'A'
	sc['NAND3']['component'].add_pin(Input(sc['NAND3']['in_1']))  
	sc['NAND3']['in_2'] = 'B'
	sc['NAND3']['component'].add_pin(Input(sc['NAND3']['in_2'])) 
	sc['NAND3']['in_3'] = 'C'
	sc['NAND3']['component'].add_pin(Input(sc['NAND3']['in_3']))
	sc['NAND3']['out'] = 'Y'   
	sc['NAND3']['component'].add_pin(Output(sc['NAND3']['out']))    
	sc['NAND3']['width'] = 1.2
	sc['NAND3']['component'].set_component_dimensions(sc['NAND3']['width'], sc['site'])

	sc['NAND4'] = {}
	sc['NAND4']['component'] = ComponentXY('NAND4_X1A_A'+str(TRACKS)+'TR')
	sc['NAND4']['in_1'] = 'A'
	sc['NAND4']['component'].add_pin(Input(sc['NAND4']['in_1']))  
	sc['NAND4']['in_2'] = 'B'
	sc['NAND4']['component'].add_pin(Input(sc['NAND4']['in_2'])) 
	sc['NAND4']['in_3'] = 'C'
	sc['NAND4']['component'].add_pin(Input(sc['NAND4']['in_3']))
	sc['NAND4']['in_4'] = 'D'
	sc['NAND4']['component'].add_pin(Input(sc['NAND4']['in_4'])) 	
	sc['NAND4']['out'] = 'Y'   
	sc['NAND4']['component'].add_pin(Output(sc['NAND4']['out']))    
	sc['NAND4']['width'] = 1.4
	sc['NAND4']['component'].set_component_dimensions(sc['NAND4']['width'], sc['site'])

	sc['NOR2'] = {}
	sc['NOR2']['component'] = ComponentXY('NOR2_X1A_A'+str(TRACKS)+'TR')
	sc['NOR2']['in_1'] = 'A'
	sc['NOR2']['component'].add_pin(Input(sc['NOR2']['in_1']))    
	sc['NOR2']['in_2'] = 'B'
	sc['NOR2']['component'].add_pin(Input(sc['NOR2']['in_2']))   
	sc['NOR2']['out'] = 'Y'    
	sc['NOR2']['component'].add_pin(Output(sc['NOR2']['out']))    
	sc['NOR2']['width'] = 0.8
	sc['NOR2']['component'].set_component_dimensions(sc['NOR2']['width'], sc['site'])

	sc['NOR3'] = {}
	sc['NOR3']['component'] = ComponentXY('NOR3_X1A_A'+str(TRACKS)+'TR')
	sc['NOR3']['in_1'] = 'A'
	sc['NOR3']['component'].add_pin(Input(sc['NOR3']['in_1']))    
	sc['NOR3']['in_2'] = 'B'
	sc['NOR3']['component'].add_pin(Input(sc['NOR3']['in_2']))
	sc['NOR3']['in_3'] = 'C'
	sc['NOR3']['component'].add_pin(Input(sc['NOR3']['in_3']))   	
	sc['NOR3']['out'] = 'Y'    
	sc['NOR3']['component'].add_pin(Output(sc['NOR3']['out']))    
	sc['NOR3']['width'] = 1.2
	sc['NOR3']['component'].set_component_dimensions(sc['NOR3']['width'], sc['site'])	
  	 
	sc['well_tap'] = {}
	sc['well_tap']['component'] = ComponentXY('WELLANTENNATIEPW2_A'+str(TRACKS)+'TR')
	sc['well_tap']['width'] = 0.4
	sc['well_tap']['component'].set_component_dimensions(sc['well_tap']['width'], sc['site'])

	sc['latch_clock_gate'] = {}
	sc['latch_clock_gate']['component'] = ComponentXY('PREICG_X0P5B_A'+str(TRACKS)+'TR')
	sc['latch_clock_gate']['clk'] = 'CK'
	sc['latch_clock_gate']['component'].add_pin(Input(sc['latch_clock_gate']['clk']))    
	sc['latch_clock_gate']['E'] = 'E'
	sc['latch_clock_gate']['component'].add_pin(Input(sc['latch_clock_gate']['E']))    
	sc['latch_clock_gate']['SE'] = 'SE'
	sc['latch_clock_gate']['component'].add_pin(Input(sc['latch_clock_gate']['SE']))    
	sc['latch_clock_gate']['out'] = 'ECK'
	sc['latch_clock_gate']['component'].add_pin(Output(sc['latch_clock_gate']['out']))    
	sc['latch_clock_gate']['width'] = 3.4
	sc['latch_clock_gate']['component'].set_component_dimensions(sc['latch_clock_gate']['width'], sc['site'])

else:
	pass

