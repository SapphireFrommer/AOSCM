import os, fileinput, datetime, math

#MY_VNC = 30
MY_VNC = 93

#LEVELS_DRIVE_STRENGTH_LIST = [1,2,3,4,6,8]
LEVELS_DRIVE_STRENGTH_LIST = [1,3]
#BUFFER_DRIVE_STRENGTH_LIST = [1,2,3,4,5,6,9,11,13,16]
BUFFER_DRIVE_STRENGTH_LIST = [1]

NUM_LEVLS = 7

#SETUP_RUN_DIRECTORY = True
SETUP_RUN_DIRECTORY=False

CREATE_REPORTS = True
#CREATE_REPORTS = False

STAGES_TO_RUN = []
#STAGES_TO_RUN += ['MODIFY_mem_tb_mpscm_netlist_DUT']
STAGES_TO_RUN += ['SALAMANDRA']
STAGES_TO_RUN += ['PLACEANDROUTE']
#STAGES_TO_RUN = []

runCommands=dict()
runTimes=dict()
# ---- Run Paths ---- #
runPaths=dict()
#runPaths['home'] = "/project/test_project/users/frommes/ws/scm_compiler_sf/"
runPaths['home'] = "/project/test_project/users/marinbh/ws/zevel/sapir/scm_compiler_sf/"

# ---- Run Commands ---- #
runCommands['SGE']='qrsh -V -cwd \' '

###################################################################################
##                               ALL THE OPTIONS                                 ##
###################################################################################
#level = params['ADDR_WIDTH'] + 1
level = NUM_LEVLS - 1
level_var = len(LEVELS_DRIVE_STRENGTH_LIST)
for i in range(level_var**level):
  power = ""
  temp = i
  #calculate the first l levels power
  while(temp > 1):
    power = "," + power
    current = temp % 6
    power = str(current) + power
    temp = temp / 6
  for j in BUFFER_DRIVE_STRENGTH_LIST:
    power = "[" + power + str(j) + "]"



    ###################################################################################
    ##  First, modify "params['MUX_DRIVE_STRENGTH']" in the define_parameters file.  ##
    ###################################################################################
    fin = open("./ID.py", "r")
    new_file_lines = []
    for line in fin:
      if ('params[\'MUX_DRIVE_STRENGTH\']' in line):
        new_file_lines.append('params[\'MUX_DRIVE_STRENGTH\'] = ' + power + '\n')
      else:
        new_file_lines.append(line)

    fin.close()
    fout = open("./ID.py", "w")
    for line in new_file_lines:
      fout.write(line)
    fout.close()

    ###################################################################################
    ##                                RUN SALAMANDRA                                 ##
    ###################################################################################
    
    runCommands['SALAMANDRA']  = runCommands['SGE']+'python3 scm_compiler_salamandra.py \''
    os.system("cd " + runPaths['home'] + " && "+ runCommands['SALAMANDRA'])
    
            
    ###################################################################################
    ##                         modify RUN_ID tcl file                                ##
    ###################################################################################
    RUN_ID_NAME = ''
    for layer in power:
      RUN_ID_NAME += ('X'+str(layer))
    fin = open("./RUN_ID_NAME.tcl", "r")
    new_file_lines = []
    for line in fin:
      if ('set timing_report_file' in line):
        new_file_lines.append('set timing_report_file timing_report_'+str(RUN_ID_NAME)+'\n')
      else:
        new_file_lines.append(line)

    fin.close()
    fout = open("./RUN_ID_NAME.tcl", "w")
    for line in new_file_lines:
        fout.write(line)
    fout.close()

            
    ###################################################################################
    ##                                RUN INNOVUS                                    ##
    ###################################################################################

    runPaths['workspace'] = runPaths['home'] + 'workspace/'
    runPaths['PLACEANDROUTE'] = runPaths['workspace'] + "innovus/"
    runCommands['PLACEANDROUTE'] = runCommands['SGE'] + 'qinnovus -files ../../innovus/backend.tcl \''
              
    os.system("cd " + runPaths['PLACEANDROUTE'] + " && "+ runCommands['PLACEANDROUTE'])
            
    ###################################################################################
    ##                          add data to summery file                             ##
    ###################################################################################
    
    # ###check if an old version exists, and if so, overwrite.
    # existed = 0

    # summery_data = str(RUN_ID_NAME)+' @  Total delay: '+'timing report name'+' @ Width: '+'tcl_FloorPlan_file_name'+'\n'
    # fin = open("./summery.rpt", "r")
    # new_file_lines = []
    # for line in fin:
    #   if (str(RUN_ID_NAME) in line):
    #     existed = 1
    #     new_file_lines.append(summery_data)
    #   else:
    #     new_file_lines.append(line)
    # if(not existed)
    #   new_file_lines.append(summery_data)

    # fin.close()
    # fout = open("./summery.rpt", "w")
    # for line in new_file_lines:
    #     fout.write(line)
    # fout.close()


