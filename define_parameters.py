####################### define parameter #######################
params = {}
params['DATA_WIDTH'] = 57
params['ADDR_WIDTH'] = 6		# Number of words (rows) is 2**ADDR_WIDTH 

params['RWL_NUM'] = 4	    # how many rwl buffer will be
params['WELLTAP'] = 8	    # after how many bitslice will be welltap (and VDD GND stripes)
params['middle_horizontal_gap'] = 0     # how many site(s) will be at the middle horizontal gap 

params['add_PreDec_out_BUF'] = 0        # 1 to adding PreDec_out_BUF OR 0 to not add
params['add_GDIN_out_BUF'] = 1        # 1 to adding GDIN_out_BUF OR 0 to not add
params['add_RADDR_out_BUF'] = 1        # 1 to adding RADDR_out_BUF OR 0 to not add


params['TRACKS'] = '9'

params['technology'] = 'tsmc65_'+params['TRACKS']+'TR'
#params['technology'] = 'Synopsys28'


if params['technology'] == 'tsmc65_'+params['TRACKS']+'TR':
    params['TOPLEVEL'] = "scm65_"+str(params['DATA_WIDTH'])+"x"+str(2**params['ADDR_WIDTH'])
if params['technology'] == 'Synopsys28':
    params['TOPLEVEL'] = "scm28_"+str(params['DATA_WIDTH'])+"x"+str(2**params['ADDR_WIDTH'])


