`timescale 1ns/100ps 

module PreDecoder_4_16_tb;
	//reg clk;
    reg [3:0] in;
    wire [15:0] out;


	PreDecoder_4_16 UUT(in, out);

	//always #1 clk=~clk;

	initial
		begin
			//clk=1'b0;
			
			$display("\t\ttime:\tin\tout");
			$monitor($time,":\t%b\t%b",in,out);
            
            in = 4'b0000;
            #1
            in = 4'b0001;
			#1
            in = 4'b0010;
        	#1
            in = 4'b0011;
        	#1			
            in = 4'b0100;
            #1
            in = 4'b0101;
			#1
            in = 4'b0110;
        	#1
            in = 4'b0111;
            #1
            in = 4'b1000;
			#1
            in = 4'b1001;
        	#1
            in = 4'b1001;
        	#1
            in = 4'b1011;			
        	#1			
            in = 4'b1100;
            #1
            in = 4'b1101;
			#1
            in = 4'b1110;
        	#1
            in = 4'b1111;



			#4 $finish;			
		end
endmodule

