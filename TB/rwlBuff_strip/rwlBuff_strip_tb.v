`timescale 1ns/100ps

module rwlBuff_strip_tb;
	//reg clk;
    reg [2**`ADDR_WIDTH-1:0] in;
    wire [2**`ADDR_WIDTH-1:0] out;

	rwlBuff_strip UUT(.IN(in), .OUT(out));

	//always #1 Clk=~Clk;

	initial
		begin
			$display("\t\ttime:\tIN\t\tOUT");
			$monitor($time,":\t%b\t%b",in,out);
            
            in = 8'b0000_0001;
            #2
            in = 8'b0100_0001;

			#2
            in = 8'b0110_0001;

        	#1
            in = 8'b1001_0010;

			#4 $finish;			
		end
endmodule

