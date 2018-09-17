create_clock -period $design(CLK_PERIOD) -name $design(CLK_NAME) \
 		[get_ports $design(CLK_PORT)]

if {$runtype=="synthesis"} {
        set_ideal_network [get_ports $design(CLK_PORT)]
#	set_false_path -from $design(RST_PORT)
}

set_input_delay -clock $design(CLK_NAME) $design(OUTPUT_DELAY) \
        [remove_from_collection [all_inputs] $design(CLK_PORT)]
set_output_delay -clock $design(CLK_NAME)  $design(OUTPUT_DELAY) [all_outputs]
set_max_delay [expr $design(CLK_PERIOD)/2] -from [all_inputs] -to [all_outputs]


#set_driving_cell -lib_cell  $tech_files(SDC_DRIVING_CELL)  [all_inputs]
set_input_transition 0.05 [all_inputs]

if {$runtype=="synthesis"} {
        set tech_files(SDC_LOAD_VALUE) [expr [get_attribute load $tech_files(SDC_LOAD_PIN)]/1000]
} elseif {$runtype =="pnr"} {
        set tech_files(SDC_LOAD_VALUE) [lindex [get_property [get_lib_pins $tech_files(SDC_LOAD_PIN)] capacitance] 0]
}

set_load $tech_files(SDC_LOAD_VALUE)  [all_outputs]

#set_case_analysis 0 [get_ports $design(SCAN_MODE_PORT)]

#set_dont_touch [get_designs pads]


set_multicycle_path -setup -through [get_pins */MemoryLatch_reg*/Q*] -to [get_ports DOUT*] 2
set_multicycle_path -hold -through [get_pins */MemoryLatch_reg*/Q*] -to [get_ports DOUT*] 1

# Dont touch instantiated cells
set dont_touch_modules [list \
    *mux \
    *CLK*_gate  ]
foreach module $dont_touch_modules {
    set_dont_touch [get_cells -hier $module]
}

if {$runtype == "pnr"} {
    set dont_touch_nets [list \
        */*DGWClkRightNet* \
        */*DGWClkLeftNet* ]
#        */*DGWClkNetToBuff* ]
    foreach net $dont_touch_nets {
        set_dont_touch $net
    }
}


