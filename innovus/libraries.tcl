set METAL_STACK 1p9m_6x2z
set IO_METAL_STACK 9lm

set TRACKS 9
set FE_OR_BE "FE"

set paths(PDK_ROOT) /data/tsmc/65LP/


if {$FE_OR_BE=="BE"} {
	set paths(ARM_ROOT) $paths(PDK_ROOT)/dig_libs/ARM_BE/arm/tsmc/cln65lp/
} elseif {$FE_OR_BE=="FE"} {
	set paths(ARM_ROOT) $paths(PDK_ROOT)/dig_libs/ARM_FEONLY/arm/tsmc/cln65lp/
}

set paths(TECHNOLOGY_FILES) $paths(ARM_ROOT)/arm_tech/r2p0
set tech_files(TECHNOLOGY_LEF) $paths(TECHNOLOGY_FILES)/lef/${METAL_STACK}/sc${TRACKS}_tech.lef
set tech_files(CAPTABLE_BC) $paths(TECHNOLOGY_FILES)/cadence_captable/${METAL_STACK}/rcbest.captbl
set tech_files(CAPTABLE_TC) $paths(TECHNOLOGY_FILES)/cadence_captable/${METAL_STACK}/typical.captbl
set tech_files(CAPTABLE_WC) $paths(TECHNOLOGY_FILES)/cadence_captable/${METAL_STACK}/rcworst.captbl
set tech_files(QRCTECH_FILE_BC) $paths(PDK_ROOT)/pdk/Assura/lvs_rcx/qrcTechFile
set tech_files(QRCTECH_FILE_TC) $paths(PDK_ROOT)/pdk/Assura/lvs_rcx/qrcTechFile
set tech_files(QRCTECH_FILE_WC) $paths(PDK_ROOT)/pdk/Assura/lvs_rcx/qrcTechFile
set tech_files(TEMPERATURE_BC) -40
set tech_files(TEMPERATURE_TC) 25
set tech_files(TEMPERATURE_WC) 125

set paths(STANDARD_CELLS_RVT) $paths(ARM_ROOT)/sc${TRACKS}_base_rvt/r0p0
set tech_files(STANDARD_CELL_SITE) sc${TRACKS}_cln65lp
set tech_files(STANDARD_CELL_VDD) VDD
set tech_files(STANDARD_CELL_GND) VSS
set tech_files(STANDARD_CELLS_RVT_LEF) $paths(STANDARD_CELLS_RVT)/lef/sc${TRACKS}_cln65lp_base_rvt.lef
set tech_files(STANDARD_CELLS_RVT_BC_LIB) $paths(STANDARD_CELLS_RVT)/lib/sc${TRACKS}_cln65lp_base_rvt_ff_typical_min_1p32v_m40c.lib
set tech_files(STANDARD_CELLS_RVT_WC_LIB) $paths(STANDARD_CELLS_RVT)/lib/sc${TRACKS}_cln65lp_base_rvt_ss_typical_max_0p90v_125c.lib
set tech_files(STANDARD_CELLS_RVT_TC_LIB) $paths(STANDARD_CELLS_RVT)/lib/sc${TRACKS}_cln65lp_base_rvt_tt_typical_max_1p00v_25c.lib
set tech_files(STANDARD_CELLS_RVT_VERILOG) $paths(STANDARD_CELLS_RVT)/verilog/sc${TRACKS}_cln65lp_base_rvt.v
set tech_files(STANDARD_CELLS_RVT_OA) $paths(STANDARD_CELLS_RVT)/oa
set tech_files(STANDARD_CELL_SUPPRESS_MESSAGES) "ENCLF-200 TECHLIB-436 TECHLIB-302 ENCLF-58 LEFPARS-2001 ENCTS-282 TECHLIB-1318"
set tech_files(STANDARD_CELL_SUPPRESS_MESSAGES_RC) "LBR-9 LBR-146 LBR-415"

#### IO Library
set tech_files(IO_NAME) tpdn65lpnv2od3


