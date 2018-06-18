set runtype "pnr"
set TOPLEVEL "scm65"
set debugState 1

############################################
# Init Design
############################################
setDesignMode -process 65

# Set up specific defines for this run
source ../${TOPLEVEL}.defines
# Set up the "paths" and "tech_files" variables to describe the installation information
source ../libraries.tcl

# Defined in ARM SC user scripts
setNanoRouteMode -quiet -routeWithViaInPin true

# Setup initialization variables
set init_gnd_net [lsort -uniq "$design(digital_gnd) $design(io_gnd) $design(additional_ground_nets)"]
set init_pwr_net [lsort -uniq "$design(digital_vdd) $design(io_vdd) $design(additional_power_nets)"]
set init_lef_file [list \
			$tech_files(TECHNOLOGY_LEF) \
			$tech_files(STANDARD_CELLS_RVT_LEF) \
		  ]
set init_verilog ../../export/scm65.post_py.v
set init_mmmc_file ../${TOPLEVEL}.mmmc

if {$design(FULLCHIP_OR_MACRO)=="FULLCHIP"} {
	set init_io_file $design(io_file)
}

# Import and initialize design
foreach msg $tech_files(STANDARD_CELL_SUPPRESS_MESSAGES) {
	suppressMessage $msg
}
set init_design_uniquify 1

init_design



source ../../export/scm65_cells_position.tcl

sroute -connect { corePin }  -nets { vdd gnd } -layerChangeRange { M1(1) AP(8) } \
    -blockPinTarget { nearestTarget } -corePinTarget { firstAfterRowEnd } \
    -allowJogging 1 -crossoverViaLayerRange { M1(1) AP(8) } -allowLayerChange 1 \
    -targetViaLayerRange { M1(1) AP(8) }

refinePlace





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

#####################
# lef and lib
#####################
verifyProcessAntenna 
lefOut $design(export_dir)/innovus/$TOPLEVEL.lef
# do_extract_model -chek $design(export_dir)/innovus/$TOPLEVEL.lib

exit
