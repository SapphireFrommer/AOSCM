`timescale 1ns/100ps 

module row_decoder_tb;
	//reg clk;
    reg [4:0] in;
    wire [31:0] out;
	integer i;

	row_decoder UUT(in, out);

	//always #1 clk=~clk;

	initial
		begin
			//clk=1'b0;
			
			$display("\t\ttime:\tin\tout");
			$monitor($time,":\t%b\t%b",in,out);
            
            in = 5'd0;
            

			for (i=0; i<32; i=i+1) begin
				#1 in = i;
				
			end
			#4 $finish;			
		end
endmodule

