####################### define parameter #######################
params = {}
params['DATA_WIDTH'] = 32
params['ADDR_WIDTH'] = 5		# Number of words (rows) is 2**ADDR_WIDTH 

params['RWL_NUM'] = 4	    # how many rwl buffer will be
params['WELLTAP'] = 8	    # after how many bitslice will be welltap (and VDD GND stripes)
params['middle_horizontal_gap'] = 0     # how many site(s) will be at the middle horizontal gap 

params['add_PreDec_out_BUF'] = 0        # 1 to adding PreDec_out_BUF OR 0 to not add
params['add_GDIN_out_BUF'] = 1        # 1 to adding GDIN_out_BUF OR 0 to not add
params['add_RADDR_out_BUF'] = 1        # 1 to adding RADDR_out_BUF OR 0 to not add


params['TRACKS'] = '9'

params['technology'] = 'tsmc65_'+params['TRACKS']+'TR'
#params['technology'] = 'Synopsys28'

params['TCL_tool'] = 'Cadence'
#params['TCL_tool'] = 'Synopsys'


if params['technology'] == 'tsmc65_'+params['TRACKS']+'TR':
    params['TOPLEVEL'] = "scm65_"+str(params['DATA_WIDTH'])+"x"+str(2**params['ADDR_WIDTH'])
if params['technology'] == 'Synopsys28':
    params['TOPLEVEL'] = "scm28_"+str(params['DATA_WIDTH'])+"x"+str(2**params['ADDR_WIDTH'])

params['MUX_DRIVE_STRENGTH'] = [1,1,4,8,1,1,1]

# NAND2 and NOR2 "x" options = 1,2,3,4,6,8
# (last level) buffer and inverter "x" options = 1,2,3,4,5,6,7P5,9,11,13,16
