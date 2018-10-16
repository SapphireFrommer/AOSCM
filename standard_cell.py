####################### standard_cell #######################
import sys, os
from salamandra import *
from standard_cell_from_tech import *
from define_parameters import *

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

TRACKS = param['TRACKS'] 

sc = {}     # standard_cell

if param['technology'] == 'tsmc65':
	sc['site'] = 2.4

	sc['latch'] = {}
	sc['latch']['component'] = str_to_class('LATQ_X1M_A'+TRACKS+'TR')()
	sc['latch']['in'] = 'D'
	sc['latch']['clk'] = 'G'     
	sc['latch']['out'] = 'Q'      
	sc['latch']['width'] = sc['latch']['component'].get_component_dimensions()[0]

	sc['flipflop'] = {}
	sc['flipflop']['component'] = str_to_class('DFFQ_X2M_A'+TRACKS+'TR')()
	sc['flipflop']['in'] = 'D'
	sc['flipflop']['clk'] = 'CK'
	sc['flipflop']['out'] = 'Q'
	sc['flipflop']['width'] = sc['flipflop']['component'].get_component_dimensions()[0]
    
	sc['buffer'] = {}
	sc['buffer']['component'] = str_to_class('BUFH_X3M_A'+TRACKS+'TR')()
	sc['buffer']['in'] = 'A'
	sc['buffer']['out'] = 'Y'
	sc['buffer']['width'] = sc['buffer']['component'].get_component_dimensions()[0]

	sc['inverter'] = {}
	sc['inverter']['component'] = str_to_class('INV_X1B_A'+TRACKS+'TR')()
	sc['inverter']['in'] = 'A'
	sc['inverter']['out'] = 'Y'
	sc['inverter']['width'] = sc['inverter']['component'].get_component_dimensions()[0]
	
	sc['NAND2'] = {}
	sc['NAND2']['component'] = str_to_class('NAND2_X1A_A'+TRACKS+'TR')()
	sc['NAND2']['in_1'] = 'A'
	sc['NAND2']['in_2'] = 'B'
	sc['NAND2']['out'] = 'Y'   
	sc['NAND2']['width'] = sc['NAND2']['component'].get_component_dimensions()[0]

	sc['NAND3'] = {}
	sc['NAND3']['component'] = str_to_class('NAND3_X1A_A'+TRACKS+'TR')()
	sc['NAND3']['in_1'] = 'A'
	sc['NAND3']['in_2'] = 'B'
	sc['NAND3']['in_3'] = 'C'
	sc['NAND3']['out'] = 'Y'   
	sc['NAND3']['width'] = sc['NAND3']['component'].get_component_dimensions()[0]

	sc['NAND4'] = {}
	sc['NAND4']['component'] = str_to_class('NAND4_X1A_A'+TRACKS+'TR')()
	sc['NAND4']['in_1'] = 'A'
	sc['NAND4']['in_2'] = 'B'
	sc['NAND4']['in_3'] = 'C'
	sc['NAND4']['in_4'] = 'D'
	sc['NAND4']['out'] = 'Y'   
	sc['NAND4']['width'] = sc['NAND4']['component'].get_component_dimensions()[0]

	sc['NOR2'] = {}
	sc['NOR2']['component'] = str_to_class('NOR2_X1A_A'+TRACKS+'TR')()
	sc['NOR2']['in_1'] = 'A'
	sc['NOR2']['in_2'] = 'B'
	sc['NOR2']['out'] = 'Y'    
	sc['NOR2']['width'] = sc['NOR2']['component'].get_component_dimensions()[0]

	sc['NOR3'] = {}
	sc['NOR3']['component'] = str_to_class('NOR3_X1A_A'+TRACKS+'TR')()
	sc['NOR3']['in_1'] = 'A'
	sc['NOR3']['in_2'] = 'B'
	sc['NOR3']['in_3'] = 'C'
	sc['NOR3']['out'] = 'Y'    
	sc['NOR3']['width'] = sc['NOR3']['component'].get_component_dimensions()[0]
  	 
	sc['well_tap'] = {}
	sc['well_tap']['component'] = ComponentXY('WELLANTENNATIEPW2_A'+str(TRACKS)+'TR')
	sc['well_tap']['width'] = 0.4
	sc['well_tap']['component'].set_component_dimensions(sc['well_tap']['width'], sc['site'])
	sc['well_tap']['component'].set_dont_uniq(True)
	#sc['well_tap']['component'].set_dont_write_verilog(True)

	sc['latch_clock_gate'] = {}
	sc['latch_clock_gate']['component'] = str_to_class('PREICG_X0P5B_A'+TRACKS+'TR')()
	sc['latch_clock_gate']['clk'] = 'CK'
	sc['latch_clock_gate']['E'] = 'E'
	sc['latch_clock_gate']['SE'] = 'SE'
	sc['latch_clock_gate']['out'] = 'ECK'
	sc['latch_clock_gate']['width'] = sc['latch_clock_gate']['component'].get_component_dimensions()[0]

else:
	pass