#         
exit()

    
    
"""   
     
for ROWS in ROWS_LIST:
  #for ADDR_WIDTH in ADDR_WIDTH_LIST:
   for DATA_WIDTH in DATA_WIDTH_LIST:
    for WP_RP_TUPLE in WP_RP_TUPLE_list:
      WP = WP_RP_TUPLE[0]
      RP = WP_RP_TUPLE[1]
    #for WP in WP_LIST:
     #for RP in RP_LIST:
      for CLK_PERIOD in CLK_PERIODS_LIST:
       for RUNTYPE in RUNTYPES:
        # ---- Run Commands ---- #  
        runCommands['setVariables']=' "set RUNTYPE '+RUNTYPE+'" '
        runCommands['XTERM'] = runCommands['SGE'] + 'xterm'
        runCommands['TB_RTL']  = ''
  
        #runCommands['SYNTHESIS']  = 'rc -bg -execute ' + runCommands['setVariables'] +' -files scripts/synthesis.tcl \''
        runCommands['SYNTHESIS']  = runCommands['SGE'] + 'xterm -e genus -bg -execute ' + runCommands['setVariables'] +' -files ../../scripts/genus.tcl \''
        runCommands['MODIFY_mem_tb_mpscm_netlist_DUT']  = 'python modify_mem_tb_mpscm_netlist_DUT.py'     # MODIFY_mem_tb_mpscm_netlist_DUT (add all ports to DUT in TB)
        runCommands['MODIFY_mpscm_postsyn_FOR_TB']  = 'python modify_mpscm.postsyn_for_tb.py'             # modify_mpscm.postsyn for tb (duplicate postsyn netlist and change toplaevel module name)
        runCommands['MODIFY_pin_to_rtl']  = 'python modify_pin_to_rtl.py'                                 # modify_pin_to_rtl  (change pin placement to fit syn rtl)
        runCommands['SALAMANDRA']  = runCommands['SGE']+'python3 mpscm_compiler_salamandra.py \''
        runCommands['TB_SALAMANDRA']  = runCommands['SGE'] + 'xterm -e irun -f ../../sourcecode/TB/tb_file_list.f -debug -sv -top mem_tb -l irun_SALAMANDRA.log -timescale 1ns/1ps -nospecify -delta_sequdp_delay -define SALAMANDRA \''
        runCommands['TB_NETLIST']  = runCommands['SGE'] + 'xterm -e irun -f ../../sourcecode/TB/tb_file_list.f -debug -sv -top mem_tb -l irun_POSTSYN.log -timescale 1ns/1ps -nospecify -delta_sequdp_delay -define POSTSYN \''
        runCommands['PLACEANDROUTE'] = runCommands['SGE'] + 'xterm -e innovus -files ../../innovus/backend.tcl \''
        #runCommands['PLACEANDROUTE'] = runCommands['SGE'] + 'xterm -e innovus -execute ' + runCommands['setVariables'] +' -files innovus/backend.tcl \''  
        runCommands['MODIFY_mpscm_backannotation_FOR_TB']  = 'python modify_mpscm.backannotation_for_tb.py'   # modify_mpscm.backannotation for tb (change backannotation netlist module name and change TB DUT module name)  
        #backAnnotationOptions = ' -access +rwc -64bit -timescale 1ns/1ps -define BACKANNOTATION -v ' + runPaths['standard_cell_verilog']
        #runCommands['BACKANNOTATION'] = runCommands['SGE'] + 'xterm -e irun -f ../../sourcecode/TB/tb_file_list.f -debug -sv -top mem_tb -timescale 1ns/1ps -delta_sequdp_delay -define BACKANNOTATION -input ../../scripts/backannotation.tcl \''   # +sdf_verbose
        runCommands['BACKANNOTATION'] = runCommands['SGE'] + 'xterm -e irun -f ../../sourcecode/TB/tb_file_list.f -debug -sv -disable_sem2009 -top mem_tb -l irun_BACKANNOTATION.log -timescale 1ns/1ps -define BACKANNOTATION -input ../../scripts/backannotation.tcl -sdf_simtime \''   # +sdf_verbose
        runCommands['POWERREPORTS'] = runCommands['SGE'] + 'xterm -e innovus -files ../../innovus/create_power_reports.tcl \''
     

        # ----- Setup basic variables ----- #
        #ROWS = 2**ADDR_WIDTH
        ADDR_WIDTH = math.ceil(math.log2(ROWS))
        sizeString=str(ROWS)+'X'+str(DATA_WIDTH)+'_WP_'+str(WP)+'_RP_'+str(RP)
        runPaths['main'] = runPaths['home']+sizeString+'_CLK_'+str(CLK_PERIOD)+'/'+RUNTYPE+'/'
        runPaths['SOURCE'] = runPaths['main'] + "sourcecode/"
        runPaths['MODIFY_mem_tb_mpscm_netlist_DUT'] = runPaths['SOURCE']+'TB/'
        runPaths['MODIFY_mpscm_postsyn_FOR_TB'] = runPaths['SOURCE']+'TB/'
        runPaths['MODIFY_pin_to_rtl'] = runPaths['main']+'scripts/'
        runPaths['workspace'] = runPaths['main'] + 'workspace/'
        runPaths['SALAMANDRA'] = runPaths['main'] + 'salamandra/'
        runPaths['TB_SALAMANDRA'] = runPaths['workspace'] + "TB/"                
        runPaths['SYNTHESIS'] = runPaths['workspace'] + "synthesis/"
        runPaths['TB_NETLIST'] = runPaths['workspace'] + "TB/"
        runPaths['PLACEANDROUTE'] = runPaths['workspace'] + "innovus/"
        runPaths['MODIFY_mpscm_backannotation_FOR_TB'] = runPaths['SOURCE']+'TB/'        
        runPaths['BACKANNOTATION'] = runPaths['workspace'] + "TB/"
        runPaths['POWERREPORTS'] = runPaths['workspace'] + "innovus/"
        os.environ["DISPLAY"] = "enicsm01:"+str(MY_VNC)+".0"

        # ----- Setup Run Directory ----- #
        if SETUP_RUN_DIRECTORY:
            if os.path.exists(runPaths['main']):
                os.system("rm -r -f "+runPaths['main'])
            print('Creating Run Directory: ' + runPaths['main'])
            os.makedirs(runPaths['main'])
            os.system("cp -r " + runPaths['skel'] + '/* ' + runPaths['main'])
            pythonLogFile = open(runPaths['main'] + 'logFile.txt' ,'w')
            pythonLogFile.close()
            
            # ----- Customize all Defines File ----- #
            file_list = []          # tupple of: (source file -> destination file)           
            file_list += [(runPaths['skel']+'salamandra/define_parameters.py', runPaths['main']+'salamandra/define_parameters.py')]

            

            for f in file_list:
                f_src = open(f[0], 'r')
                f_dst = open(f[1], 'w')
                for line in f_src:
                    if 'MUX_DRIVE_STRENGTH' in line:
                      newLine = 'params['MUX_DRIVE_STRENGTH'] = [2,2,2,8,1,1,1]'                     
                    

                    f_dst.write(newLine)
                f_src.close()
                f_dst.close()

        else:
            pass
            #pythonLogFile = open(runPaths['main'] + 'logFile.txt' ,'a')



        runTimes['START'] = datetime.datetime.now().replace(microsecond=0)
        for STAGE in STAGES_TO_RUN:
            if (RUNTYPE != 'RTL'):
                if (STAGE in ['MODIFY_pin_to_rtl','SYNTHESIS','MODIFY_mpscm_postsyn_FOR_TB','TB_NETLIST']):
                    continue
            if (RUNTYPE == 'RTL'):
                if (STAGE in ['TB_SALAMANDRA']):
                    continue
            start_time = datetime.datetime.now().replace(microsecond=0)
            pythonLogFile = open(runPaths['main'] + 'logFile.txt' ,'a')
            pythonLogFile.write(STAGE + ' started at ' +str(start_time) + '\n')
            print("cd " + runPaths[STAGE] + " && "+ runCommands[STAGE]+ '\n'+ '\n')
            os.system("cd " + runPaths[STAGE] + " && "+ runCommands[STAGE])
            end_time = datetime.datetime.now().replace(microsecond=0)
            runTimes[STAGE]=end_time-start_time
            pythonLogFile.write(STAGE + ' ended at ' + str(end_time) + '\n')
            pythonLogFile.write(STAGE + ' took ' + str(runTimes[STAGE]) + '\n')
            pythonLogFile.close()
    
        runTimes['END'] = datetime.datetime.now().replace(microsecond=0)
        runTimes['TOTAL'] = runTimes['END']-runTimes['START']

        ##########################################################
        #################### Write to summaryFile #################
        ##########################################################

        if CREATE_REPORTS:
            print('\n'+'#'*40)
            print('START CREATE REPORTS (summaryFile.txt)')
            print('#'*40+'\n')
            reportsPath = runPaths['main']+'reports/'
            innoPath = reportsPath+'innovus/'
            PowerReportsPath = reportsPath+'innovus/power_reports/'

            summaryFile = open(runPaths['main']+ 'summaryFile.txt' ,'a') 
            summaryFile.write('Summary file of - '+runPaths['main']+'\n\n')
            if ('POWERREPORTS' in STAGES_TO_RUN):
                summaryFile.write('                                                               Internal   Switching      Total     Leakage   \n')
                summaryFile.write('                                                                  Power       Power      Power       Power   \n')
                for mode in ['random', 'write', 'read', 'idle']:
                    mode_power_report_file = open(PowerReportsPath +mode+'_mode_power.rpt','r')
                    for line in mode_power_report_file:
                        if 'Total (' in line:
                            summaryFile.write('Total '+mode+'  \tmode power is :' +line + '\n')
                        if ('Total Capacitance' in line) and (mode=='idle'):
                            summaryFile.write('Total capacitance is :' +line + '\n')
    
            if ('PLACEANDROUTE' in STAGES_TO_RUN):     
                total_wire_length = open(innoPath + 'reportWireLength.post_route.txt','r')               
                for line in total_wire_length:
                    if 'Total Wire Length' in line:
                        summaryFile.write(line + '\n')

                Density_file = open(innoPath + 'checkPlace.post_route.txt','r')
                for line in Density_file:
                    if 'Placement Density' in line:
                        summaryFile.write(line + '\n')
                timing_summary_file = open(innoPath + 'timing_summary.rpt','r')
                for line in timing_summary_file:
                    if 'Total' in line:
                        summaryFile.write(line + '\n')

                summaryFile.write('Place and Route run time is: ' + str(runTimes['PLACEANDROUTE']) + '\n')
            summaryFile.write('Total run time is: ' + str(runTimes['TOTAL']) + '\n')
            summaryFile.write('='*50+'\n')
            summaryFile.close()
            print('\n'+'#'*40)
            print('FINISH CREATE REPORTS (summaryFile.txt)')
            print('#'*40+'\n')


"""
