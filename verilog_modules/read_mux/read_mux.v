

module read_mux (DOUT, MemoryLatch, RWL);

    //ports
    output DOUT;
    input [15:0] MemoryLatch;
    input [15:0] RWL;

    //wires
    wire DOUT;
    wire [15:0] MemoryLatch;
    wire [15:0] RWL;
    wire [15:0] w0;
    wire [7:0] w1;
    wire [3:0] w2;
    wire [1:0] w3;
    wire [0:0] w4;

    //instances
    INV_X1B_A12TR inv_out(.A(w4[0]), .Y(DOUT));
    NAND2_X1A_A12TR level_1_0(.A(MemoryLatch[0]), .B(RWL[0]), .Y(w0[0]));
    NAND2_X1A_A12TR level_1_1(.A(MemoryLatch[1]), .B(RWL[1]), .Y(w0[1]));
    NAND2_X1A_A12TR level_1_10(.A(MemoryLatch[10]), .B(RWL[10]), .Y(w0[10]));
    NAND2_X1A_A12TR level_1_11(.A(MemoryLatch[11]), .B(RWL[11]), .Y(w0[11]));
    NAND2_X1A_A12TR level_1_12(.A(MemoryLatch[12]), .B(RWL[12]), .Y(w0[12]));
    NAND2_X1A_A12TR level_1_13(.A(MemoryLatch[13]), .B(RWL[13]), .Y(w0[13]));
    NAND2_X1A_A12TR level_1_14(.A(MemoryLatch[14]), .B(RWL[14]), .Y(w0[14]));
    NAND2_X1A_A12TR level_1_15(.A(MemoryLatch[15]), .B(RWL[15]), .Y(w0[15]));
    NAND2_X1A_A12TR level_1_2(.A(MemoryLatch[2]), .B(RWL[2]), .Y(w0[2]));
    NAND2_X1A_A12TR level_1_3(.A(MemoryLatch[3]), .B(RWL[3]), .Y(w0[3]));
    NAND2_X1A_A12TR level_1_4(.A(MemoryLatch[4]), .B(RWL[4]), .Y(w0[4]));
    NAND2_X1A_A12TR level_1_5(.A(MemoryLatch[5]), .B(RWL[5]), .Y(w0[5]));
    NAND2_X1A_A12TR level_1_6(.A(MemoryLatch[6]), .B(RWL[6]), .Y(w0[6]));
    NAND2_X1A_A12TR level_1_7(.A(MemoryLatch[7]), .B(RWL[7]), .Y(w0[7]));
    NAND2_X1A_A12TR level_1_8(.A(MemoryLatch[8]), .B(RWL[8]), .Y(w0[8]));
    NAND2_X1A_A12TR level_1_9(.A(MemoryLatch[9]), .B(RWL[9]), .Y(w0[9]));
    NAND2_X1A_A12TR level_2_0(.A(w0[0]), .B(w0[1]), .Y(w1[0]));
    NAND2_X1A_A12TR level_2_1(.A(w0[2]), .B(w0[3]), .Y(w1[1]));
    NAND2_X1A_A12TR level_2_2(.A(w0[4]), .B(w0[5]), .Y(w1[2]));
    NAND2_X1A_A12TR level_2_3(.A(w0[6]), .B(w0[7]), .Y(w1[3]));
    NAND2_X1A_A12TR level_2_4(.A(w0[8]), .B(w0[9]), .Y(w1[4]));
    NAND2_X1A_A12TR level_2_5(.A(w0[10]), .B(w0[11]), .Y(w1[5]));
    NAND2_X1A_A12TR level_2_6(.A(w0[12]), .B(w0[13]), .Y(w1[6]));
    NAND2_X1A_A12TR level_2_7(.A(w0[14]), .B(w0[15]), .Y(w1[7]));
    NOR2_X1A_A12TR level_3_0(.A(w1[0]), .B(w1[1]), .Y(w2[0]));
    NOR2_X1A_A12TR level_3_1(.A(w1[2]), .B(w1[3]), .Y(w2[1]));
    NOR2_X1A_A12TR level_3_2(.A(w1[4]), .B(w1[5]), .Y(w2[2]));
    NOR2_X1A_A12TR level_3_3(.A(w1[6]), .B(w1[7]), .Y(w2[3]));
    NAND2_X1A_A12TR level_4_0(.A(w2[0]), .B(w2[1]), .Y(w3[0]));
    NAND2_X1A_A12TR level_4_1(.A(w2[2]), .B(w2[3]), .Y(w3[1]));
    NOR2_X1A_A12TR level_5_0(.A(w3[0]), .B(w3[1]), .Y(w4[0]));

endmodule
