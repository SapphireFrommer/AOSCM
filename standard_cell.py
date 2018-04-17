####################### standard_cell #######################
import sys, os
from salamandra import *
from define_parameters import *

sc = {}     # standard_cell

if param['technology'] == 'tsmc65':
    sc['site'] = 2.4

    sc['latch'] = {}
    sc['latch']['component'] = Component('LATQ_X1M_A12TR')
    sc['latch']['in'] = 'D'
    sc['latch']['component'].add_pin(Input(sc['latch']['in']))
    sc['latch']['clk'] = 'G'     
    sc['latch']['component'].add_pin(Input(sc['latch']['clk']))
    sc['latch']['out'] = 'Q'    
    sc['latch']['component'].add_pin(Output(sc['latch']['out']))
    sc['latch']['width'] = 2.4

    sc['flipflop'] = {}
    sc['flipflop']['component'] = Component('DFFQ_X2M_A12TR')
    sc['flipflop']['in'] = 'D'
    sc['flipflop']['component'].add_pin(Input(sc['flipflop']['in'])) 
    sc['flipflop']['clk'] = 'CK'
    sc['flipflop']['component'].add_pin(Input(sc['flipflop']['clk']))
    sc['flipflop']['out'] = 'Q'
    sc['flipflop']['component'].add_pin(Output(sc['flipflop']['out']))    
    sc['flipflop']['width'] = 4.4
    
    sc['buffer'] = {}
    sc['buffer']['component'] = Component('BUFH_X3M_A12TR')
    sc['buffer']['in'] = 'A'
    sc['buffer']['component'].add_pin(Input(sc['buffer']['in']))    
    sc['buffer']['out'] = 'Y'
    sc['buffer']['component'].add_pin(Output(sc['buffer']['out']))    
    sc['buffer']['width'] = 1.6

    sc['inverter'] = {}
    sc['inverter']['component'] = Component('INV_X1B_A12TR')
    sc['inverter']['in'] = 'A'
    sc['inverter']['component'].add_pin(Input(sc['inverter']['in']))
    sc['inverter']['out'] = 'Y'
    sc['inverter']['component'].add_pin(Input(sc['inverter']['out']))
    sc['inverter']['width'] = 0.6

    sc['NAND2'] = {}
    sc['NAND2']['component'] = Component('NAND2_X1A_A12TR')
    sc['NAND2']['in_1'] = 'A'
    sc['NAND2']['component'].add_pin(Input(sc['NAND2']['in_1']))  
    sc['NAND2']['in_2'] = 'B'
    sc['NAND2']['component'].add_pin(Input(sc['NAND2']['in_2'])) 
    sc['NAND2']['out'] = 'Y'   
    sc['NAND2']['component'].add_pin(Output(sc['NAND2']['out']))    
    sc['NAND2']['width'] = 0.8

    sc['NOR2'] = {}
    sc['NOR2']['component'] = Component('NOR2_X1A_A12TR')
    sc['NOR2']['in_1'] = 'A'
    sc['NOR2']['component'].add_pin(Input(sc['NOR2']['in_1']))    
    sc['NOR2']['in_2'] = 'B'
    sc['NOR2']['component'].add_pin(Input(sc['NOR2']['in_2']))   
    sc['NOR2']['out'] = 'Y'    
    sc['NOR2']['component'].add_pin(Output(sc['NOR2']['out']))    
    sc['NOR2']['width'] = 0.8
   
    sc['well_tap'] = {}
    sc['well_tap']['component'] = Component('WELLANTENNATIEPW2_A12TR')
    sc['well_tap']['width'] = 0.4

    sc['latch_clock_gate'] = {}
    sc['latch_clock_gate']['component'] = Component('PREICG_X0P5B_A12TR')
    sc['latch_clock_gate']['clk'] = 'CK'
    sc['latch_clock_gate']['component'].add_pin(Input(sc['latch_clock_gate']['clk']))    
    sc['latch_clock_gate']['E'] = 'E'
    sc['latch_clock_gate']['component'].add_pin(Input(sc['latch_clock_gate']['E']))    
    sc['latch_clock_gate']['SE'] = 'SE'
    sc['latch_clock_gate']['component'].add_pin(Input(sc['latch_clock_gate']['SE']))    
    sc['latch_clock_gate']['out'] = 'ECK'
    sc['latch_clock_gate']['component'].add_pin(Output(sc['latch_clock_gate']['out']))    
    sc['latch_clock_gate']['width'] = 3.4

else:
    pass

