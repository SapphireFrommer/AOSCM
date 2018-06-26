`timescale 1ns/100ps 

module read_mux_tb;
	//reg clk;
    reg [3:0] rwl;
    reg [3:0] in;

	wire DOUT;

	read_mux UUT(DOUT, in, rwl);

	//always #1 clk=~clk;

	initial
		begin
			//clk=1'b0;
			
			$display("\t\ttime:     in      rwl     DOUT");
			$monitor($time,":   %b      %b    %b  ",in,rwl,DOUT);
            
            rwl = 4'b0001;
            in = 4'b1011;

            #2
            rwl = 4'b0010;

			#1
            rwl = 4'd0100;

        	#1
            rwl = 4'b1000;

			#4 $finish;			
		end
endmodule

