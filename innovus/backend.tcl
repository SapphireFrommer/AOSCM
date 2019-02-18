set runtype "pnr"
set TOPLEVEL "scm65"
set debugState 1
set ScriptDir "../../innovus"

############################################
# Init Design
############################################
setDesignMode -process 65

# Set up specific defines for this run
source ${ScriptDir}/${TOPLEVEL}.defines
set design(salamandra_netlist) "$design(export_dir)/${TOPLEVEL}_57x64.post_py.v"

# Set up the "paths" and "tech_files" variables to describe the installation information
source ${ScriptDir}/libraries.tcl

# Defined in ARM SC user scripts
setNanoRouteMode -quiet -routeWithViaInPin true

# Setup initialization variables
set init_gnd_net [lsort -uniq "$design(digital_gnd) $design(io_gnd) $design(additional_ground_nets)"]
set init_pwr_net [lsort -uniq "$design(digital_vdd) $design(io_vdd) $design(additional_power_nets)"]
set init_lef_file [list \
			$tech_files(TECHNOLOGY_LEF) \
			$tech_files(STANDARD_CELLS_RVT_LEF) \
		  ]

set init_verilog $design(salamandra_netlist)

set init_mmmc_file $design(mmmc_view_file)

if {$design(FULLCHIP_OR_MACRO)=="FULLCHIP"} {
	set init_io_file $design(io_file)
}

# Import and initialize design
foreach msg $tech_files(STANDARD_CELL_SUPPRESS_MESSAGES) {
	suppressMessage $msg
}
set init_design_uniquify 1

init_design

#To speed up the pin assign:
setPinAssignMode -pinEditInBatch true  
set design(salamandra_tcl) "$design(export_dir)/${TOPLEVEL}_57x64_cells_position.tcl"
source $design(salamandra_tcl)
setPinAssignMode -pinEditInBatch false

#suspend


sroute -connect { corePin }  -nets "$design(digital_vdd) $design(digital_gnd)" \
    -layerChangeRange { M1(1) AP(8) } \
    -blockPinTarget { nearestTarget } -corePinTarget { firstAfterRowEnd } \
    -allowJogging 1 -crossoverViaLayerRange { M1(1) AP(8) } -allowLayerChange 1 \
    -targetViaLayerRange { M1(1) AP(8) }

refinePlace

report_timing -to [all_outputs ] -format "hpin cell fanout load pin_load wire_load delay slew arrival" -net 




getAnalysisMode
setAnalysisMode -analysisType onChipVariation

# Connect Global Nets
clearGlobalNets
# Connect standard cells to VDD and GND
globalNetConnect $design(digital_gnd) -pin $tech_files(STANDARD_CELL_GND) -all -verbose
globalNetConnect $design(digital_vdd) -pin $tech_files(STANDARD_CELL_VDD) -all -verbose
# Connect constants
globalNetConnect $design(digital_vdd) -type tiehi -pin $tech_files(STANDARD_CELL_VDD) -all -verbose 
globalNetConnect $design(digital_gnd) -type tielo -pin $tech_files(STANDARD_CELL_GND) -all -verbose 



fit

getDrawView
loadWorkspace -name Physical
win
fit

# set_db [get_db insts *] .place_status fixed
set_db [get_db insts *] .dont_touch size_ok

# place
# CTS
routeDesign




saveDesign $design(export_dir)/${TOPLEVEL}.post_route.enc -relativePath
write_sdf  -precision 4 -min_period_edges posedge -recompute_parallel_arcs \
    -no_escape $design(export_dir)/${TOPLEVEL}.sdf ;       #check for the -view_typ
saveNetlist  $design(export_dir)/${TOPLEVEL}.post_route.v
# This one generally works with modelsim SDF backannotation
saveNetlist $design(backannotation_netlist) -excludeLeafCell

#redirect summaryFile.txt "source ../innovus/scripts/createRelevantReports.tcl"
reportWire -detail $design(reports_dir)/reportWireLength.post_route.txt
verifyGeometry -report $design(reports_dir)/verifyGeometry.post_route.txt
verifyConnectivity -report $design(reports_dir)/verifyConnectivity.post_route.txt


#####################
# lef and lib
#####################
verifyProcessAntenna 
# lefOut $design(export_dir)/$TOPLEVEL.lef		#need to replace by: write_lef_abstract command.
# do_extract_model -chek $design(export_dir)/$TOPLEVEL.lib

exit

# freeDesign # to delete the whole design at innovus 17.1
#
#
#
# report_timing -to [all_outputs ] -format "hpin cell fanout load pin_load wire_load delay slew arrival" -net 
# set_db [get_db insts *] .place_status fixed
# place_design
# set_db [get_db insts *] .place_status placed
# set_db [get_db insts *] .dont_touch size_ok
# optDesign -postCTS
#
# dbGet [dbGetInstByName bitslice_35/MemoryLatch_reg_56].pStatus                                              
#
# report_timing -to [all_outputs ] -machine_readable > dout.tarpt
# get_ports
#
#
#
