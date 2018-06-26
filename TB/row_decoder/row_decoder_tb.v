`timescale 1ns/100ps 

module row_decoder_tb;
	//reg clk;
    reg [`ADDR_WIDTH-1:0] in;
    wire [2**`ADDR_WIDTH-1:0] out;
	integer i;

	row_decoder UUT(in, out);

	//always #1 clk=~clk;

	initial
		begin
			//clk=1'b0;
			
			$display("\t\ttime:\tin\tout");
			$monitor($time,":\t%b\t%b",in,out);
            
            in = `ADDR_WIDTH'd0;
            

			for (i=0; i<2**`ADDR_WIDTH; i=i+1) begin
				in = i;
				#1;
			end
			#4 $finish;			
		end
endmodule

