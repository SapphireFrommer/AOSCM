####################### define parameter #######################
param = {}
param['TOPLEVEL'] = "scm65"
param['DATA_WIDTH'] = 16
param['ADDR_WIDTH'] = 4		# Number of words (rows) is 2**ADDR_WIDTH 

param['RWL_NUM'] = 8	# how many rwl buffer will be
param['WELLTAP'] = 5	# after how many bitslice will be welltap (and VDD GND stripes)
param['technology'] = 'tsmc65'
param['TRACKS'] = '12'

