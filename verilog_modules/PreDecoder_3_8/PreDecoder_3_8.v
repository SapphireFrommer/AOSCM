

module PreDecoder_3_8 (decoder_in, decoder_out);

	//ports
	input [2:0] decoder_in;
	output [7:0] decoder_out;

	//wires
	wire [2:0] in_not;
	wire [2:0] decoder_in;
	wire [7:0] decoder_out;

	//instances
	NAND3_X1A_A12TR NAND3_0(.A(in_not[2]), .B(in_not[1]), .C(in_not[0]), .Y(decoder_out[0]));
	NAND3_X1A_A12TR NAND3_1(.A(in_not[2]), .B(in_not[1]), .C(decoder_in[0]), .Y(decoder_out[1]));
	NAND3_X1A_A12TR NAND3_2(.A(in_not[2]), .B(decoder_in[1]), .C(in_not[0]), .Y(decoder_out[2]));
	NAND3_X1A_A12TR NAND3_3(.A(in_not[2]), .B(decoder_in[1]), .C(decoder_in[0]), .Y(decoder_out[3]));
	NAND3_X1A_A12TR NAND3_4(.A(decoder_in[2]), .B(in_not[1]), .C(in_not[0]), .Y(decoder_out[4]));
	NAND3_X1A_A12TR NAND3_5(.A(decoder_in[2]), .B(in_not[1]), .C(decoder_in[0]), .Y(decoder_out[5]));
	NAND3_X1A_A12TR NAND3_6(.A(decoder_in[2]), .B(decoder_in[1]), .C(in_not[0]), .Y(decoder_out[6]));
	NAND3_X1A_A12TR NAND3_7(.A(decoder_in[2]), .B(decoder_in[1]), .C(decoder_in[0]), .Y(decoder_out[7]));
	INV_X1B_A12TR in_0_not(.A(decoder_in[0]), .Y(in_not[0]));
	INV_X1B_A12TR in_1_not(.A(decoder_in[1]), .Y(in_not[1]));
	INV_X1B_A12TR in_2_not(.A(decoder_in[2]), .Y(in_not[2]));

endmodule
