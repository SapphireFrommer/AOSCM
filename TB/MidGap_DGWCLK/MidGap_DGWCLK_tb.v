`timescale 1ns/100ps
`define ADD 8
module MidGap_DGWCLK_tb;
	
    reg clk;
    reg [2**`ADDR_WIDTH-1:0] E;
    reg SE;

    wire [2**`ADDR_WIDTH-1:0] DGWClkLeftNet;
    wire [2**`ADDR_WIDTH-1:0] DGWClkRightNet;

	MidGap_DGWCLK UUT(.DGWClkLeftNet(DGWClkLeftNet), .DGWClkRightNet(DGWClkRightNet), .E(E), .SE(SE), .clk(clk));

	always #1 clk=~clk;

	initial
		begin
			clk=1'b0;
			
			$display("\t\ttime:\tclk\tE\t\tDGWClkLeftNet\tDGWClkRightNet");
			$monitor($time,":\t%b\t%b\t%b\t%b",clk,E,DGWClkLeftNet,DGWClkRightNet);
            

            #2
            E = 8'b0000_0001;
			#1
            E = 8'b0100_0000;

        	#1

			#4 $finish;			
		end
endmodule

