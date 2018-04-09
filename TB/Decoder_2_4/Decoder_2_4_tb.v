`timescale 1ns/100ps 

module Decoder_2_4_tb;
	//reg clk;
    reg [1:0] in;
    wire [3:0] out;


	Decoder_2_4 UUT(in, out);

	//always #1 clk=~clk;

	initial
		begin
			//clk=1'b0;
			
			$display("\t\ttime:\tin\tout");
			$monitor($time,":\t%b\t%b",in,out);
            
            in = 2'b00;
            #1
            in = 2'b01;
			#1
            in = 2'd10;
        	#1
            in = 2'b11;

			#4 $finish;			
		end
endmodule

