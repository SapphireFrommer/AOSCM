####################### standard_cell #######################
from salamandra import *
from define_parameters import *

standard_cell = {}

if param['technology'] == 'tsmc65':
    standard_cell['latch'] = Component('LATQ_X1M_A12TR')
    standard_cell['latch'].add_pin(Input('D'))    
    standard_cell['latch'].add_pin(Input('G'))
    standard_cell['latch'].add_pin(Output('Q'))

    standard_cell['flipflop'] = Component('DFFQ_X2M_A12TR')
    standard_cell['flipflop'].add_pin(Input('D'))    
    standard_cell['flipflop'].add_pin(Input('CK'))    
    standard_cell['flipflop'].add_pin(Output('Q'))    
    
    standard_cell['buffer'] = Component('BUFH_X3M_A12TR')
    standard_cell['buffer'].add_pin(Input('A'))    
    standard_cell['buffer'].add_pin(Output('Y'))    

    standard_cell['NAND2'] = Component('NAND2_X1A_A12TR')
    standard_cell['NAND2'].add_pin(Input('A'))    
    standard_cell['NAND2'].add_pin(Input('B'))    
    standard_cell['NAND2'].add_pin(Output('Y'))    

    standard_cell['NOR2'] = Component('NOR2_X1A_A12TR')
    standard_cell['NOR2'].add_pin(Input('A'))    
    standard_cell['NOR2'].add_pin(Input('B'))    
    standard_cell['NOR2'].add_pin(Output('Y'))    

    standard_cell['well_tap'] = Component('WELLANTENNATIEPW2_A12TR')

    standard_cell['latch_clock_gate'] = Component('PREICG_X0P5B_A12TR')
    standard_cell['latch_clock_gate'].add_pin(Input('CK'))    
    standard_cell['latch_clock_gate'].add_pin(Input('E'))    
    standard_cell['latch_clock_gate'].add_pin(Input('SE'))    
    standard_cell['latch_clock_gate'].add_pin(Output('ECK'))    

else:
    pass

