

module MidGap_DGWCLK (DGWClkLeftNet, DGWClkRightNet, E, SE, clk);

    //ports
    input clk;
    input SE;
    input [15:0] E;
    output [15:0] DGWClkLeftNet;
    output [15:0] DGWClkRightNet;

    //wires
    wire clk;
    wire SE;
    wire [15:0] E;
    wire [15:0] DGWClkLeftNet;
    wire [15:0] DGWClkRightNet;
    wire [15:0] ECK;

    //instances
    PREICG_X0P5B_A12TR DGWCLK_gate_0(.CK(clk), .E(E[0]), .ECK(ECK[0]), .SE());
    PREICG_X0P5B_A12TR DGWCLK_gate_1(.CK(clk), .E(E[1]), .ECK(ECK[1]), .SE());
    PREICG_X0P5B_A12TR DGWCLK_gate_10(.CK(clk), .E(E[10]), .ECK(ECK[10]), .SE());
    PREICG_X0P5B_A12TR DGWCLK_gate_11(.CK(clk), .E(E[11]), .ECK(ECK[11]), .SE());
    PREICG_X0P5B_A12TR DGWCLK_gate_12(.CK(clk), .E(E[12]), .ECK(ECK[12]), .SE());
    PREICG_X0P5B_A12TR DGWCLK_gate_13(.CK(clk), .E(E[13]), .ECK(ECK[13]), .SE());
    PREICG_X0P5B_A12TR DGWCLK_gate_14(.CK(clk), .E(E[14]), .ECK(ECK[14]), .SE());
    PREICG_X0P5B_A12TR DGWCLK_gate_15(.CK(clk), .E(E[15]), .ECK(ECK[15]), .SE());
    PREICG_X0P5B_A12TR DGWCLK_gate_2(.CK(clk), .E(E[2]), .ECK(ECK[2]), .SE());
    PREICG_X0P5B_A12TR DGWCLK_gate_3(.CK(clk), .E(E[3]), .ECK(ECK[3]), .SE());
    PREICG_X0P5B_A12TR DGWCLK_gate_4(.CK(clk), .E(E[4]), .ECK(ECK[4]), .SE());
    PREICG_X0P5B_A12TR DGWCLK_gate_5(.CK(clk), .E(E[5]), .ECK(ECK[5]), .SE());
    PREICG_X0P5B_A12TR DGWCLK_gate_6(.CK(clk), .E(E[6]), .ECK(ECK[6]), .SE());
    PREICG_X0P5B_A12TR DGWCLK_gate_7(.CK(clk), .E(E[7]), .ECK(ECK[7]), .SE());
    PREICG_X0P5B_A12TR DGWCLK_gate_8(.CK(clk), .E(E[8]), .ECK(ECK[8]), .SE());
    PREICG_X0P5B_A12TR DGWCLK_gate_9(.CK(clk), .E(E[9]), .ECK(ECK[9]), .SE());
    BUFH_X3M_A12TR DGWClkLeftBuff_0(.A(ECK[0]), .Y(DGWClkLeftNet[0]));
    BUFH_X3M_A12TR DGWClkLeftBuff_1(.A(ECK[1]), .Y(DGWClkLeftNet[1]));
    BUFH_X3M_A12TR DGWClkLeftBuff_10(.A(ECK[10]), .Y(DGWClkLeftNet[10]));
    BUFH_X3M_A12TR DGWClkLeftBuff_11(.A(ECK[11]), .Y(DGWClkLeftNet[11]));
    BUFH_X3M_A12TR DGWClkLeftBuff_12(.A(ECK[12]), .Y(DGWClkLeftNet[12]));
    BUFH_X3M_A12TR DGWClkLeftBuff_13(.A(ECK[13]), .Y(DGWClkLeftNet[13]));
    BUFH_X3M_A12TR DGWClkLeftBuff_14(.A(ECK[14]), .Y(DGWClkLeftNet[14]));
    BUFH_X3M_A12TR DGWClkLeftBuff_15(.A(ECK[15]), .Y(DGWClkLeftNet[15]));
    BUFH_X3M_A12TR DGWClkLeftBuff_2(.A(ECK[2]), .Y(DGWClkLeftNet[2]));
    BUFH_X3M_A12TR DGWClkLeftBuff_3(.A(ECK[3]), .Y(DGWClkLeftNet[3]));
    BUFH_X3M_A12TR DGWClkLeftBuff_4(.A(ECK[4]), .Y(DGWClkLeftNet[4]));
    BUFH_X3M_A12TR DGWClkLeftBuff_5(.A(ECK[5]), .Y(DGWClkLeftNet[5]));
    BUFH_X3M_A12TR DGWClkLeftBuff_6(.A(ECK[6]), .Y(DGWClkLeftNet[6]));
    BUFH_X3M_A12TR DGWClkLeftBuff_7(.A(ECK[7]), .Y(DGWClkLeftNet[7]));
    BUFH_X3M_A12TR DGWClkLeftBuff_8(.A(ECK[8]), .Y(DGWClkLeftNet[8]));
    BUFH_X3M_A12TR DGWClkLeftBuff_9(.A(ECK[9]), .Y(DGWClkLeftNet[9]));
    BUFH_X3M_A12TR DGWClkRightBuff_0(.A(ECK[0]), .Y(DGWClkRightNet[0]));
    BUFH_X3M_A12TR DGWClkRightBuff_1(.A(ECK[1]), .Y(DGWClkRightNet[1]));
    BUFH_X3M_A12TR DGWClkRightBuff_10(.A(ECK[10]), .Y(DGWClkRightNet[10]));
    BUFH_X3M_A12TR DGWClkRightBuff_11(.A(ECK[11]), .Y(DGWClkRightNet[11]));
    BUFH_X3M_A12TR DGWClkRightBuff_12(.A(ECK[12]), .Y(DGWClkRightNet[12]));
    BUFH_X3M_A12TR DGWClkRightBuff_13(.A(ECK[13]), .Y(DGWClkRightNet[13]));
    BUFH_X3M_A12TR DGWClkRightBuff_14(.A(ECK[14]), .Y(DGWClkRightNet[14]));
    BUFH_X3M_A12TR DGWClkRightBuff_15(.A(ECK[15]), .Y(DGWClkRightNet[15]));
    BUFH_X3M_A12TR DGWClkRightBuff_2(.A(ECK[2]), .Y(DGWClkRightNet[2]));
    BUFH_X3M_A12TR DGWClkRightBuff_3(.A(ECK[3]), .Y(DGWClkRightNet[3]));
    BUFH_X3M_A12TR DGWClkRightBuff_4(.A(ECK[4]), .Y(DGWClkRightNet[4]));
    BUFH_X3M_A12TR DGWClkRightBuff_5(.A(ECK[5]), .Y(DGWClkRightNet[5]));
    BUFH_X3M_A12TR DGWClkRightBuff_6(.A(ECK[6]), .Y(DGWClkRightNet[6]));
    BUFH_X3M_A12TR DGWClkRightBuff_7(.A(ECK[7]), .Y(DGWClkRightNet[7]));
    BUFH_X3M_A12TR DGWClkRightBuff_8(.A(ECK[8]), .Y(DGWClkRightNet[8]));
    BUFH_X3M_A12TR DGWClkRightBuff_9(.A(ECK[9]), .Y(DGWClkRightNet[9]));

endmodule
