`timescale 1ns/100ps 

module PreDecoder_3_8_tb;
	//reg clk;
    reg [2:0] in;
    wire [7:0] out;


	PreDecoder_3_8 UUT(in, out);

	//always #1 clk=~clk;

	initial
		begin
			//clk=1'b0;
			
			$display("\t\ttime:\tin\tout");
			$monitor($time,":\t%b\t%b",in,out);
            
            in = 3'b000;
            #1
            in = 3'b001;
			#1
            in = 3'b010;
        	#1
            in = 3'b011;
        	#1
            in = 3'b100;
            #1
            in = 3'b101;
			#1
            in = 3'b110;
        	#1
            in = 3'b111;

			#4 $finish;			
		end
endmodule

