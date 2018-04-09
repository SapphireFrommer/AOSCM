
# NC-Sim Command File
# TOOL:	ncsim(64)	15.10-s014
#

set tcl_prompt1 {puts -nonewline "ncsim> "}
set tcl_prompt2 {puts -nonewline "> "}
set vlog_format %h
set vhdl_format %v
set real_precision 6
set display_unit auto
set time_unit module
set heap_garbage_size -200
set heap_garbage_time 0
set assert_report_level note
set assert_stop_level error
set autoscope yes
set assert_1164_warnings yes
set pack_assert_off {}
set severity_pack_assert_off {note warning}
set assert_output_stop_level failed
set tcl_debug_level 0
set relax_path_name 1
set vhdl_vcdmap XX01ZX01X
set intovf_severity_level ERROR
set probe_screen_format 0
set rangecnst_severity_level ERROR
set textio_severity_level ERROR
set vital_timing_checks_on 1
set vlog_code_show_force 0
set assert_count_attempts 1
set tcl_all64 false
set tcl_runerror_exit false
set assert_report_incompletes 0
set show_force 1
set force_reset_by_reinvoke 0
set tcl_relaxed_literal 0
set probe_exclude_patterns {}
set probe_packed_limit 4k
set probe_unpacked_limit 16k
set assert_internal_msg no
set svseed 1
set assert_reporting_mode 0
alias . run
alias iprof profile
alias quit exit
stop -create -name Randomize -randomize
database -open -shm -into waves.shm waves -default
probe -create -database waves tb_scm65.CLK tb_scm65.DIN tb_scm65.DOUT tb_scm65.RADDR tb_scm65.RADDR_old tb_scm65.RE tb_scm65.R_W tb_scm65.TBArray tb_scm65.WADDR tb_scm65.WE tb_scm65.correct tb_scm65.error tb_scm65.fo tb_scm65.row
probe -create -database waves tb_scm65.MEM.CLK tb_scm65.MEM.DGWCLKLeftNet tb_scm65.MEM.DGWClkRightNet tb_scm65.MEM.DIN tb_scm65.MEM.DOUT tb_scm65.MEM.GDINCLK tb_scm65.MEM.GRCLK tb_scm65.MEM.GWCLK tb_scm65.MEM.RADDR tb_scm65.MEM.RE tb_scm65.MEM.SE tb_scm65.MEM.WADDR tb_scm65.MEM.WE tb_scm65.MEM.decoder_read_out tb_scm65.MEM.decoder_write_out tb_scm65.MEM.rwlBuffNet_0 tb_scm65.MEM.rwlBuffNet_1 tb_scm65.MEM.rwlBuffNet_2 tb_scm65.MEM.rwlBuffNet_3
probe -create -database waves tb_scm65.MEM.bitslice_1.DGWCLK tb_scm65.MEM.bitslice_1.DIN tb_scm65.MEM.bitslice_1.DOUT tb_scm65.MEM.bitslice_1.GDIN tb_scm65.MEM.bitslice_1.MemoryLatch tb_scm65.MEM.bitslice_1.RWL tb_scm65.MEM.bitslice_1.clk

simvision -input /project/test_project/users/marinbh/ws/scm_compiler/TB/scm65/.simvision/21323_marinbh_enicsw03_autosave.tcl.svcf
