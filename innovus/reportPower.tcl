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


restoreDesign $design(export_dir)/${TOPLEVEL}.post_route.enc ${TOPLEVEL}


set tcf_file(write) "$design(backannotation_export_path)/write.tcf"
set tcf_file(read) "$design(backannotation_export_path)/read.tcf"

foreach mode {write read} {
        set_power_analysis_mode -method static -report_missing_nets true \
	        -analysis_view $design(power_analysis_view) 
        set_power_output_dir $design(reports_dir)
        set_default_switching_activity -reset
        #set_default_switching_activity -period $vcd_period
        set_power -reset
        set_powerup_analysis -reset
        set_powerup_analysis -mode accurate -ultrasim_simulation_mode ms
        set_dynamic_power_simulation -reset

       	read_activity_file -format TCF -scope $design(backannotation_scope) \
        	 $tcf_file($mode) 

	    report_power -rail_analysis_format VS \
            -outfile ${mode}_power.rpt

    }
exit
