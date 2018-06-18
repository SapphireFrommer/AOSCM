

module bitslice2 (DGWCLK, DIN, DOUT, RWL, clk);

	//ports
	input clk;
	input DIN;
	input [15:0] DGWCLK;
	output DOUT;
	input [15:0] RWL;

	//wires
	wire [15:0] MemoryLatch;
	wire GDIN;
	wire [15:0] RWL;
	wire clk;
	wire DIN;
	wire [15:0] DGWCLK;
	wire DOUT;

	//instances
	DFFQ_X2M_A12TR GDIN_reg(.CK(clk), .D(DIN), .Q(GDIN));
	LATQ_X1M_A12TR MemoryLatch_reg_0(.D(GDIN), .G(DGWCLK[0]), .Q(MemoryLatch[0]));
	LATQ_X1M_A12TR MemoryLatch_reg_1(.D(GDIN), .G(DGWCLK[1]), .Q(MemoryLatch[1]));
	LATQ_X1M_A12TR MemoryLatch_reg_10(.D(GDIN), .G(DGWCLK[10]), .Q(MemoryLatch[10]));
	LATQ_X1M_A12TR MemoryLatch_reg_11(.D(GDIN), .G(DGWCLK[11]), .Q(MemoryLatch[11]));
	LATQ_X1M_A12TR MemoryLatch_reg_12(.D(GDIN), .G(DGWCLK[12]), .Q(MemoryLatch[12]));
	LATQ_X1M_A12TR MemoryLatch_reg_13(.D(GDIN), .G(DGWCLK[13]), .Q(MemoryLatch[13]));
	LATQ_X1M_A12TR MemoryLatch_reg_14(.D(GDIN), .G(DGWCLK[14]), .Q(MemoryLatch[14]));
	LATQ_X1M_A12TR MemoryLatch_reg_15(.D(GDIN), .G(DGWCLK[15]), .Q(MemoryLatch[15]));
	LATQ_X1M_A12TR MemoryLatch_reg_2(.D(GDIN), .G(DGWCLK[2]), .Q(MemoryLatch[2]));
	LATQ_X1M_A12TR MemoryLatch_reg_3(.D(GDIN), .G(DGWCLK[3]), .Q(MemoryLatch[3]));
	LATQ_X1M_A12TR MemoryLatch_reg_4(.D(GDIN), .G(DGWCLK[4]), .Q(MemoryLatch[4]));
	LATQ_X1M_A12TR MemoryLatch_reg_5(.D(GDIN), .G(DGWCLK[5]), .Q(MemoryLatch[5]));
	LATQ_X1M_A12TR MemoryLatch_reg_6(.D(GDIN), .G(DGWCLK[6]), .Q(MemoryLatch[6]));
	LATQ_X1M_A12TR MemoryLatch_reg_7(.D(GDIN), .G(DGWCLK[7]), .Q(MemoryLatch[7]));
	LATQ_X1M_A12TR MemoryLatch_reg_8(.D(GDIN), .G(DGWCLK[8]), .Q(MemoryLatch[8]));
	LATQ_X1M_A12TR MemoryLatch_reg_9(.D(GDIN), .G(DGWCLK[9]), .Q(MemoryLatch[9]));
	read_mux read_mux(.DOUT(DOUT), .MemoryLatch({MemoryLatch[15:0]}), .RWL({RWL[15:0]}));

endmodule
