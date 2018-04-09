`timescale 1ns/100ps 

module row_decoder_tb;
	//reg clk;
    reg [3:0] in;
    wire [15:0] out;


	row_decoder UUT(in, out);

	//always #1 clk=~clk;

	initial
		begin
			//clk=1'b0;
			
			$display("\t\ttime:\tin\tout");
			$monitor($time,":\t%b\t%b",in,out);
            
            in = 4'd0;
            #1
            in = 4'd1;
            #1
            in = 4'd2;
            #1
            in = 4'd3;
            #1
            in = 4'd4;
            #1
            in = 4'd5;
            #1
            in = 4'd6;
            #1
            in = 4'd7;
            #1
            in = 4'd8;
            #1
            in = 4'd9;
            #1
            in = 4'd10;
            #1
            in = 4'd11;
            #1
            in = 4'd12;
            #1
            in = 4'd13;
            #1
            in = 4'd14;
            #1
            in = 4'd15;


			#4 $finish;			
		end
endmodule

