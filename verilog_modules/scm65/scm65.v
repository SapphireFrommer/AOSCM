

module scm65 (CLK, DIN, DOUT, RADDR, RE, WADDR, WE);

    //ports
    input CLK;
    input WE;
    input RE;
    input [3:0] WADDR;
    input [3:0] RADDR;
    input [15:0] DIN;
    output [15:0] DOUT;

    //wires
    wire CLK;
    wire WE;
    wire RE;
    wire [3:0] WADDR;
    wire [3:0] RADDR;
    wire [15:0] DIN;
    wire [15:0] DOUT;
    wire SE;
    wire GDINCLK;
    wire GWCLK;
    wire GRCLK;
    wire [15:0] decoder_write_out;
    wire [15:0] DGWCLKLeftNet;
    wire [15:0] DGWClkRightNet;
    wire [15:0] rwlBuffNet_0;
    wire [15:0] rwlBuffNet_1;
    wire [15:0] decoder_read_out;
    wire [15:0] rwlBuffNet_2;
    wire [15:0] rwlBuffNet_3;

    //instances
    PREICG_X0P5B_A12TR GDINCLK_gate(.CK(CLK), .E(WE), .ECK(GDINCLK), .SE(SE));
    PREICG_X0P5B_A12TR GRCLK_gate(.CK(CLK), .E(RE), .ECK(GRCLK), .SE(SE));
    PREICG_X0P5B_A12TR GWCLK_gate(.CK(CLK), .E(WE), .ECK(GWCLK), .SE(SE));
    MidGap_DGWCLK MidGap_DGWCLK(.DGWClkLeftNet({DGWCLKLeftNet[15:0]}), .DGWClkRightNet({DGWClkRightNet[15:0]}), .E({decoder_write_out[15:0]}), .SE(), .clk(GWCLK));
    bitslice bitslice_0(.DGWCLK({DGWCLKLeftNet[15:0]}), .DIN(DIN[0]), .DOUT(DOUT[0]), .RWL({rwlBuffNet_0[15:0]}), .clk(GDINCLK));
    bitslice bitslice_1(.DGWCLK({DGWCLKLeftNet[15:0]}), .DIN(DIN[1]), .DOUT(DOUT[1]), .RWL({rwlBuffNet_0[15:0]}), .clk(GDINCLK));
    bitslice bitslice_10(.DGWCLK({DGWClkRightNet[15:0]}), .DIN(DIN[10]), .DOUT(DOUT[10]), .RWL({rwlBuffNet_2[15:0]}), .clk(GDINCLK));
    bitslice bitslice_11(.DGWCLK({DGWClkRightNet[15:0]}), .DIN(DIN[11]), .DOUT(DOUT[11]), .RWL({rwlBuffNet_2[15:0]}), .clk(GDINCLK));
    bitslice bitslice_12(.DGWCLK({DGWClkRightNet[15:0]}), .DIN(DIN[12]), .DOUT(DOUT[12]), .RWL({rwlBuffNet_3[15:0]}), .clk(GDINCLK));
    bitslice bitslice_13(.DGWCLK({DGWClkRightNet[15:0]}), .DIN(DIN[13]), .DOUT(DOUT[13]), .RWL({rwlBuffNet_3[15:0]}), .clk(GDINCLK));
    bitslice bitslice_14(.DGWCLK({DGWClkRightNet[15:0]}), .DIN(DIN[14]), .DOUT(DOUT[14]), .RWL({rwlBuffNet_3[15:0]}), .clk(GDINCLK));
    bitslice bitslice_15(.DGWCLK({DGWClkRightNet[15:0]}), .DIN(DIN[15]), .DOUT(DOUT[15]), .RWL({rwlBuffNet_3[15:0]}), .clk(GDINCLK));
    bitslice bitslice_2(.DGWCLK({DGWCLKLeftNet[15:0]}), .DIN(DIN[2]), .DOUT(DOUT[2]), .RWL({rwlBuffNet_0[15:0]}), .clk(GDINCLK));
    bitslice bitslice_3(.DGWCLK({DGWCLKLeftNet[15:0]}), .DIN(DIN[3]), .DOUT(DOUT[3]), .RWL({rwlBuffNet_0[15:0]}), .clk(GDINCLK));
    bitslice bitslice_4(.DGWCLK({DGWCLKLeftNet[15:0]}), .DIN(DIN[4]), .DOUT(DOUT[4]), .RWL({rwlBuffNet_1[15:0]}), .clk(GDINCLK));
    bitslice bitslice_5(.DGWCLK({DGWCLKLeftNet[15:0]}), .DIN(DIN[5]), .DOUT(DOUT[5]), .RWL({rwlBuffNet_1[15:0]}), .clk(GDINCLK));
    bitslice bitslice_6(.DGWCLK({DGWCLKLeftNet[15:0]}), .DIN(DIN[6]), .DOUT(DOUT[6]), .RWL({rwlBuffNet_1[15:0]}), .clk(GDINCLK));
    bitslice bitslice_7(.DGWCLK({DGWCLKLeftNet[15:0]}), .DIN(DIN[7]), .DOUT(DOUT[7]), .RWL({rwlBuffNet_1[15:0]}), .clk(GDINCLK));
    bitslice bitslice_8(.DGWCLK({DGWClkRightNet[15:0]}), .DIN(DIN[8]), .DOUT(DOUT[8]), .RWL({rwlBuffNet_2[15:0]}), .clk(GDINCLK));
    bitslice bitslice_9(.DGWCLK({DGWClkRightNet[15:0]}), .DIN(DIN[9]), .DOUT(DOUT[9]), .RWL({rwlBuffNet_2[15:0]}), .clk(GDINCLK));
    row_decoder read_decoder(.decoder_in({RADDR[3:0]}), .decoder_out({decoder_read_out[15:0]}));
    rwlBuff_strip rwlBuff_strip_0(.IN({rwlBuffNet_1[15:0]}), .OUT({rwlBuffNet_0[15:0]}));
    rwlBuff_strip rwlBuff_strip_1(.IN({decoder_read_out[15:0]}), .OUT({rwlBuffNet_1[15:0]}));
    rwlBuff_strip rwlBuff_strip_2(.IN({decoder_read_out[15:0]}), .OUT({rwlBuffNet_2[15:0]}));
    rwlBuff_strip rwlBuff_strip_3(.IN({rwlBuffNet_2[15:0]}), .OUT({rwlBuffNet_3[15:0]}));
    welltap_strip welltap_strip_0();
    welltap_strip welltap_strip_1();
    row_decoder write_decoder(.decoder_in({WADDR[3:0]}), .decoder_out({decoder_write_out[15:0]}));

endmodule
