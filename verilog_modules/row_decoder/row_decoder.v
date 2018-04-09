

module row_decoder (decoder_in, decoder_out);

    //ports
    input [3:0] decoder_in;
    output [15:0] decoder_out;

    //wires
    wire [3:0] decoder_in;
    wire [15:0] decoder_out;
    wire [7:0] PreDec_out;
    wire [15:0] nand_out;

    //instances
    INV_X1B_A12TR INV_out_0(.A(nand_out[0]), .Y(decoder_out[0]));
    INV_X1B_A12TR INV_out_1(.A(nand_out[1]), .Y(decoder_out[1]));
    INV_X1B_A12TR INV_out_10(.A(nand_out[10]), .Y(decoder_out[10]));
    INV_X1B_A12TR INV_out_11(.A(nand_out[11]), .Y(decoder_out[11]));
    INV_X1B_A12TR INV_out_12(.A(nand_out[12]), .Y(decoder_out[12]));
    INV_X1B_A12TR INV_out_13(.A(nand_out[13]), .Y(decoder_out[13]));
    INV_X1B_A12TR INV_out_14(.A(nand_out[14]), .Y(decoder_out[14]));
    INV_X1B_A12TR INV_out_15(.A(nand_out[15]), .Y(decoder_out[15]));
    INV_X1B_A12TR INV_out_2(.A(nand_out[2]), .Y(decoder_out[2]));
    INV_X1B_A12TR INV_out_3(.A(nand_out[3]), .Y(decoder_out[3]));
    INV_X1B_A12TR INV_out_4(.A(nand_out[4]), .Y(decoder_out[4]));
    INV_X1B_A12TR INV_out_5(.A(nand_out[5]), .Y(decoder_out[5]));
    INV_X1B_A12TR INV_out_6(.A(nand_out[6]), .Y(decoder_out[6]));
    INV_X1B_A12TR INV_out_7(.A(nand_out[7]), .Y(decoder_out[7]));
    INV_X1B_A12TR INV_out_8(.A(nand_out[8]), .Y(decoder_out[8]));
    INV_X1B_A12TR INV_out_9(.A(nand_out[9]), .Y(decoder_out[9]));
    NAND2_X1A_A12TR PostDec_0(.A(PreDec_out[4]), .B(PreDec_out[0]), .Y(nand_out[0]));
    NAND2_X1A_A12TR PostDec_1(.A(PreDec_out[4]), .B(PreDec_out[1]), .Y(nand_out[1]));
    NAND2_X1A_A12TR PostDec_10(.A(PreDec_out[6]), .B(PreDec_out[2]), .Y(nand_out[10]));
    NAND2_X1A_A12TR PostDec_11(.A(PreDec_out[6]), .B(PreDec_out[3]), .Y(nand_out[11]));
    NAND2_X1A_A12TR PostDec_12(.A(PreDec_out[7]), .B(PreDec_out[0]), .Y(nand_out[12]));
    NAND2_X1A_A12TR PostDec_13(.A(PreDec_out[7]), .B(PreDec_out[1]), .Y(nand_out[13]));
    NAND2_X1A_A12TR PostDec_14(.A(PreDec_out[7]), .B(PreDec_out[2]), .Y(nand_out[14]));
    NAND2_X1A_A12TR PostDec_15(.A(PreDec_out[7]), .B(PreDec_out[3]), .Y(nand_out[15]));
    NAND2_X1A_A12TR PostDec_2(.A(PreDec_out[4]), .B(PreDec_out[2]), .Y(nand_out[2]));
    NAND2_X1A_A12TR PostDec_3(.A(PreDec_out[4]), .B(PreDec_out[3]), .Y(nand_out[3]));
    NAND2_X1A_A12TR PostDec_4(.A(PreDec_out[5]), .B(PreDec_out[0]), .Y(nand_out[4]));
    NAND2_X1A_A12TR PostDec_5(.A(PreDec_out[5]), .B(PreDec_out[1]), .Y(nand_out[5]));
    NAND2_X1A_A12TR PostDec_6(.A(PreDec_out[5]), .B(PreDec_out[2]), .Y(nand_out[6]));
    NAND2_X1A_A12TR PostDec_7(.A(PreDec_out[5]), .B(PreDec_out[3]), .Y(nand_out[7]));
    NAND2_X1A_A12TR PostDec_8(.A(PreDec_out[6]), .B(PreDec_out[0]), .Y(nand_out[8]));
    NAND2_X1A_A12TR PostDec_9(.A(PreDec_out[6]), .B(PreDec_out[1]), .Y(nand_out[9]));
    Decoder_2_4 PreDec_0(.decoder_in({decoder_in[1:0]}), .decoder_out({PreDec_out[3:0]}));
    Decoder_2_4 PreDec_1(.decoder_in({decoder_in[3:2]}), .decoder_out({PreDec_out[7:4]}));

endmodule
