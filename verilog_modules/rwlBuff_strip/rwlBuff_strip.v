

module rwlBuff_strip (IN, OUT);

    //ports
    input [15:0] IN;
    output [15:0] OUT;

    //wires
    wire [15:0] IN;
    wire [15:0] OUT;

    //instances
    BUFH_X3M_A12TR rwlBuff_0(.A(IN[0]), .Y(OUT[0]));
    BUFH_X3M_A12TR rwlBuff_1(.A(IN[1]), .Y(OUT[1]));
    BUFH_X3M_A12TR rwlBuff_10(.A(IN[10]), .Y(OUT[10]));
    BUFH_X3M_A12TR rwlBuff_11(.A(IN[11]), .Y(OUT[11]));
    BUFH_X3M_A12TR rwlBuff_12(.A(IN[12]), .Y(OUT[12]));
    BUFH_X3M_A12TR rwlBuff_13(.A(IN[13]), .Y(OUT[13]));
    BUFH_X3M_A12TR rwlBuff_14(.A(IN[14]), .Y(OUT[14]));
    BUFH_X3M_A12TR rwlBuff_15(.A(IN[15]), .Y(OUT[15]));
    BUFH_X3M_A12TR rwlBuff_2(.A(IN[2]), .Y(OUT[2]));
    BUFH_X3M_A12TR rwlBuff_3(.A(IN[3]), .Y(OUT[3]));
    BUFH_X3M_A12TR rwlBuff_4(.A(IN[4]), .Y(OUT[4]));
    BUFH_X3M_A12TR rwlBuff_5(.A(IN[5]), .Y(OUT[5]));
    BUFH_X3M_A12TR rwlBuff_6(.A(IN[6]), .Y(OUT[6]));
    BUFH_X3M_A12TR rwlBuff_7(.A(IN[7]), .Y(OUT[7]));
    BUFH_X3M_A12TR rwlBuff_8(.A(IN[8]), .Y(OUT[8]));
    BUFH_X3M_A12TR rwlBuff_9(.A(IN[9]), .Y(OUT[9]));

endmodule
