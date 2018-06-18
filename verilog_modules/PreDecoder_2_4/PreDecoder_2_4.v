

module PreDecoder_2_4 (decoder_in, decoder_out);

	//ports
	output [3:0] decoder_out;
	input [1:0] decoder_in;

	//wires
	wire [1:0] in_not;
	wire [3:0] decoder_out;
	wire [1:0] decoder_in;

	//instances
	NAND2_X1A_A12TR NAND2_0(.A(in_not[1]), .B(in_not[0]), .Y(decoder_out[0]));
	NAND2_X1A_A12TR NAND2_1(.A(in_not[1]), .B(decoder_in[0]), .Y(decoder_out[1]));
	NAND2_X1A_A12TR NAND2_2(.A(decoder_in[1]), .B(in_not[0]), .Y(decoder_out[2]));
	NAND2_X1A_A12TR NAND2_3(.A(decoder_in[1]), .B(decoder_in[0]), .Y(decoder_out[3]));
	INV_X1B_A12TR in_0_not(.A(decoder_in[0]), .Y(in_not[0]));
	INV_X1B_A12TR in_1_not(.A(decoder_in[1]), .Y(in_not[1]));

endmodule
