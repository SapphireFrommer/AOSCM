`timescale 1ns/100ps 

module scm65_tb;
    reg clk;
    reg WE;
    reg RE;
    reg [`ADDR_WIDTH-1:0] WADDR;
    reg [`ADDR_WIDTH-1:0] RADDR;
    reg [`DATA_WIDTH-1:0] DIN;
    wire [`DATA_WIDTH-1:0] DOUT;

	scm65 UUT(clk, DIN, DOUT, RADDR, RE, WADDR, WE);

	always #1 clk=~clk;

	initial
		begin
			clk=1'b0;
			
			$display("\t\ttime:\tclk\tDIN\t\t\tDOUT\t\t\tRADDR\tRE\tWADDR\tWE");
			$monitor($time,":\t%b\t%b\t%b\t%b\t%b\t%b\t%b",clk, DIN, DOUT, RADDR, RE, WADDR, WE);
            

            #2

			#1

        	#1

			#4 $finish;			
		end
endmodule

