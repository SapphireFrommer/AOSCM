

module Decoder_4_16 (decoder_in, decoder_out);

	//ports
	input [3:0] decoder_in;
	output [15:0] decoder_out;

	//wires
	wire [3:0] decoder_in;
	wire [3:0] in_not;
	wire [15:0] decoder_out;

	//instances
	NAND4_X1A_A12TR NAND4_0(.A(in_not[0]), .B(in_not[1]), .C(in_not[2]), .D(in_not[3]), .Y(decoder_out[0]));
	NAND4_X1A_A12TR NAND4_1(.A(decoder_in[0]), .B(in_not[1]), .C(in_not[2]), .D(in_not[3]), .Y(decoder_out[1]));
	NAND4_X1A_A12TR NAND4_10(.A(in_not[0]), .B(decoder_in[1]), .C(in_not[2]), .D(decoder_in[3]), .Y(decoder_out[10]));
	NAND4_X1A_A12TR NAND4_11(.A(decoder_in[0]), .B(decoder_in[1]), .C(in_not[2]), .D(decoder_in[3]), .Y(decoder_out[11]));
	NAND4_X1A_A12TR NAND4_12(.A(in_not[0]), .B(in_not[1]), .C(decoder_in[2]), .D(decoder_in[3]), .Y(decoder_out[12]));
	NAND4_X1A_A12TR NAND4_13(.A(decoder_in[0]), .B(in_not[1]), .C(decoder_in[2]), .D(decoder_in[3]), .Y(decoder_out[13]));
	NAND4_X1A_A12TR NAND4_14(.A(in_not[0]), .B(decoder_in[1]), .C(decoder_in[2]), .D(decoder_in[3]), .Y(decoder_out[14]));
	NAND4_X1A_A12TR NAND4_15(.A(decoder_in[0]), .B(decoder_in[1]), .C(decoder_in[2]), .D(decoder_in[3]), .Y(decoder_out[15]));
	NAND4_X1A_A12TR NAND4_2(.A(in_not[0]), .B(decoder_in[1]), .C(in_not[2]), .D(in_not[3]), .Y(decoder_out[2]));
	NAND4_X1A_A12TR NAND4_3(.A(decoder_in[0]), .B(decoder_in[1]), .C(in_not[2]), .D(in_not[3]), .Y(decoder_out[3]));
	NAND4_X1A_A12TR NAND4_4(.A(in_not[0]), .B(in_not[1]), .C(decoder_in[2]), .D(in_not[3]), .Y(decoder_out[4]));
	NAND4_X1A_A12TR NAND4_5(.A(decoder_in[0]), .B(in_not[1]), .C(decoder_in[2]), .D(in_not[3]), .Y(decoder_out[5]));
	NAND4_X1A_A12TR NAND4_6(.A(in_not[0]), .B(decoder_in[1]), .C(decoder_in[2]), .D(in_not[3]), .Y(decoder_out[6]));
	NAND4_X1A_A12TR NAND4_7(.A(decoder_in[0]), .B(decoder_in[1]), .C(decoder_in[2]), .D(in_not[3]), .Y(decoder_out[7]));
	NAND4_X1A_A12TR NAND4_8(.A(in_not[0]), .B(in_not[1]), .C(in_not[2]), .D(decoder_in[3]), .Y(decoder_out[8]));
	NAND4_X1A_A12TR NAND4_9(.A(decoder_in[0]), .B(in_not[1]), .C(in_not[2]), .D(decoder_in[3]), .Y(decoder_out[9]));
	INV_X1B_A12TR in_0_not(.A(decoder_in[0]), .Y(in_not[0]));
	INV_X1B_A12TR in_1_not(.A(decoder_in[1]), .Y(in_not[1]));
	INV_X1B_A12TR in_2_not(.A(decoder_in[2]), .Y(in_not[2]));
	INV_X1B_A12TR in_3_not(.A(decoder_in[3]), .Y(in_not[3]));

endmodule
