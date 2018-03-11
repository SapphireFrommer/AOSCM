`timescale 1ns/100ps 
`include "read_mux.v"
//`include "/data/tsmc/65LP/dig_libs/ARM_FEONLY/arm/tsmc/cln65lp/sc12_base_rvt/r0p0/verilog/sc12_cln65lp_base_rvt.v"

//`include "/data/tsmc/65LP/dig_libs/ARM_FEONLY/arm/tsmc/cln65lp/sc12_base_rvt/r0p0/verilog/sc12_cln65lp_base_rvt_udp.v"


module NAND2_X1A_A12TR (A, B, Y);
    input A,B;
    output Y;
    assign Y=!(A&B);
endmodule

module NOR2_X1A_A12TR (A, B, Y);
    input A,B;
    output Y;
    assign Y=!(A|B);
endmodule


module INV_X1B_A12TR (A, Y);
    input A;
    output Y;
    assign Y=!A;
endmodule


module read_mux_tb;
	//reg clk;
    reg rwl_0;
    reg rwl_1;
    reg rwl_2;
    reg rwl_3;
    reg in_0;
    reg in_1;
    reg in_2;
    reg in_3;

	wire DOUT;

	read_mux UUT(DOUT,in_0,in_1,in_2,in_3,rwl_0,rwl_1,rwl_2,rwl_3);

	//always #1 clk=~clk;

	initial
		begin
			//clk=1'b0;
			
			$display("\t\ttime:     in_0   in_1  in_2 in_3    rwl_0  rwl_1    rwl_2  rwl_3  DOUT");
			$monitor($time,":      %b      %b    %b      %b        %b      %b      %b      %b      %b",in_0,in_1,in_2,in_3,rwl_0,rwl_1,rwl_2,rwl_3,DOUT);
            
            rwl_0 = 1'b1;
            rwl_1 = 1'b0;
            rwl_2 = 1'b0;
            rwl_3 = 1'b0;
            in_0 = 1'b1;
            in_1 = 1'b1;
            in_2 = 1'b0;
            in_3 = 1'b1;

            #2
            rwl_0 = 1'b0;
            rwl_1 = 1'b1;
            rwl_2 = 1'b0;
            rwl_3 = 1'b0;
            
			#1
            rwl_0 = 1'b0;
            rwl_1 = 1'b0;
            rwl_2 = 1'b1;
            rwl_3 = 1'b0;
        
        	#1
            rwl_0 = 1'b0;
            rwl_1 = 1'b0;
            rwl_2 = 1'b0;
            rwl_3 = 1'b1;
			#4 $finish;			
		end
endmodule

