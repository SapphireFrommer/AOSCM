
module read_mux (DOUT, MemoryLatch_0, MemoryLatch_1, MemoryLatch_2, MemoryLatch_3, RWL_0, RWL_1, RWL_2, RWL_3);

	//ports
	output DOUT;
	input MemoryLatch_0;
	input MemoryLatch_1;
	input MemoryLatch_2;
	input MemoryLatch_3;
	input RWL_0;
	input RWL_1;
	input RWL_2;
	input RWL_3;

	//instances
	INV_X1B_A12TR inv_out(.A(w20), .Y(DOUT));
	NAND2_X1A_A12TR level_1_0(.A(MemoryLatch_0), .B(RWL_0), .Y(w00));
	NAND2_X1A_A12TR level_1_1(.A(MemoryLatch_1), .B(RWL_1), .Y(w01));
	NAND2_X1A_A12TR level_1_2(.A(MemoryLatch_2), .B(RWL_2), .Y(w02));
	NAND2_X1A_A12TR level_1_3(.A(MemoryLatch_3), .B(RWL_3), .Y(w03));
	NAND2_X1A_A12TR level_2_0(.A(w00), .B(w01), .Y(w10));
	NAND2_X1A_A12TR level_2_1(.A(w02), .B(w03), .Y(w11));
	NOR2_X1A_A12TR level_3_0(.A(w10), .B(w11), .Y(w20));

endmodule
