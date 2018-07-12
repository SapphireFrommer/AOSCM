set runtype "power_reports"
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


#restoreDesign $design(export_dir)/${TOPLEVEL}.post_route.enc ${TOPLEVEL}
# In Voltus 
restoreDesign $design(export_dir)/${TOPLEVEL}.post_route.enc.dat ${TOPLEVEL}

# Connect Global Nets
clearGlobalNets
# Connect standard cells to VDD and GND
globalNetConnect $design(digital_gnd) -pin $tech_files(STANDARD_CELL_GND) -all -verbose
globalNetConnect $design(digital_vdd) -pin $tech_files(STANDARD_CELL_VDD) -all -verbose
# Connect constants
globalNetConnect $design(digital_vdd) -type tiehi -pin $tech_files(STANDARD_CELL_VDD) -all -verbose 
globalNetConnect $design(digital_gnd) -type tielo -pin $tech_files(STANDARD_CELL_GND) -all -verbose 


set tb_name tb_scm65
set dut_name MEM
set tcf_scope "$tb_name"
set design(backannotation_scope) "$tcf_scope/MEM"
set period 10
set number_of_writes 116
set number_of_reads 100
set vcd_start(write) 1
set vcd_end(write) [expr $vcd_start(write) + $number_of_writes * $period]
set vcd_start(read)  [expr $vcd_end(write)+1]
set vcd_end(read) [expr $vcd_start(read) + $number_of_reads * $period]

set tcf_file(write) "$design(backannotation_export_path)/write.tcf"
set tcf_file(read) "$design(backannotation_export_path)/read.tcf"
set vcd_file "$design(backannotation_export_path)/$tb_name.vcd"


foreach mode {write read} {
        set_power_analysis_mode -reset
        set_power_analysis_mode -method static -report_missing_nets true \
	        -analysis_view $design(power_analysis_view) 
        set_power_output_dir $design(reports_dir)
        set_default_switching_activity -reset
        #set_default_switching_activity -period $vcd_period
        set_power -reset
        set_powerup_analysis -reset
        set_powerup_analysis -mode accurate -ultrasim_simulation_mode ms
        set_dynamic_power_simulation -reset

        read_activity_file -reset 
       	read_activity_file -format TCF -scope $dut_name  $tcf_file($mode) 
        report_power -rail_analysis_format VS -outfile ${mode}_power.rpt

        read_activity_file -reset 
        read_activity_file -format VCD -scope "tb_scm65.MEM" -start $vcd_start($mode) -end $vcd_end($mode) $vcd_file 
        report_power -rail_analysis_format VS -outfile ${mode}_vcd_power.rpt
        


    }
exit
