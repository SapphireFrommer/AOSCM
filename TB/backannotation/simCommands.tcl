# This script opens the waveform with all the signals and 
#   start the simulation until 1000ns and thne exports a pair of tcf files
#              read.tcf, write.tcf
#   execute this script with the command: simvision -input simCommands.tcl 

set tb_name tb_scm65
set dut_name MEM
set tcf_scope "$tb_name.$dut_name"
#set tcf_scope "$tb_name"
simvision set tcf_scope "$tb_name.$dut_name"
#simvision set tcf_scope "$tb_name"
set tcf_file_write "../../export/write.tcf"
set tcf_file_read  "../../export/read.tcf"
set vcd_file  "../../export/$tb_name.vcd"
set period 10
set number_of_writes 116
set number_of_reads 100
set run_time_write [expr 1+$number_of_writes * $period]
set run_time_read  [expr $number_of_reads * $period]
set total_run_time [expr $run_time_write + $run_time_read]

 set w [simvision waveform new]
 #simvision scope set $tcf_scope
 simvision scope set $tb_name
 simvision waveform add -using "Waveform 1" -signals $tcf_scope -depth 2
 database -open $vcd_file -vcd  
 probe  -create $dut_name -vcd -depth 9 -all -database $vcd_file
 simvision simcontrol run -time 1
 
 # Write Procedure
  #     dumptcf [-dumpwireasnet] [-flatformat] [-inctoggle] [-internal]
  #               [-output filename] [-overwrite] [-scope scope_identifier] [-verbose]  #    -flatformat  -- makes flat output rather than hierarchical
 dumptcf -output $tcf_file_write -scope $tcf_scope -overwrite -verbose
 run -time $run_time_write ; # the simulation will run until 1160ns
 dumptcf -end

 # Read Procedure
 dumptcf -output $tcf_file_read -scope $tcf_scope -overwrite -verbose
 run -time $run_time_read ; # the simulation will run until 2160ns
 dumptcf -end
 #probe -save $vcd_file
# reset
# probe -create $dut_name -vcd -depth 2 -all -save $vcd_file
# simvision simcontrol run -time $total_run_time ; # the simulation will run until 2160ns
# simvision database export -all -format vcd -name $vcd_file -depth 5 -overwrite
 simvision exit
