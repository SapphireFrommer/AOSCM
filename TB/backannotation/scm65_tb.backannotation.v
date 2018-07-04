//////////////////////////////////
///   test_bench of scm65.v    ///
//////////////////////////////////
`timescale 1ns/1ps

`define TCLK 10
`define HALF_CYCLE (`TCLK/2)
`define NUM_ROWS  (2**`ADDR_WIDTH)

`define WRITING_TIME (`NUM_ROWS>100 ? `TCLK*(`NUM_ROWS*2) : `TCLK*(`NUM_ROWS+100))
`define FINAL_READING_TIME (`WRITING_TIME+1000)
`define SIMULATION_TIME (`FINAL_READING_TIME+1000)


`ifdef GATE_LEVEL 
    `include "../../export/synthesis/scm65.postsyn.v"
`endif

module tb_scm65;


//------ TB wires and registers ------// 
    reg CLK,RE,WE,SE;
    reg [`ADDR_WIDTH-1:0] WADDR;
    reg [`ADDR_WIDTH-1:0] RADDR;
    reg [`ADDR_WIDTH-1:0] RADDR_old;
    reg [`DATA_WIDTH-1:0] DIN;
    wire [`DATA_WIDTH-1:0] DOUT;
    reg [`DATA_WIDTH-1:0] TBArray [`NUM_ROWS-1:0];


//------ Integers --------//
    integer fo,row,R_W,error,correct;

//------ Memory instantiation --------//
    scm65 MEM (CLK, DIN, DOUT, RADDR, RE, SE, WADDR, WE);

//------ SDF file --------//
 initial
    begin 
	  $sdf_annotate(`SDF_FILE, `SDF_SCOPE,,"sdf_logfile.log" ,"MAXIMUM");
    
    end

//------ Output file --------//
    initial
        begin
            fo=$fopen("output_Report_GATE_LEVEL.txt","w"); 
            $fwrite(fo, "GATE_LEVEL Output Report:\t\t  \n\n");
        end


//------ Clock --------//
    always 
        #`HALF_CYCLE CLK = ~CLK;

//------ Initial State --------//
    initial 
        begin
            #0
            error = 0;
            correct = 0;
            row = 0;
            CLK = 0;
            SE=0;
            WADDR = `ADDR_WIDTH'b0;
            //DIN [31:0]	=$urandom_range(2**(`DATA_WIDTH/2)-1,0);
            //DIN [63:32]	=$urandom_range(2**(`DATA_WIDTH/2)-1,0);
            std::randomize(DIN);	
            WE = 0;
            R_W=0;
        end // #0

//------ Stimuli Application --------//  
    always @(negedge CLK)
        begin
            //------ Write to all Rows sequentially --------//  
            if(row < `NUM_ROWS)
                begin 
                    //DIN [31:0]	=$urandom_range(2**(`DATA_WIDTH/2)-1,0);
                    //DIN [63:32]	=$urandom_range(2**(`DATA_WIDTH/2)-1,0);	
                    std::randomize(DIN);

                    WADDR = row;
                    row = row +1;
                    WE = 1 ; // Write
                    RE = 0 ;
                    R_W = 1; // Write
                end   // row<NUM_ROWS

        //------ After finishing writing to all rows --------//  
            else if (row >= `NUM_ROWS ) 
                begin
                //------ Continue to write randomly until WRITING_TIME --------//  
                    if ($time < `WRITING_TIME)
                        begin
                            R_W = 1;     // 0 for reading , 1 for writing , 2 for leakage
                            //DIN [31:0]	=$urandom_range(2**(`DATA_WIDTH/2)-1,0);
                            //DIN [63:32]	=$urandom_range(2**(`DATA_WIDTH/2)-1,0);
                            std::randomize(DIN);
                        end // time<WRITING_TIME

                    else if (($time >= `WRITING_TIME) && ($time < `FINAL_READING_TIME))
                        begin
                            R_W = 0;
                        end // WRITING_TIME<time<FINAL_READING_TIME
                    else 
                        begin
                            R_W = 2;
                        end // time>FINAL_READING_TIME

                //------ We still havent reached t=WRITING_TIME so write --------//  
                    if (R_W == 1) 
                        begin
                            WADDR = $urandom_range(2**(`ADDR_WIDTH)-1,0);
                            WE = 1;
                            RE = 0;  
                        end // R_W == 1

                //------ Now read random addresses --------//  
                    if (R_W == 0) 
                        begin
                            RADDR = $urandom_range(2**(`ADDR_WIDTH)-1,0);
                            WE = 0;
                            RE = 1;  
                        end // R_W == 0

                //------ Now don't do any operation --------//  
                    if (R_W == 2) 
                        begin
                            WE = 0;
                            RE = 0;  
                        end // R_W == 2

                end // rows>NUM_ROWS
        end //always@(posedge clk)


//------ Verify that the correct data is written and read out. --------//  
    always @(posedge CLK)
        begin
            
            //------ If the previous action was to write, then record the data in TBArray --------//  
            if(R_W == 1)
                begin
                    #1 TBArray [WADDR] <= DIN;
                end // R_W==1

            //------ After filling up the array, check if the readouts correspond to the expected value --------//  
            if (row >= `NUM_ROWS)
                begin
                    if (RE == 1 ) 
                        begin
                            #(0.9*`TCLK)
                            RADDR_old = RADDR;               
                            if (TBArray[RADDR_old] != DOUT)
                                begin
                                    $fwrite(fo, "ERROR!!!\t\t\t TBArray value is=%h\t DOUT value is=%h\t of RADDR = %d\t time is %d\n",TBArray[RADDR_old],DOUT,RADDR_old, $time);
                                    error = error+1;
                                end // TBArray[RADDR] != DOUT
                            else 
                                begin
                                    $fwrite(fo, "Correct reading!\t TBArray value is=%h\t DOUT value is=%h\t of RADDR = %d\t time is %d\n",TBArray[RADDR_old],DOUT,RADDR_old, $time); 
                                    correct = correct+1;
                        end
                end //RE==1
            end//row>num_rows
        end //always @(posedge CLK)

    initial
        begin
            #`SIMULATION_TIME
            $fwrite(fo, "\n\n\t\t\t\tERROR =%d\t Correct=%d\t time is %d\n",error,correct,$time); 
            if (error == 0)
                $fwrite(fo, "\n\t\t\t\t\t\t\t\t\t +++++  SEEMS GOOD!  +++++\n");
            else
                $fwrite(fo, "\n\t\t\t\t\t\t\t\t\t +++++  SEEMS BAD!  +++++\n");        
            $fclose(fo);

            #10
            $finish;			
        end // Close output file


endmodule    


