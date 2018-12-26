####################### define parameter #######################
params = {}
params['DATA_WIDTH'] = 16
params['ADDR_WIDTH'] = 4		# Number of words (rows) is 2**ADDR_WIDTH 

params['RWL_NUM'] = 8	# how many rwl buffer will be
params['WELLTAP'] = 8	# after how many bitslice will be welltap (and VDD GND stripes)

params['technology'] = 'tsmc65'
#params['technology'] = 'Synopsys28'


if params['technology'] == 'tsmc65':
    params['TOPLEVEL'] = "scm65_"+str(params['DATA_WIDTH'])+"x"+str(2**params['ADDR_WIDTH'])
if params['technology'] == 'Synopsys28':
    params['TOPLEVEL'] = "scm28_"+str(params['DATA_WIDTH'])+"x"+str(2**params['ADDR_WIDTH'])

params['TRACKS'] = '12'

