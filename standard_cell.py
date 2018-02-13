####################### standard_cell #######################
from salamandra import *
from define_parameters import *

standard_cell = {}

if param['technology'] == 'tsmc65':
    standard_cell['latch'] = {}
    standard_cell['latch']['component'] = Component('LATQ_X1M_A12TR')
    standard_cell['latch']['in'] = 'D'
    standard_cell['latch']['component'].add_pin(Input(standard_cell['latch']['in']))
    standard_cell['latch']['clk'] = 'G'     
    standard_cell['latch']['component'].add_pin(Input(standard_cell['latch']['clk']))
    standard_cell['latch']['out'] = 'Q'    
    standard_cell['latch']['component'].add_pin(Output(standard_cell['latch']['out']))

    standard_cell['flipflop'] = {}
    standard_cell['flipflop']['component'] = Component('DFFQ_X2M_A12TR')
    standard_cell['flipflop']['in'] = 'D'
    standard_cell['flipflop']['component'].add_pin(Input(standard_cell['flipflop']['in'])) 
    standard_cell['flipflop']['clk'] = 'CK'
    standard_cell['flipflop']['component'].add_pin(Input(standard_cell['flipflop']['clk']))
    standard_cell['flipflop']['out'] = 'Q'
    standard_cell['flipflop']['component'].add_pin(Output(standard_cell['flipflop']['out']))    
    
    standard_cell['buffer'] = {}
    standard_cell['buffer']['component'] = Component('BUFH_X3M_A12TR')
    standard_cell['buffer']['in'] = 'A'
    standard_cell['buffer']['component'].add_pin(Input(standard_cell['buffer']['in']))    
    standard_cell['buffer']['out'] = 'Y'
    standard_cell['buffer']['component'].add_pin(Output(standard_cell['buffer']['out']))    

    standard_cell['inverter'] = {}
    standard_cell['inverter']['component'] = Component('INV_X1B_A12TR')
    standard_cell['inverter']['in'] = 'A'
    standard_cell['inverter']['component'].add_pin(Input(standard_cell['inverter']['in']))
    standard_cell['inverter']['out'] = 'Y'
    standard_cell['inverter']['component'].add_pin(Input(standard_cell['inverter']['out']))

    standard_cell['NAND2'] = {}
    standard_cell['NAND2']['component'] = Component('NAND2_X1A_A12TR')
    standard_cell['NAND2']['in_1'] = 'A'
    standard_cell['NAND2']['component'].add_pin(Input(standard_cell['NAND2']['in_1']))  
    standard_cell['NAND2']['in_2'] = 'B'
    standard_cell['NAND2']['component'].add_pin(Input(standard_cell['NAND2']['in_2'])) 
    standard_cell['NAND2']['out'] = 'Y'   
    standard_cell['NAND2']['component'].add_pin(Output(standard_cell['NAND2']['out']))    

    standard_cell['NOR2'] = {}
    standard_cell['NOR2']['component'] = Component('NOR2_X1A_A12TR')
    standard_cell['NOR2']['in_1'] = 'A'
    standard_cell['NOR2']['component'].add_pin(Input(standard_cell['NOR2']['in_1']))    
    standard_cell['NOR2']['in_2'] = 'B'
    standard_cell['NOR2']['component'].add_pin(Input(standard_cell['NOR2']['in_2']))   
    standard_cell['NOR2']['out'] = 'Y'    
    standard_cell['NOR2']['component'].add_pin(Output(standard_cell['NOR2']['out']))    

    standard_cell['well_tap'] = Component('WELLANTENNATIEPW2_A12TR')

    standard_cell['latch_clock_gate'] = {}
    standard_cell['latch_clock_gate']['component'] = Component('PREICG_X0P5B_A12TR')
    standard_cell['latch_clock_gate']['clk'] = 'CK'
    standard_cell['latch_clock_gate']['component'].add_pin(Input(standard_cell['latch_clock_gate']['clk']))    
    standard_cell['latch_clock_gate']['E'] = 'E'
    standard_cell['latch_clock_gate']['component'].add_pin(Input(standard_cell['latch_clock_gate']['E']))    
    standard_cell['latch_clock_gate']['SE'] = 'SE'
    standard_cell['latch_clock_gate']['component'].add_pin(Input(standard_cell['latch_clock_gate']['SE']))    
    standard_cell['latch_clock_gate']['out'] = 'ECK'
    standard_cell['latch_clock_gate']['component'].add_pin(Output(standard_cell['latch_clock_gate']['out']))    

else:
    pass

