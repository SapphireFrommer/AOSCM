# This script opens the waveform with all the signals and 
#   start the simulation until 1000ns and thne exports a pair of tcf files
#              read.tcf, write.tcf
#   execute this script with the command: simvision -input simCommands.tcl 

set tb_name tb_scm65
set dut_name MEM
set tcf_scope "$tb_name.$dut_name"
simvision set tcf_scope "$tb_name.$dut_name"
set tcf_file_write "../../export/write.tcf"
set tcf_file_read  "../../export/read.tcf"
set run_time_write 2000
set run_time_read  2000

 set w [simvision waveform new]
 simvision scope set $tcf_scope
 simvision waveform add -using "Waveform 1" -signals $tcf_scope
 run -time 1
 
 # Write Procedure
 dumptcf -output $tcf_file_write -scope $tcf_scope -overwrite
 run -time $run_time_write ; # the simulation will run until 2000ns
 dumptcf -end
 dumptcf -output $tcf_file_read -scope $tcf_scope -overwrite

 # Read Procedure
 run -time $run_time_read ; # the simulation will run until 4000ns
 dumptcf -end
 #simvision simcontrol run -time 4010 ; # the simulation will run until 1000ns
 #simvision database export -all -format vcd -name simvisionTcl.vcd -overwrite
 simvision exit