set paths(IO_dir) $paths(PDK_ROOT)/dig_libs/ARM/TSMCHOME_fe/digital
set paths(IO_libs) $paths(IO_dir)/Front_End/timing_power_noise/NLDM/$tech_files(IO_NAME)_200a
set paths(IO_lefs) $paths(IO_dir)/Back_End/lef/$tech_files(IO_NAME)_140b/mt/$IO_METAL_STACK/lef/

set tech_files(IO_WC_LIB) $paths(IO_libs)/$tech_files(IO_NAME)wc.lib
set tech_files(IO_TC_LIB) $paths(IO_libs)/$tech_files(IO_NAME)tc.lib
set tech_files(IO_BC_LIB) $paths(IO_libs)/$tech_files(IO_NAME)bc.lib
set tech_files(IO_VERILOG) $paths(IO_dir)/Front_End/verilog/tpdn65lpnv2od3_140b/$tech_files(IO_NAME).v 
set tech_files(IO_LEF) $paths(IO_lefs)/$tech_files(IO_NAME)_$IO_METAL_STACK.lef
#set tech_files(IO_LEF) /u/engguest/temanad/VLSI/mor1kx/workspace/tpdn65lpnv2od3_9lm.lef
set tech_files(IO_LEF) $paths(IO_lefs)/$tech_files(IO_NAME)_$IO_METAL_STACK.lef
set tech_files(IO_ANTENNA_LEF) $paths(IO_lefs)/antenna_$IO_METAL_STACK.lef
set tech_files(IO_FILLERS) "PFILLER20 PFILLER10 PFILLER5 PFILLER1 PFILLER05 PFILLER0005"
set tech_files(IO_SITE) sc${TRACKS}_cln65lp
set tech_files(IO_VDDCORE) VDD
set tech_files(IO_GNDCORE) VSS
set tech_files(IO_VDDIO) VDDPST
set tech_files(IO_GNDIO) VSS

set tech_files(layer_names) "M0 M1 M2 M3 M4 M5 M6 M7 M8 M9"
if {$design(FULLCHIP_OR_MACRO)=="MACRO"} {
	set tech_files(SDC_DRIVING_CELL) BUF_X11B_A${TRACKS}TR
	set tech_files(CCOPT_DRIVING_PIN) BUF_X11B_A${TRACKS}TR/Y
	set tech_files(SDC_LOAD_PIN) BUF_X11B_A${TRACKS}TR/A
} elseif {$design(FULLCHIP_OR_MACRO)=="FULLCHIP"} {
	set tech_files(SDC_DRIVING_CELL) PRUW0204CDG
	set tech_files(CCOPT_DRIVING_PIN) PRUW0204CDG/C
	set tech_files(SDC_LOAD_PIN) PRUW0204CDG/PAD
}
set tech_files(WELLTAP) WELLANTENNATIEPW2_A${TRACKS}TR
set tech_files(WELLTAP_RULE) 20.0
set tech_files(ENDCAPS) "ENDCAPTIE2_A${TRACKS}TR ENDCAPTIE2_A${TRACKS}TR"
set tech_files(CLOCK_BUFFERS) "BUF_X16M_A${TRACKS}TR BUF_X11M_A${TRACKS}TR BUF_X6M_A${TRACKS}TR BUF_X3M_A${TRACKS}TR"
set tech_files(CLOCK_INVERTERS) "INV_X9M_A${TRACKS}TR INV_X6M_A${TRACKS}TR INV_X3M_A${TRACKS}TR INV_X2M_A${TRACKS}TR"
set tech_files(CLOCK_GATES) "POSTICG_X9B_A${TRACKS}TR POSTICG_X6B_A${TRACKS}TR POSTICG_X4B_A${TRACKS}TR POSTICG_X1P4B_A${TRACKS}TR POSTICG_X1B_A${TRACKS}TR"
set tech_files(CLOCK_LOGIC) ""
set tech_files(CLOCK_DELAYS) ""

# ARM Memory Compiler
set tech_files(SRAM_VDDCORE_PIN) "VDDCE"
set tech_files(SRAM_VDDPERIPHERY_PIN) "VDDPE"
set tech_files(SRAM_GND_PIN) "VSSE"


#################################
# Technology SITE Definitions
################################
set tech(row_height) 2.4
set tech(grid_unit) 0.2
set tech(llx) 0
set tech(lly) 0


