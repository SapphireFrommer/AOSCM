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
runPaths['home'] = "/project/test_project/users/frommes/ws/scm_compiler_sf/"
#runPaths['home'] = "/project/test_project/users/marinbh/ws/zevel/sapir/scm_compiler_sf/"

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
  for k in range(level-1):
    power = "," + power
    current = int(temp % 6)
    gamba = LEVELS_DRIVE_STRENGTH_LIST[current]
    power = str(gamba) + power
    temp = int(temp / 6)
  for j in BUFFER_DRIVE_STRENGTH_LIST:
    power = "[" + power + str(j) + "]"
    #print ('power= ' + power + '\n')




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
    print('START - Salamandra "python3 scm_compiler_salamandra.py"\n')
    runCommands['SALAMANDRA']  = runCommands['SGE']+'python3 scm_compiler_salamandra.py \''
    os.system("cd " + runPaths['home'] + " && "+ runCommands['SALAMANDRA'])
    print('DONE - Salamandra "python3 scm_compiler_salamandra.py"\n')
            
    ###################################################################################
    ##                         modify RUN_ID tcl file                                ##
    ###################################################################################
    # RUN_ID_NAME = ''
    # for layer in power:
    #   RUN_ID_NAME += ('X'+str(layer))
    power = power.rstrip(']')
    power = power.replace(',','X')
    power = power.replace('[','X')
    fin = open("./RUN_ID_NAME.tcl", "r")
    new_file_lines = []
    for line in fin:
      if ('set timing_report_file' in line):
        new_file_lines.append('set timing_report_file timing_report_'+str(power)+'\n')
      else:
        new_file_lines.append(line)

    fin.close()
    fout = open("./RUN_ID_NAME.tcl", "w")
    for line in new_file_lines:
        fout.write(line)
    fout.close()
    print('DONE - modify RUN_ID tcl file \n')

            
    ###################################################################################
    ##                                RUN INNOVUS                                    ##
    ###################################################################################

    runPaths['workspace'] = runPaths['home'] + 'workspace/'
    runPaths['PLACEANDROUTE'] = runPaths['workspace'] + "innovus/"
    runCommands['PLACEANDROUTE'] = runCommands['SGE'] + 'innovus -files ../../innovus/backend.tcl \''
              
    os.system("cd " + runPaths['PLACEANDROUTE'] + " && "+ runCommands['PLACEANDROUTE'])
    print('DONE - RUN INNOVUS \n')
            
    ###################################################################################
    ##                          add data to summery file                             ##
    ###################################################################################
    
    #id name = str(power)
    #width from width.rpt
    fin = open("./width.rpt","r")
    width = fin.readline()
    fin.close()
    #width = 7 #for now
    #delay time = from reports/timing_summary.rpt
    fin = open("./reports/timing_summary.rpt","r")
    delay = fin.readline()
    fin.close()
    #delay = 5 #for now
    
    found = False
    fin = open("./summary.rpt", "r")
    new_file_lines = []
    for line in fin:
      if (str(power) in line):
        new_file_lines.append('ID: '+str(power)+'\n')
        new_file_lines.append('WIDTH: '+str(width)+'\n')
        new_file_lines.append(str(delay)+'\n')
        #mark as found
        found = True
        #skip the other two lines we override
        line = next(fin)
        line = next(fin)
      else:
        new_file_lines.append(line)
        line = next(fin)
        new_file_lines.append(line)
        line = next(fin)
        new_file_lines.append(line)
    #if wasn't found in the file, add it
    if not found:
      new_file_lines.append('ID: '+str(power)+'\n')
      new_file_lines.append('WIDTH: '+str(width)+'\n')
      new_file_lines.append('DELAY TIME: '+str(delay)+'\n')
      

    fin.close()
    fout = open("./summary.rpt", "w")
    for line in new_file_lines:
      fout.write(line)
    fout.close() 
            
          
exit()
