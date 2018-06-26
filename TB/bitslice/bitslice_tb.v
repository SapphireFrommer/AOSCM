`timescale 1ns/100ps

module bitslice_tb;
	//reg clk;
    reg [2**`ADDR_WIDTH-1:0] DGWCLK;
    reg [2**`ADDR_WIDTH-1:0] RWL;
    reg Din;
    reg Clk;


	wire DOUT;

	bitslice UUT(.DGWCLK(DGWCLK), .DIN(Din), .DOUT(DOUT), .RWL(RWL), .clk(Clk));

	always #1 Clk=~Clk;

	initial
		begin
			Clk=1'b0;
			
			$display("\t\ttime:\tclk\tDIN\tDGWCLK\t\tRWL\t\tDOUT");
			$monitor($time,":\t%b\t%b\t%b\t%b\t%b",Clk,Din,DGWCLK,RWL,DOUT);
            
            Din = 1'b0;             // data to write
            DGWCLK = 8'b00000001;   // cell to write 
            RWL = 8'b00000001;      // cell to read
            #2
            Din = 1'b1;             // data to write
            DGWCLK = 8'b00000010;   // cell to write 
            RWL = 8'b00000001;      // cell to read

			#2
            RWL = 8'b00000010;      // cell to read

        	#1

			#4 $finish;			
		end
endmodule

