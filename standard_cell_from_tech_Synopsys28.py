from salamandra import *

class SEP_AN2_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_AN2_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_ECOCT_2(ComponentXY):
	__defaultName = 'SEP_AN2_ECOCT_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_ECOCT_4(ComponentXY):
	__defaultName = 'SEP_AN2_ECOCT_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_AN3_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21ECOCT_4(ComponentXY):
	__defaultName = 'SEP_AO21ECOCT_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_AO21_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO22_ECOCT_2(ComponentXY):
	__defaultName = 'SEP_AO22_ECOCT_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.68, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI211_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_AOI211_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_AOI21_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21_ECOCT_4(ComponentXY):
	__defaultName = 'SEP_AOI21_ECOCT_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI22_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_AOI22_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI31_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_AOI31_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_BUF_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_ECOCT_2(ComponentXY):
	__defaultName = 'SEP_BUF_ECOCT_2'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_ECOCT_4(ComponentXY):
	__defaultName = 'SEP_BUF_ECOCT_4'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.68, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_EN2_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN3_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_EN3_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_EO2_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO3_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_EO3_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPRBQ_V2ECOCT_1(ComponentXY):
	__defaultName = 'SEP_FDPRBQ_V2ECOCT_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.92, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPRBQ_V2ECOCT_2(ComponentXY):
	__defaultName = 'SEP_FDPRBQ_V2ECOCT_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.76, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPRBSBQ_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_FDPRBSBQ_ECOCT_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', in4='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPRBSBQ_ECOCT_2(ComponentXY):
	__defaultName = 'SEP_FDPRBSBQ_ECOCT_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', in4='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.76, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPSBQ_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_FDPSBQ_ECOCT_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.2, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPSBQ_ECOCT_2(ComponentXY):
	__defaultName = 'SEP_FDPSBQ_ECOCT_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.76, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_DECOCT_1(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_DECOCT_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.76, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_DECOCT_2(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_DECOCT_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.6, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_DECOCT_4(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_DECOCT_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(7.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBSBQ_V2ECOCT_1(ComponentXY):
	__defaultName = 'SEP_FSDPRBSBQ_V2ECOCT_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', in6='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.6, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBSBQ_V2ECOCT_2(ComponentXY):
	__defaultName = 'SEP_FSDPRBSBQ_V2ECOCT_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', in6='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.88, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBSBQO_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_FSDPRBSBQO_ECOCT_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', in6='SD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(5.88, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBSBQO_ECOCT_2(ComponentXY):
	__defaultName = 'SEP_FSDPRBSBQO_ECOCT_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', in6='SD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(6.72, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPSBQ_V2ECOCT_1(ComponentXY):
	__defaultName = 'SEP_FSDPSBQ_V2ECOCT_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.04, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPSBQ_V2ECOCT_2(ComponentXY):
	__defaultName = 'SEP_FSDPSBQ_V2ECOCT_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.32, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_INV_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.28, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_ECOCT_2(ComponentXY):
	__defaultName = 'SEP_INV_ECOCT_2'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_ECOCT_4(ComponentXY):
	__defaultName = 'SEP_INV_ECOCT_4'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDPQ_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_LDPQ_ECOCT_1'

	def __init__(self, name = __defaultName, in1='G', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDPQ_ECOCT_2(ComponentXY):
	__defaultName = 'SEP_LDPQ_ECOCT_2'

	def __init__(self, name = __defaultName, in1='G', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_MUXI2_ECOCT_1'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_ECOCT_2(ComponentXY):
	__defaultName = 'SEP_MUXI2_ECOCT_2'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_ND2_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_ECOCT_4(ComponentXY):
	__defaultName = 'SEP_ND2_ECOCT_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_ND3_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3_ECOCT_4(ComponentXY):
	__defaultName = 'SEP_ND3_ECOCT_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_NR2_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_ECOCT_4(ComponentXY):
	__defaultName = 'SEP_NR2_ECOCT_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_NR3_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_ECOCT_4(ComponentXY):
	__defaultName = 'SEP_NR3_ECOCT_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA21_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_OA21_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA21_ECOCT_4(ComponentXY):
	__defaultName = 'SEP_OA21_ECOCT_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA22_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_OA22_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA22_ECOCT_4(ComponentXY):
	__defaultName = 'SEP_OA22_ECOCT_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI211_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_OAI211_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_OAI21_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21_ECOCT_4(ComponentXY):
	__defaultName = 'SEP_OAI21_ECOCT_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI22_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_OAI22_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI31_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_OAI31_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_ECOCT_4(ComponentXY):
	__defaultName = 'SEP_OR2_ECOCT_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_OR2_ECOCT_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_TIE0_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_TIE0_ECOCT_1'


class SEP_TIE1_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_TIE1_ECOCT_1'


class SEP_TIEDIN_ECOCT_1(ComponentXY):
	__defaultName = 'SEP_TIEDIN_ECOCT_1'

	def __init__(self, name = __defaultName, in1='X', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.28, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ADDF_V1_0P5(ComponentXY):
	__defaultName = 'SEP_ADDF_V1_0P5'

	def __init__(self, name = __defaultName, in1='A', in2='B', in3='CI', out1='S', out2='CO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ADDF_V1_1(ComponentXY):
	__defaultName = 'SEP_ADDF_V1_1'

	def __init__(self, name = __defaultName, in1='A', in2='B', in3='CI', out1='S', out2='CO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ADDF_V1_2(ComponentXY):
	__defaultName = 'SEP_ADDF_V1_2'

	def __init__(self, name = __defaultName, in1='A', in2='B', in3='CI', out1='S', out2='CO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ADDF_V1_4(ComponentXY):
	__defaultName = 'SEP_ADDF_V1_4'

	def __init__(self, name = __defaultName, in1='A', in2='B', in3='CI', out1='S', out2='CO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ADDH_4(ComponentXY):
	__defaultName = 'SEP_ADDH_4'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='S', out2='CO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ADDH_0P5(ComponentXY):
	__defaultName = 'SEP_ADDH_0P5'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='S', out2='CO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ADDH_1(ComponentXY):
	__defaultName = 'SEP_ADDH_1'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='S', out2='CO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ADDH_2(ComponentXY):
	__defaultName = 'SEP_ADDH_2'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='S', out2='CO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ADDH_DG_4(ComponentXY):
	__defaultName = 'SEP_ADDH_DG_4'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='S', out2='CO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_12(ComponentXY):
	__defaultName = 'SEP_AN2_12'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_16(ComponentXY):
	__defaultName = 'SEP_AN2_16'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_24(ComponentXY):
	__defaultName = 'SEP_AN2_24'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.86, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_3(ComponentXY):
	__defaultName = 'SEP_AN2_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_4(ComponentXY):
	__defaultName = 'SEP_AN2_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_8(ComponentXY):
	__defaultName = 'SEP_AN2_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_0P5(ComponentXY):
	__defaultName = 'SEP_AN2_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_1(ComponentXY):
	__defaultName = 'SEP_AN2_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_1P5(ComponentXY):
	__defaultName = 'SEP_AN2_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_2(ComponentXY):
	__defaultName = 'SEP_AN2_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_6(ComponentXY):
	__defaultName = 'SEP_AN2_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_MG_0P5(ComponentXY):
	__defaultName = 'SEP_AN2_MG_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_MG_0P75(ComponentXY):
	__defaultName = 'SEP_AN2_MG_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_MG_1(ComponentXY):
	__defaultName = 'SEP_AN2_MG_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_MG_1P5(ComponentXY):
	__defaultName = 'SEP_AN2_MG_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_MG_3(ComponentXY):
	__defaultName = 'SEP_AN2_MG_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_MG_6(ComponentXY):
	__defaultName = 'SEP_AN2_MG_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_S_0P5(ComponentXY):
	__defaultName = 'SEP_AN2_S_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_S_1(ComponentXY):
	__defaultName = 'SEP_AN2_S_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_S_1P5(ComponentXY):
	__defaultName = 'SEP_AN2_S_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_S_2(ComponentXY):
	__defaultName = 'SEP_AN2_S_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_S_3(ComponentXY):
	__defaultName = 'SEP_AN2_S_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_S_4(ComponentXY):
	__defaultName = 'SEP_AN2_S_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN2_S_8(ComponentXY):
	__defaultName = 'SEP_AN2_S_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3_4(ComponentXY):
	__defaultName = 'SEP_AN3_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3_8(ComponentXY):
	__defaultName = 'SEP_AN3_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3_MM_4(ComponentXY):
	__defaultName = 'SEP_AN3_MM_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3_MM_8(ComponentXY):
	__defaultName = 'SEP_AN3_MM_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3_0P5(ComponentXY):
	__defaultName = 'SEP_AN3_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3_1(ComponentXY):
	__defaultName = 'SEP_AN3_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3_2(ComponentXY):
	__defaultName = 'SEP_AN3_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3_MM_1(ComponentXY):
	__defaultName = 'SEP_AN3_MM_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3_MM_2(ComponentXY):
	__defaultName = 'SEP_AN3_MM_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3B_2(ComponentXY):
	__defaultName = 'SEP_AN3B_2'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3B_3(ComponentXY):
	__defaultName = 'SEP_AN3B_3'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3B_4(ComponentXY):
	__defaultName = 'SEP_AN3B_4'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3B_8(ComponentXY):
	__defaultName = 'SEP_AN3B_8'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3B_0P5(ComponentXY):
	__defaultName = 'SEP_AN3B_0P5'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN3B_1(ComponentXY):
	__defaultName = 'SEP_AN3B_1'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4_4(ComponentXY):
	__defaultName = 'SEP_AN4_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4_8(ComponentXY):
	__defaultName = 'SEP_AN4_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4_L_1P5(ComponentXY):
	__defaultName = 'SEP_AN4_L_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4_MM_4(ComponentXY):
	__defaultName = 'SEP_AN4_MM_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4_U_0P5(ComponentXY):
	__defaultName = 'SEP_AN4_U_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4_U_1(ComponentXY):
	__defaultName = 'SEP_AN4_U_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4_0P5(ComponentXY):
	__defaultName = 'SEP_AN4_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4_1(ComponentXY):
	__defaultName = 'SEP_AN4_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4_2(ComponentXY):
	__defaultName = 'SEP_AN4_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4_L_0P5(ComponentXY):
	__defaultName = 'SEP_AN4_L_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4_L_1(ComponentXY):
	__defaultName = 'SEP_AN4_L_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4_MM_1(ComponentXY):
	__defaultName = 'SEP_AN4_MM_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4_MM_1P5(ComponentXY):
	__defaultName = 'SEP_AN4_MM_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4_MM_2(ComponentXY):
	__defaultName = 'SEP_AN4_MM_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4B_2(ComponentXY):
	__defaultName = 'SEP_AN4B_2'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', in4='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4B_4(ComponentXY):
	__defaultName = 'SEP_AN4B_4'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', in4='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.1, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4B_8(ComponentXY):
	__defaultName = 'SEP_AN4B_8'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', in4='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.06, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4B_0P5(ComponentXY):
	__defaultName = 'SEP_AN4B_0P5'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', in4='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN4B_1(ComponentXY):
	__defaultName = 'SEP_AN4B_1'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', in4='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN6_4(ComponentXY):
	__defaultName = 'SEP_AN6_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', in5='A5', in6='A6', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN6_1(ComponentXY):
	__defaultName = 'SEP_AN6_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', in5='A5', in6='A6', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AN6_2(ComponentXY):
	__defaultName = 'SEP_AN6_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', in5='A5', in6='A6', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO211_4(ComponentXY):
	__defaultName = 'SEP_AO211_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO211_0P5(ComponentXY):
	__defaultName = 'SEP_AO211_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO211_1(ComponentXY):
	__defaultName = 'SEP_AO211_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO211_2(ComponentXY):
	__defaultName = 'SEP_AO211_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21_4(ComponentXY):
	__defaultName = 'SEP_AO21_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21_6(ComponentXY):
	__defaultName = 'SEP_AO21_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21_8(ComponentXY):
	__defaultName = 'SEP_AO21_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21_0P5(ComponentXY):
	__defaultName = 'SEP_AO21_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21_1(ComponentXY):
	__defaultName = 'SEP_AO21_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21_1P5(ComponentXY):
	__defaultName = 'SEP_AO21_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21_2(ComponentXY):
	__defaultName = 'SEP_AO21_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21_DG_1(ComponentXY):
	__defaultName = 'SEP_AO21_DG_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21_DG_2(ComponentXY):
	__defaultName = 'SEP_AO21_DG_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21_DG_4(ComponentXY):
	__defaultName = 'SEP_AO21_DG_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21B_3(ComponentXY):
	__defaultName = 'SEP_AO21B_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21B_12(ComponentXY):
	__defaultName = 'SEP_AO21B_12'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.18, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21B_16(ComponentXY):
	__defaultName = 'SEP_AO21B_16'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.86, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21B_1P5(ComponentXY):
	__defaultName = 'SEP_AO21B_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21B_2(ComponentXY):
	__defaultName = 'SEP_AO21B_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21B_4(ComponentXY):
	__defaultName = 'SEP_AO21B_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21B_6(ComponentXY):
	__defaultName = 'SEP_AO21B_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21B_8(ComponentXY):
	__defaultName = 'SEP_AO21B_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21B_0P5(ComponentXY):
	__defaultName = 'SEP_AO21B_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21B_0P75(ComponentXY):
	__defaultName = 'SEP_AO21B_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO21B_1(ComponentXY):
	__defaultName = 'SEP_AO21B_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO221_4(ComponentXY):
	__defaultName = 'SEP_AO221_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO221_0P5(ComponentXY):
	__defaultName = 'SEP_AO221_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO221_1(ComponentXY):
	__defaultName = 'SEP_AO221_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO221_2(ComponentXY):
	__defaultName = 'SEP_AO221_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO2222_MN_2(ComponentXY):
	__defaultName = 'SEP_AO2222_MN_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C1', in6='C2', in7='D1', in8='D2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Input(in7) )
		self.add_pin(Input(in8) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO222_2(ComponentXY):
	__defaultName = 'SEP_AO222_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C1', in6='C2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO222_4(ComponentXY):
	__defaultName = 'SEP_AO222_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C1', in6='C2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO222_1(ComponentXY):
	__defaultName = 'SEP_AO222_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C1', in6='C2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO22_0P5(ComponentXY):
	__defaultName = 'SEP_AO22_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO22_1(ComponentXY):
	__defaultName = 'SEP_AO22_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO22_2(ComponentXY):
	__defaultName = 'SEP_AO22_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO22_4(ComponentXY):
	__defaultName = 'SEP_AO22_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO22_6(ComponentXY):
	__defaultName = 'SEP_AO22_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO22_8(ComponentXY):
	__defaultName = 'SEP_AO22_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.64, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO22_DG_1(ComponentXY):
	__defaultName = 'SEP_AO22_DG_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO22_DG_2(ComponentXY):
	__defaultName = 'SEP_AO22_DG_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO22_DG_4(ComponentXY):
	__defaultName = 'SEP_AO22_DG_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO2BB2_2(ComponentXY):
	__defaultName = 'SEP_AO2BB2_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO2BB2_4(ComponentXY):
	__defaultName = 'SEP_AO2BB2_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO2BB2_8(ComponentXY):
	__defaultName = 'SEP_AO2BB2_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO2BB2_DG_2(ComponentXY):
	__defaultName = 'SEP_AO2BB2_DG_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO2BB2_DG_4(ComponentXY):
	__defaultName = 'SEP_AO2BB2_DG_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.1, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO2BB2_0P5(ComponentXY):
	__defaultName = 'SEP_AO2BB2_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO2BB2_1(ComponentXY):
	__defaultName = 'SEP_AO2BB2_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO2BB2_DG_0P5(ComponentXY):
	__defaultName = 'SEP_AO2BB2_DG_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO2BB2_DG_1(ComponentXY):
	__defaultName = 'SEP_AO2BB2_DG_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO2BB2_V3_1(ComponentXY):
	__defaultName = 'SEP_AO2BB2_V3_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO31_4(ComponentXY):
	__defaultName = 'SEP_AO31_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO31_0P5(ComponentXY):
	__defaultName = 'SEP_AO31_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO31_1(ComponentXY):
	__defaultName = 'SEP_AO31_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO31_2(ComponentXY):
	__defaultName = 'SEP_AO31_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO32_4(ComponentXY):
	__defaultName = 'SEP_AO32_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.1, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO32_0P5(ComponentXY):
	__defaultName = 'SEP_AO32_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO32_1(ComponentXY):
	__defaultName = 'SEP_AO32_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AO32_2(ComponentXY):
	__defaultName = 'SEP_AO32_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOA211_2(ComponentXY):
	__defaultName = 'SEP_AOA211_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOA211_DG_1(ComponentXY):
	__defaultName = 'SEP_AOA211_DG_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOA211_DG_2(ComponentXY):
	__defaultName = 'SEP_AOA211_DG_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOA211_DG_3(ComponentXY):
	__defaultName = 'SEP_AOA211_DG_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOA211_DG_4(ComponentXY):
	__defaultName = 'SEP_AOA211_DG_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOA211_DG_8(ComponentXY):
	__defaultName = 'SEP_AOA211_DG_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOAI211_12(ComponentXY):
	__defaultName = 'SEP_AOAI211_12'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.86, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOAI211_2(ComponentXY):
	__defaultName = 'SEP_AOAI211_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOAI211_4(ComponentXY):
	__defaultName = 'SEP_AOAI211_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOAI211_6(ComponentXY):
	__defaultName = 'SEP_AOAI211_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOAI211_8(ComponentXY):
	__defaultName = 'SEP_AOAI211_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOAI211_0P5(ComponentXY):
	__defaultName = 'SEP_AOAI211_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOAI211_0P75(ComponentXY):
	__defaultName = 'SEP_AOAI211_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOAI211_1(ComponentXY):
	__defaultName = 'SEP_AOAI211_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOAI211_3(ComponentXY):
	__defaultName = 'SEP_AOAI211_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI211_1P5(ComponentXY):
	__defaultName = 'SEP_AOI211_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI211_2(ComponentXY):
	__defaultName = 'SEP_AOI211_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI211_3(ComponentXY):
	__defaultName = 'SEP_AOI211_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI211_4(ComponentXY):
	__defaultName = 'SEP_AOI211_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI211_8(ComponentXY):
	__defaultName = 'SEP_AOI211_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI211_G_2(ComponentXY):
	__defaultName = 'SEP_AOI211_G_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI211_G_4(ComponentXY):
	__defaultName = 'SEP_AOI211_G_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI211_0P5(ComponentXY):
	__defaultName = 'SEP_AOI211_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI211_0P75(ComponentXY):
	__defaultName = 'SEP_AOI211_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI211_1(ComponentXY):
	__defaultName = 'SEP_AOI211_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI211_G_1(ComponentXY):
	__defaultName = 'SEP_AOI211_G_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21_16(ComponentXY):
	__defaultName = 'SEP_AOI21_16'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.86, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21_4(ComponentXY):
	__defaultName = 'SEP_AOI21_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21_6(ComponentXY):
	__defaultName = 'SEP_AOI21_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21_8(ComponentXY):
	__defaultName = 'SEP_AOI21_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21_0P5(ComponentXY):
	__defaultName = 'SEP_AOI21_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21_0P75(ComponentXY):
	__defaultName = 'SEP_AOI21_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21_1(ComponentXY):
	__defaultName = 'SEP_AOI21_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21_1P5(ComponentXY):
	__defaultName = 'SEP_AOI21_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21_2(ComponentXY):
	__defaultName = 'SEP_AOI21_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21B_2(ComponentXY):
	__defaultName = 'SEP_AOI21B_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21B_4(ComponentXY):
	__defaultName = 'SEP_AOI21B_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.1, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21B_8(ComponentXY):
	__defaultName = 'SEP_AOI21B_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.92, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21B_0P5(ComponentXY):
	__defaultName = 'SEP_AOI21B_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI21B_1(ComponentXY):
	__defaultName = 'SEP_AOI21B_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI221_2(ComponentXY):
	__defaultName = 'SEP_AOI221_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.68, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI221_4(ComponentXY):
	__defaultName = 'SEP_AOI221_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI221_0P5(ComponentXY):
	__defaultName = 'SEP_AOI221_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI221_1(ComponentXY):
	__defaultName = 'SEP_AOI221_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI222_2(ComponentXY):
	__defaultName = 'SEP_AOI222_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C1', in6='C2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI222_4(ComponentXY):
	__defaultName = 'SEP_AOI222_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C1', in6='C2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI222_0P5(ComponentXY):
	__defaultName = 'SEP_AOI222_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C1', in6='C2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI222_1(ComponentXY):
	__defaultName = 'SEP_AOI222_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C1', in6='C2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI22_12(ComponentXY):
	__defaultName = 'SEP_AOI22_12'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.86, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI22_1P5(ComponentXY):
	__defaultName = 'SEP_AOI22_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI22_2(ComponentXY):
	__defaultName = 'SEP_AOI22_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI22_4(ComponentXY):
	__defaultName = 'SEP_AOI22_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI22_6(ComponentXY):
	__defaultName = 'SEP_AOI22_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI22_8(ComponentXY):
	__defaultName = 'SEP_AOI22_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI22_0P5(ComponentXY):
	__defaultName = 'SEP_AOI22_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI22_0P75(ComponentXY):
	__defaultName = 'SEP_AOI22_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI22_1(ComponentXY):
	__defaultName = 'SEP_AOI22_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI22_3(ComponentXY):
	__defaultName = 'SEP_AOI22_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI22_5(ComponentXY):
	__defaultName = 'SEP_AOI22_5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI22_V3_1(ComponentXY):
	__defaultName = 'SEP_AOI22_V3_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI31_2(ComponentXY):
	__defaultName = 'SEP_AOI31_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI31_4(ComponentXY):
	__defaultName = 'SEP_AOI31_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI31_8(ComponentXY):
	__defaultName = 'SEP_AOI31_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI31_0P5(ComponentXY):
	__defaultName = 'SEP_AOI31_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI31_0P75(ComponentXY):
	__defaultName = 'SEP_AOI31_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI31_1(ComponentXY):
	__defaultName = 'SEP_AOI31_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI32_2(ComponentXY):
	__defaultName = 'SEP_AOI32_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI32_4(ComponentXY):
	__defaultName = 'SEP_AOI32_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI32_1(ComponentXY):
	__defaultName = 'SEP_AOI32_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI33_2(ComponentXY):
	__defaultName = 'SEP_AOI33_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', in6='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI33_4(ComponentXY):
	__defaultName = 'SEP_AOI33_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', in6='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_AOI33_1(ComponentXY):
	__defaultName = 'SEP_AOI33_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', in6='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_U_0P5(ComponentXY):
	__defaultName = 'SEP_BUF_U_0P5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_U_1(ComponentXY):
	__defaultName = 'SEP_BUF_U_1'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_1(ComponentXY):
	__defaultName = 'SEP_BUF_1'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_10(ComponentXY):
	__defaultName = 'SEP_BUF_10'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_12(ComponentXY):
	__defaultName = 'SEP_BUF_12'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_12P5(ComponentXY):
	__defaultName = 'SEP_BUF_12P5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_16(ComponentXY):
	__defaultName = 'SEP_BUF_16'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_16P5(ComponentXY):
	__defaultName = 'SEP_BUF_16P5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.64, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_1P5(ComponentXY):
	__defaultName = 'SEP_BUF_1P5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_2(ComponentXY):
	__defaultName = 'SEP_BUF_2'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_20(ComponentXY):
	__defaultName = 'SEP_BUF_20'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.34, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_24(ComponentXY):
	__defaultName = 'SEP_BUF_24'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.18, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_3(ComponentXY):
	__defaultName = 'SEP_BUF_3'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_32(ComponentXY):
	__defaultName = 'SEP_BUF_32'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.86, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_3P5(ComponentXY):
	__defaultName = 'SEP_BUF_3P5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_4(ComponentXY):
	__defaultName = 'SEP_BUF_4'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_5(ComponentXY):
	__defaultName = 'SEP_BUF_5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_6(ComponentXY):
	__defaultName = 'SEP_BUF_6'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_6P5(ComponentXY):
	__defaultName = 'SEP_BUF_6P5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_8(ComponentXY):
	__defaultName = 'SEP_BUF_8'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_MN_8(ComponentXY):
	__defaultName = 'SEP_BUF_MN_8'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.68, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_D_0P5(ComponentXY):
	__defaultName = 'SEP_BUF_D_0P5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_D_1(ComponentXY):
	__defaultName = 'SEP_BUF_D_1'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_D_16(ComponentXY):
	__defaultName = 'SEP_BUF_D_16'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_D_1P5(ComponentXY):
	__defaultName = 'SEP_BUF_D_1P5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_D_2(ComponentXY):
	__defaultName = 'SEP_BUF_D_2'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_D_3(ComponentXY):
	__defaultName = 'SEP_BUF_D_3'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_D_32(ComponentXY):
	__defaultName = 'SEP_BUF_D_32'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.74, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_D_4(ComponentXY):
	__defaultName = 'SEP_BUF_D_4'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_D_8(ComponentXY):
	__defaultName = 'SEP_BUF_D_8'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_1(ComponentXY):
	__defaultName = 'SEP_BUF_S_1'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_10(ComponentXY):
	__defaultName = 'SEP_BUF_S_10'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_12(ComponentXY):
	__defaultName = 'SEP_BUF_S_12'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_16(ComponentXY):
	__defaultName = 'SEP_BUF_S_16'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_1P25(ComponentXY):
	__defaultName = 'SEP_BUF_S_1P25'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_1P5(ComponentXY):
	__defaultName = 'SEP_BUF_S_1P5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_2(ComponentXY):
	__defaultName = 'SEP_BUF_S_2'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_20(ComponentXY):
	__defaultName = 'SEP_BUF_S_20'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.34, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_24(ComponentXY):
	__defaultName = 'SEP_BUF_S_24'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.9, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_2P5(ComponentXY):
	__defaultName = 'SEP_BUF_S_2P5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_3(ComponentXY):
	__defaultName = 'SEP_BUF_S_3'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_32(ComponentXY):
	__defaultName = 'SEP_BUF_S_32'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.86, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_4(ComponentXY):
	__defaultName = 'SEP_BUF_S_4'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_5(ComponentXY):
	__defaultName = 'SEP_BUF_S_5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_6(ComponentXY):
	__defaultName = 'SEP_BUF_S_6'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_BUF_S_8(ComponentXY):
	__defaultName = 'SEP_BUF_S_8'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTNLT_V5_0P5(ComponentXY):
	__defaultName = 'SEP_CKGTNLT_V5_0P5'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTNLT_V5_0P65(ComponentXY):
	__defaultName = 'SEP_CKGTNLT_V5_0P65'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTNLT_V5_1(ComponentXY):
	__defaultName = 'SEP_CKGTNLT_V5_1'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTNLT_V5_12(ComponentXY):
	__defaultName = 'SEP_CKGTNLT_V5_12'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.64, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTNLT_V5_16(ComponentXY):
	__defaultName = 'SEP_CKGTNLT_V5_16'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.2, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTNLT_V5_2(ComponentXY):
	__defaultName = 'SEP_CKGTNLT_V5_2'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTNLT_V5_3(ComponentXY):
	__defaultName = 'SEP_CKGTNLT_V5_3'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTNLT_V5_4(ComponentXY):
	__defaultName = 'SEP_CKGTNLT_V5_4'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTNLT_V5_6(ComponentXY):
	__defaultName = 'SEP_CKGTNLT_V5_6'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTNLT_V5_8(ComponentXY):
	__defaultName = 'SEP_CKGTNLT_V5_8'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLS_V3_1(ComponentXY):
	__defaultName = 'SEP_CKGTPLS_V3_1'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V7_12(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V7_12'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.02, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V7_16(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V7_16'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(7.14, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V7_24(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V7_24'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(10.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V7_8(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V7_8'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.9, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_0P5(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_0P5'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_0P65(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_0P65'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_0P8(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_0P8'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_1(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_1'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_11(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_11'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.92, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_12(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_12'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.06, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_13(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_13'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.2, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_16(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_16'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.76, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_1P2(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_1P2'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_1P5(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_1P5'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_1P7(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_1P7'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_2(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_2'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_2P5(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_2P5'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_3(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_3'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_3P5(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_3P5'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_4(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_4'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_5(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_5'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_6(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_6'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_7(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_7'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_8(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_8'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.22, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V5_9(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V5_9'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.64, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V7_1(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V7_1'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V7_2(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V7_2'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_CKGTPLT_V7_4(ComponentXY):
	__defaultName = 'SEP_CKGTPLT_V7_4'

	def __init__(self, name = __defaultName, in1='CK', in2='EN', in3='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_DEL_L4_1(ComponentXY):
	__defaultName = 'SEP_DEL_L4_1'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_DEL_L4_2(ComponentXY):
	__defaultName = 'SEP_DEL_L4_2'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_DEL_L4_4(ComponentXY):
	__defaultName = 'SEP_DEL_L4_4'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_DEL_L4_8(ComponentXY):
	__defaultName = 'SEP_DEL_L4_8'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_DEL_L6_1(ComponentXY):
	__defaultName = 'SEP_DEL_L6_1'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_DEL_L6_2(ComponentXY):
	__defaultName = 'SEP_DEL_L6_2'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_DEL_L6_4(ComponentXY):
	__defaultName = 'SEP_DEL_L6_4'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_DEL_L6_8(ComponentXY):
	__defaultName = 'SEP_DEL_L6_8'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.64, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_4(ComponentXY):
	__defaultName = 'SEP_EN2_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_F_1(ComponentXY):
	__defaultName = 'SEP_EN2_F_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_0P5(ComponentXY):
	__defaultName = 'SEP_EN2_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_1(ComponentXY):
	__defaultName = 'SEP_EN2_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_1P5(ComponentXY):
	__defaultName = 'SEP_EN2_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_2(ComponentXY):
	__defaultName = 'SEP_EN2_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_3(ComponentXY):
	__defaultName = 'SEP_EN2_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_6(ComponentXY):
	__defaultName = 'SEP_EN2_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_8(ComponentXY):
	__defaultName = 'SEP_EN2_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.9, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_V2_1(ComponentXY):
	__defaultName = 'SEP_EN2_V2_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_S_0P5(ComponentXY):
	__defaultName = 'SEP_EN2_S_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_S_1(ComponentXY):
	__defaultName = 'SEP_EN2_S_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_S_2(ComponentXY):
	__defaultName = 'SEP_EN2_S_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_S_3(ComponentXY):
	__defaultName = 'SEP_EN2_S_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_S_4(ComponentXY):
	__defaultName = 'SEP_EN2_S_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_S_6(ComponentXY):
	__defaultName = 'SEP_EN2_S_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN2_S_8(ComponentXY):
	__defaultName = 'SEP_EN2_S_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.9, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN3_4(ComponentXY):
	__defaultName = 'SEP_EN3_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN3_1(ComponentXY):
	__defaultName = 'SEP_EN3_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN3_2(ComponentXY):
	__defaultName = 'SEP_EN3_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN3_3(ComponentXY):
	__defaultName = 'SEP_EN3_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EN3_6(ComponentXY):
	__defaultName = 'SEP_EN3_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.74, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_S_3(ComponentXY):
	__defaultName = 'SEP_EO2_S_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.1, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_0P5(ComponentXY):
	__defaultName = 'SEP_EO2_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_1(ComponentXY):
	__defaultName = 'SEP_EO2_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_1P5(ComponentXY):
	__defaultName = 'SEP_EO2_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_2(ComponentXY):
	__defaultName = 'SEP_EO2_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_3(ComponentXY):
	__defaultName = 'SEP_EO2_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_4(ComponentXY):
	__defaultName = 'SEP_EO2_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_6(ComponentXY):
	__defaultName = 'SEP_EO2_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_8(ComponentXY):
	__defaultName = 'SEP_EO2_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.76, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_S_0P5(ComponentXY):
	__defaultName = 'SEP_EO2_S_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_S_1(ComponentXY):
	__defaultName = 'SEP_EO2_S_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_S_2(ComponentXY):
	__defaultName = 'SEP_EO2_S_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_S_4(ComponentXY):
	__defaultName = 'SEP_EO2_S_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_S_6(ComponentXY):
	__defaultName = 'SEP_EO2_S_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO2_S_8(ComponentXY):
	__defaultName = 'SEP_EO2_S_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.2, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO3_4(ComponentXY):
	__defaultName = 'SEP_EO3_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.06, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO3_0P5(ComponentXY):
	__defaultName = 'SEP_EO3_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.68, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO3_1(ComponentXY):
	__defaultName = 'SEP_EO3_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO3_2(ComponentXY):
	__defaultName = 'SEP_EO3_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO3_3(ComponentXY):
	__defaultName = 'SEP_EO3_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_EO3_6(ComponentXY):
	__defaultName = 'SEP_EO3_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.88, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDAO22PQ_1(ComponentXY):
	__defaultName = 'SEP_FDAO22PQ_1'

	def __init__(self, name = __defaultName, in1='CK', in2='A1', in3='A2', in4='B1', in5='B2', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDAO22PQ_2(ComponentXY):
	__defaultName = 'SEP_FDAO22PQ_2'

	def __init__(self, name = __defaultName, in1='CK', in2='A1', in3='A2', in4='B1', in5='B2', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDAO22PQ_4(ComponentXY):
	__defaultName = 'SEP_FDAO22PQ_4'

	def __init__(self, name = __defaultName, in1='CK', in2='A1', in3='A2', in4='B1', in5='B2', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.22, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDNQ_1(ComponentXY):
	__defaultName = 'SEP_FDNQ_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDNQ_2(ComponentXY):
	__defaultName = 'SEP_FDNQ_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDNQ_4(ComponentXY):
	__defaultName = 'SEP_FDNQ_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDNRBQ_4(ComponentXY):
	__defaultName = 'SEP_FDNRBQ_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.64, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDNRBQ_1(ComponentXY):
	__defaultName = 'SEP_FDNRBQ_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDNRBQ_2(ComponentXY):
	__defaultName = 'SEP_FDNRBQ_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDNRBQ_V2_1(ComponentXY):
	__defaultName = 'SEP_FDNRBQ_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDNRBQ_V2_2(ComponentXY):
	__defaultName = 'SEP_FDNRBQ_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDNRBQ_V2_4(ComponentXY):
	__defaultName = 'SEP_FDNRBQ_V2_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDNRBSBQ_1(ComponentXY):
	__defaultName = 'SEP_FDNRBSBQ_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', in4='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDNRBSBQ_2(ComponentXY):
	__defaultName = 'SEP_FDNRBSBQ_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', in4='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDNRBSBQ_4(ComponentXY):
	__defaultName = 'SEP_FDNRBSBQ_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', in4='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPCBQ_1(ComponentXY):
	__defaultName = 'SEP_FDPCBQ_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RS', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPCBQ_2(ComponentXY):
	__defaultName = 'SEP_FDPCBQ_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RS', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPCBQ_4(ComponentXY):
	__defaultName = 'SEP_FDPCBQ_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RS', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPHQ_1(ComponentXY):
	__defaultName = 'SEP_FDPHQ_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='EN', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPHQ_2(ComponentXY):
	__defaultName = 'SEP_FDPHQ_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='EN', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPHRBSBQ_1(ComponentXY):
	__defaultName = 'SEP_FDPHRBSBQ_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='EN', in4='RD', in5='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPHRBSBQ_2(ComponentXY):
	__defaultName = 'SEP_FDPHRBSBQ_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='EN', in4='RD', in5='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.92, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPMQ_1(ComponentXY):
	__defaultName = 'SEP_FDPMQ_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D0', in3='D1', in4='S', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.22, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPMQ_2(ComponentXY):
	__defaultName = 'SEP_FDPMQ_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D0', in3='D1', in4='S', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPMQ_4(ComponentXY):
	__defaultName = 'SEP_FDPMQ_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D0', in3='D1', in4='S', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQ_1(ComponentXY):
	__defaultName = 'SEP_FDPQ_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQ_2(ComponentXY):
	__defaultName = 'SEP_FDPQ_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQ_4(ComponentXY):
	__defaultName = 'SEP_FDPQ_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQ_V2M_1(ComponentXY):
	__defaultName = 'SEP_FDPQ_V2M_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQ_V2M_2(ComponentXY):
	__defaultName = 'SEP_FDPQ_V2M_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQ_V2_1(ComponentXY):
	__defaultName = 'SEP_FDPQ_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.1, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQ_V2_2(ComponentXY):
	__defaultName = 'SEP_FDPQ_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQ_V2_4(ComponentXY):
	__defaultName = 'SEP_FDPQ_V2_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQB_1(ComponentXY):
	__defaultName = 'SEP_FDPQB_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='QN'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQB_1P5(ComponentXY):
	__defaultName = 'SEP_FDPQB_1P5'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='QN'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQB_2(ComponentXY):
	__defaultName = 'SEP_FDPQB_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='QN'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQB_3(ComponentXY):
	__defaultName = 'SEP_FDPQB_3'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='QN'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQB_4(ComponentXY):
	__defaultName = 'SEP_FDPQB_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='QN'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQB_V2_1(ComponentXY):
	__defaultName = 'SEP_FDPQB_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='QN'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQB_V2_2(ComponentXY):
	__defaultName = 'SEP_FDPQB_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='QN'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.1, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPQB_V2_4(ComponentXY):
	__defaultName = 'SEP_FDPQB_V2_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', out1='QN'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPRBQ_1(ComponentXY):
	__defaultName = 'SEP_FDPRBQ_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPRBQ_2(ComponentXY):
	__defaultName = 'SEP_FDPRBQ_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPRBQ_4(ComponentXY):
	__defaultName = 'SEP_FDPRBQ_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.64, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPRBQ_V2_1(ComponentXY):
	__defaultName = 'SEP_FDPRBQ_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPRBQ_V2_2(ComponentXY):
	__defaultName = 'SEP_FDPRBQ_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPRBQ_V2_4(ComponentXY):
	__defaultName = 'SEP_FDPRBQ_V2_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPRBSBQ_1(ComponentXY):
	__defaultName = 'SEP_FDPRBSBQ_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', in4='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPRBSBQ_2(ComponentXY):
	__defaultName = 'SEP_FDPRBSBQ_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', in4='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPRBSBQ_4(ComponentXY):
	__defaultName = 'SEP_FDPRBSBQ_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='RD', in4='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.06, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPSBQ_1(ComponentXY):
	__defaultName = 'SEP_FDPSBQ_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPSBQ_2(ComponentXY):
	__defaultName = 'SEP_FDPSBQ_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FDPSBQ_4(ComponentXY):
	__defaultName = 'SEP_FDPSBQ_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDAO22PQ_V2_1(ComponentXY):
	__defaultName = 'SEP_FSDAO22PQ_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='A1', in3='A2', in4='B1', in5='B2', in6='SI', in7='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Input(in7) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.64, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDAO22PQ_V2_2(ComponentXY):
	__defaultName = 'SEP_FSDAO22PQ_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='A1', in3='A2', in4='B1', in5='B2', in6='SI', in7='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Input(in7) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDAO22PQ_V2_4(ComponentXY):
	__defaultName = 'SEP_FSDAO22PQ_V2_4'

	def __init__(self, name = __defaultName, in1='CK', in2='A1', in3='A2', in4='B1', in5='B2', in6='SI', in7='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Input(in7) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.34, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDAO22PQO_1(ComponentXY):
	__defaultName = 'SEP_FSDAO22PQO_1'

	def __init__(self, name = __defaultName, in1='CK', in2='A1', in3='A2', in4='B1', in5='B2', in6='SI', in7='SE', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Input(in7) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.2, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDAO22PQO_2(ComponentXY):
	__defaultName = 'SEP_FSDAO22PQO_2'

	def __init__(self, name = __defaultName, in1='CK', in2='A1', in3='A2', in4='B1', in5='B2', in6='SI', in7='SE', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Input(in7) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.34, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDAO22PQO_4(ComponentXY):
	__defaultName = 'SEP_FSDAO22PQO_4'

	def __init__(self, name = __defaultName, in1='CK', in2='A1', in3='A2', in4='B1', in5='B2', in6='SI', in7='SE', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Input(in7) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.9, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDNQ_V2_1(ComponentXY):
	__defaultName = 'SEP_FSDNQ_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDNQ_V2_2(ComponentXY):
	__defaultName = 'SEP_FSDNQ_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDNQ_V2_4(ComponentXY):
	__defaultName = 'SEP_FSDNQ_V2_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDNQO_1(ComponentXY):
	__defaultName = 'SEP_FSDNQO_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDNQO_2(ComponentXY):
	__defaultName = 'SEP_FSDNQO_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDNQO_4(ComponentXY):
	__defaultName = 'SEP_FSDNQO_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDNRBQ_V2_1(ComponentXY):
	__defaultName = 'SEP_FSDNRBQ_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDNRBQ_V2_2(ComponentXY):
	__defaultName = 'SEP_FSDNRBQ_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.22, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDNRBQ_V2_4(ComponentXY):
	__defaultName = 'SEP_FSDNRBQ_V2_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDNRBQO_1(ComponentXY):
	__defaultName = 'SEP_FSDNRBQO_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.64, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDNRBQO_2(ComponentXY):
	__defaultName = 'SEP_FSDNRBQO_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDNRBQO_4(ComponentXY):
	__defaultName = 'SEP_FSDNRBQO_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.06, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDNRBSBQO_1(ComponentXY):
	__defaultName = 'SEP_FSDNRBSBQO_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', in6='SD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDNRBSBQO_2(ComponentXY):
	__defaultName = 'SEP_FSDNRBSBQO_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', in6='SD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.92, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDNRBSBQO_4(ComponentXY):
	__defaultName = 'SEP_FSDNRBSBQO_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', in6='SD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.34, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPC1BQ_V2_1(ComponentXY):
	__defaultName = 'SEP_FSDPC1BQ_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RS', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPC1BQ_V2_2(ComponentXY):
	__defaultName = 'SEP_FSDPC1BQ_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RS', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPC1BQ_V2_3(ComponentXY):
	__defaultName = 'SEP_FSDPC1BQ_V2_3'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RS', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPC1BQ_V2_4(ComponentXY):
	__defaultName = 'SEP_FSDPC1BQ_V2_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RS', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.22, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPC1BQO_1(ComponentXY):
	__defaultName = 'SEP_FSDPC1BQO_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RS', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPC1BQO_2(ComponentXY):
	__defaultName = 'SEP_FSDPC1BQO_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RS', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPC1BQO_4(ComponentXY):
	__defaultName = 'SEP_FSDPC1BQO_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RS', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPC1BQO_8(ComponentXY):
	__defaultName = 'SEP_FSDPC1BQO_8'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RS', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.2, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPHQ_V2_1(ComponentXY):
	__defaultName = 'SEP_FSDPHQ_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='EN', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.92, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPHQ_V2_2(ComponentXY):
	__defaultName = 'SEP_FSDPHQ_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='EN', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.92, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPHQO_1(ComponentXY):
	__defaultName = 'SEP_FSDPHQO_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='EN', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.76, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPHQO_2(ComponentXY):
	__defaultName = 'SEP_FSDPHQO_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='EN', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.9, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPHRBQ_1(ComponentXY):
	__defaultName = 'SEP_FSDPHRBQ_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='EN', in6='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.76, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPHRBQ_2(ComponentXY):
	__defaultName = 'SEP_FSDPHRBQ_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='EN', in6='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.9, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPHRBQO_1(ComponentXY):
	__defaultName = 'SEP_FSDPHRBQO_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='EN', in6='RD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.9, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPHRBQO_2(ComponentXY):
	__defaultName = 'SEP_FSDPHRBQO_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='EN', in6='RD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(5.04, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPHRBSBQ_V2_1(ComponentXY):
	__defaultName = 'SEP_FSDPHRBSBQ_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='EN', in6='RD', in7='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Input(in7) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPHRBSBQ_V2_2(ComponentXY):
	__defaultName = 'SEP_FSDPHRBSBQ_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='EN', in6='RD', in7='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Input(in7) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPHRBSBQO_1(ComponentXY):
	__defaultName = 'SEP_FSDPHRBSBQO_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='EN', in6='RD', in7='SD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Input(in7) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(5.18, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPHRBSBQO_2(ComponentXY):
	__defaultName = 'SEP_FSDPHRBSBQO_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='EN', in6='RD', in7='SD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Input(in7) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(5.32, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPMQ_V2_1(ComponentXY):
	__defaultName = 'SEP_FSDPMQ_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D0', in3='D1', in4='S', in5='SI', in6='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPMQ_V2_2(ComponentXY):
	__defaultName = 'SEP_FSDPMQ_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D0', in3='D1', in4='S', in5='SI', in6='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPMQ_V2_4(ComponentXY):
	__defaultName = 'SEP_FSDPMQ_V2_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D0', in3='D1', in4='S', in5='SI', in6='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.06, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPMQO_1(ComponentXY):
	__defaultName = 'SEP_FSDPMQO_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D0', in3='D1', in4='S', in5='SI', in6='SE', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.2, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPMQO_2(ComponentXY):
	__defaultName = 'SEP_FSDPMQO_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D0', in3='D1', in4='S', in5='SI', in6='SE', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.34, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPMQO_4(ComponentXY):
	__defaultName = 'SEP_FSDPMQO_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D0', in3='D1', in4='S', in5='SI', in6='SE', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(5.88, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQ_D_0P5(ComponentXY):
	__defaultName = 'SEP_FSDPQ_D_0P5'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQ_D_1(ComponentXY):
	__defaultName = 'SEP_FSDPQ_D_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQ_D_1P5(ComponentXY):
	__defaultName = 'SEP_FSDPQ_D_1P5'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQ_D_2(ComponentXY):
	__defaultName = 'SEP_FSDPQ_D_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQ_D_3(ComponentXY):
	__defaultName = 'SEP_FSDPQ_D_3'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQ_D_4(ComponentXY):
	__defaultName = 'SEP_FSDPQ_D_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQ_V2_0P5(ComponentXY):
	__defaultName = 'SEP_FSDPQ_V2_0P5'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQ_V2_1(ComponentXY):
	__defaultName = 'SEP_FSDPQ_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQ_V2_1P5(ComponentXY):
	__defaultName = 'SEP_FSDPQ_V2_1P5'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQ_V2_2(ComponentXY):
	__defaultName = 'SEP_FSDPQ_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQ_V2_3(ComponentXY):
	__defaultName = 'SEP_FSDPQ_V2_3'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQ_V2_4(ComponentXY):
	__defaultName = 'SEP_FSDPQ_V2_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQB_V2_1(ComponentXY):
	__defaultName = 'SEP_FSDPQB_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='QN'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQB_V2_2(ComponentXY):
	__defaultName = 'SEP_FSDPQB_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='QN'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQB_V2_4(ComponentXY):
	__defaultName = 'SEP_FSDPQB_V2_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='QN'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.22, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQBO_1(ComponentXY):
	__defaultName = 'SEP_FSDPQBO_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='QN', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQBO_2(ComponentXY):
	__defaultName = 'SEP_FSDPQBO_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='QN', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQBO_4(ComponentXY):
	__defaultName = 'SEP_FSDPQBO_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='QN', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.06, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQBO_8(ComponentXY):
	__defaultName = 'SEP_FSDPQBO_8'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='QN', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(6.02, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQO_1(ComponentXY):
	__defaultName = 'SEP_FSDPQO_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.22, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQO_2(ComponentXY):
	__defaultName = 'SEP_FSDPQO_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQO_3(ComponentXY):
	__defaultName = 'SEP_FSDPQO_3'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQO_4(ComponentXY):
	__defaultName = 'SEP_FSDPQO_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.64, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQO_6(ComponentXY):
	__defaultName = 'SEP_FSDPQO_6'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.92, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPQO_8(ComponentXY):
	__defaultName = 'SEP_FSDPQO_8'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.76, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_D_0P5(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_D_0P5'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_D_1(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_D_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_D_1P5(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_D_1P5'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_D_2(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_D_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_D_3(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_D_3'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.22, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_D_4(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_D_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.22, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_V2_1(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_V2_1P5(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_V2_1P5'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.22, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_V2_2(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.22, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_V2_3(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_V2_3'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_V2_4(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_V2_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_V2_6(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_V2_6'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQ_V2_8(ComponentXY):
	__defaultName = 'SEP_FSDPRBQ_V2_8'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.34, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQO_1(ComponentXY):
	__defaultName = 'SEP_FSDPRBQO_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.64, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQO_2(ComponentXY):
	__defaultName = 'SEP_FSDPRBQO_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQO_3(ComponentXY):
	__defaultName = 'SEP_FSDPRBQO_3'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(3.92, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQO_4(ComponentXY):
	__defaultName = 'SEP_FSDPRBQO_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.06, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBQO_8(ComponentXY):
	__defaultName = 'SEP_FSDPRBQO_8'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(5.18, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBSBQ_V2_1(ComponentXY):
	__defaultName = 'SEP_FSDPRBSBQ_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', in6='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBSBQ_V2_2(ComponentXY):
	__defaultName = 'SEP_FSDPRBSBQ_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', in6='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBSBQ_V2_4(ComponentXY):
	__defaultName = 'SEP_FSDPRBSBQ_V2_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', in6='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBSBQO_1(ComponentXY):
	__defaultName = 'SEP_FSDPRBSBQO_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', in6='SD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.2, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBSBQO_2(ComponentXY):
	__defaultName = 'SEP_FSDPRBSBQO_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', in6='SD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.2, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPRBSBQO_4(ComponentXY):
	__defaultName = 'SEP_FSDPRBSBQO_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='RD', in6='SD', out1='Q', out2='SO'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.add_pin(Output(out2) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPSBQ_V2_1(ComponentXY):
	__defaultName = 'SEP_FSDPSBQ_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPSBQ_V2_2(ComponentXY):
	__defaultName = 'SEP_FSDPSBQ_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPSBQ_V2_4(ComponentXY):
	__defaultName = 'SEP_FSDPSBQ_V2_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='SD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.64, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPTQ_V2_1(ComponentXY):
	__defaultName = 'SEP_FSDPTQ_V2_1'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='SS', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPTQ_V2_2(ComponentXY):
	__defaultName = 'SEP_FSDPTQ_V2_2'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='SS', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.22, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_FSDPTQ_V2_4(ComponentXY):
	__defaultName = 'SEP_FSDPTQ_V2_4'

	def __init__(self, name = __defaultName, in1='CK', in2='D', in3='SI', in4='SE', in5='SS', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_0P5(ComponentXY):
	__defaultName = 'SEP_INV_0P5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.28, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_0P65(ComponentXY):
	__defaultName = 'SEP_INV_0P65'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.28, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_0P8(ComponentXY):
	__defaultName = 'SEP_INV_0P8'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.28, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_1(ComponentXY):
	__defaultName = 'SEP_INV_1'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.28, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_10(ComponentXY):
	__defaultName = 'SEP_INV_10'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_12(ComponentXY):
	__defaultName = 'SEP_INV_12'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_15(ComponentXY):
	__defaultName = 'SEP_INV_15'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_16(ComponentXY):
	__defaultName = 'SEP_INV_16'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_18(ComponentXY):
	__defaultName = 'SEP_INV_18'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_1P25(ComponentXY):
	__defaultName = 'SEP_INV_1P25'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_1P5(ComponentXY):
	__defaultName = 'SEP_INV_1P5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_2(ComponentXY):
	__defaultName = 'SEP_INV_2'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_20(ComponentXY):
	__defaultName = 'SEP_INV_20'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_24(ComponentXY):
	__defaultName = 'SEP_INV_24'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_3(ComponentXY):
	__defaultName = 'SEP_INV_3'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_32(ComponentXY):
	__defaultName = 'SEP_INV_32'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_4(ComponentXY):
	__defaultName = 'SEP_INV_4'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_5(ComponentXY):
	__defaultName = 'SEP_INV_5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_6(ComponentXY):
	__defaultName = 'SEP_INV_6'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_8(ComponentXY):
	__defaultName = 'SEP_INV_8'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_9(ComponentXY):
	__defaultName = 'SEP_INV_9'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_0P5(ComponentXY):
	__defaultName = 'SEP_INV_S_0P5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.28, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_0P65(ComponentXY):
	__defaultName = 'SEP_INV_S_0P65'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.28, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_0P8(ComponentXY):
	__defaultName = 'SEP_INV_S_0P8'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.28, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_1(ComponentXY):
	__defaultName = 'SEP_INV_S_1'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.28, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_10(ComponentXY):
	__defaultName = 'SEP_INV_S_10'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_12(ComponentXY):
	__defaultName = 'SEP_INV_S_12'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_16(ComponentXY):
	__defaultName = 'SEP_INV_S_16'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_1P25(ComponentXY):
	__defaultName = 'SEP_INV_S_1P25'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_1P5(ComponentXY):
	__defaultName = 'SEP_INV_S_1P5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_2(ComponentXY):
	__defaultName = 'SEP_INV_S_2'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_20(ComponentXY):
	__defaultName = 'SEP_INV_S_20'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_24(ComponentXY):
	__defaultName = 'SEP_INV_S_24'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_2P5(ComponentXY):
	__defaultName = 'SEP_INV_S_2P5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_3(ComponentXY):
	__defaultName = 'SEP_INV_S_3'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_32(ComponentXY):
	__defaultName = 'SEP_INV_S_32'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_4(ComponentXY):
	__defaultName = 'SEP_INV_S_4'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_5(ComponentXY):
	__defaultName = 'SEP_INV_S_5'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_6(ComponentXY):
	__defaultName = 'SEP_INV_S_6'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_7(ComponentXY):
	__defaultName = 'SEP_INV_S_7'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_8(ComponentXY):
	__defaultName = 'SEP_INV_S_8'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_INV_S_9(ComponentXY):
	__defaultName = 'SEP_INV_S_9'

	def __init__(self, name = __defaultName, in1='A', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDNQ_4(ComponentXY):
	__defaultName = 'SEP_LDNQ_4'

	def __init__(self, name = __defaultName, in1='G', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDNQ_6(ComponentXY):
	__defaultName = 'SEP_LDNQ_6'

	def __init__(self, name = __defaultName, in1='G', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDNQ_8(ComponentXY):
	__defaultName = 'SEP_LDNQ_8'

	def __init__(self, name = __defaultName, in1='G', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDNQ_1(ComponentXY):
	__defaultName = 'SEP_LDNQ_1'

	def __init__(self, name = __defaultName, in1='G', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDNQ_2(ComponentXY):
	__defaultName = 'SEP_LDNQ_2'

	def __init__(self, name = __defaultName, in1='G', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDNRBQ_4(ComponentXY):
	__defaultName = 'SEP_LDNRBQ_4'

	def __init__(self, name = __defaultName, in1='G', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDNRBQ_6(ComponentXY):
	__defaultName = 'SEP_LDNRBQ_6'

	def __init__(self, name = __defaultName, in1='G', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDNRBQ_1(ComponentXY):
	__defaultName = 'SEP_LDNRBQ_1'

	def __init__(self, name = __defaultName, in1='G', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDNRBQ_2(ComponentXY):
	__defaultName = 'SEP_LDNRBQ_2'

	def __init__(self, name = __defaultName, in1='G', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.68, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDNRBQ_8(ComponentXY):
	__defaultName = 'SEP_LDNRBQ_8'

	def __init__(self, name = __defaultName, in1='G', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.22, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDPQ_4(ComponentXY):
	__defaultName = 'SEP_LDPQ_4'

	def __init__(self, name = __defaultName, in1='G', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDPQ_1(ComponentXY):
	__defaultName = 'SEP_LDPQ_1'

	def __init__(self, name = __defaultName, in1='G', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDPQ_2(ComponentXY):
	__defaultName = 'SEP_LDPQ_2'

	def __init__(self, name = __defaultName, in1='G', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDPQ_6(ComponentXY):
	__defaultName = 'SEP_LDPQ_6'

	def __init__(self, name = __defaultName, in1='G', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDPQ_8(ComponentXY):
	__defaultName = 'SEP_LDPQ_8'

	def __init__(self, name = __defaultName, in1='G', in2='D', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDPRBQ_1(ComponentXY):
	__defaultName = 'SEP_LDPRBQ_1'

	def __init__(self, name = __defaultName, in1='G', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDPRBQ_2(ComponentXY):
	__defaultName = 'SEP_LDPRBQ_2'

	def __init__(self, name = __defaultName, in1='G', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.68, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDPRBQ_4(ComponentXY):
	__defaultName = 'SEP_LDPRBQ_4'

	def __init__(self, name = __defaultName, in1='G', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDPRBQ_6(ComponentXY):
	__defaultName = 'SEP_LDPRBQ_6'

	def __init__(self, name = __defaultName, in1='G', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_LDPRBQ_8(ComponentXY):
	__defaultName = 'SEP_LDPRBQ_8'

	def __init__(self, name = __defaultName, in1='G', in2='D', in3='RD', out1='Q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.36, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MAJ3_4(ComponentXY):
	__defaultName = 'SEP_MAJ3_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.1, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MAJ3_0P5(ComponentXY):
	__defaultName = 'SEP_MAJ3_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MAJ3_1(ComponentXY):
	__defaultName = 'SEP_MAJ3_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MAJ3_1P5(ComponentXY):
	__defaultName = 'SEP_MAJ3_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MAJ3_2(ComponentXY):
	__defaultName = 'SEP_MAJ3_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MAJI3_2(ComponentXY):
	__defaultName = 'SEP_MAJI3_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MAJI3_4(ComponentXY):
	__defaultName = 'SEP_MAJI3_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MAJI3_8(ComponentXY):
	__defaultName = 'SEP_MAJI3_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.74, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MAJI3_1(ComponentXY):
	__defaultName = 'SEP_MAJI3_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_0P5(ComponentXY):
	__defaultName = 'SEP_MUX2_0P5'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_1(ComponentXY):
	__defaultName = 'SEP_MUX2_1'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_12(ComponentXY):
	__defaultName = 'SEP_MUX2_12'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.6, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_16(ComponentXY):
	__defaultName = 'SEP_MUX2_16'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(7.28, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_1P5(ComponentXY):
	__defaultName = 'SEP_MUX2_1P5'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_2(ComponentXY):
	__defaultName = 'SEP_MUX2_2'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_4(ComponentXY):
	__defaultName = 'SEP_MUX2_4'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.1, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_6(ComponentXY):
	__defaultName = 'SEP_MUX2_6'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_8(ComponentXY):
	__defaultName = 'SEP_MUX2_8'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.92, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_S_0P5(ComponentXY):
	__defaultName = 'SEP_MUX2_S_0P5'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_S_1(ComponentXY):
	__defaultName = 'SEP_MUX2_S_1'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_S_1P5(ComponentXY):
	__defaultName = 'SEP_MUX2_S_1P5'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_S_2(ComponentXY):
	__defaultName = 'SEP_MUX2_S_2'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_S_4(ComponentXY):
	__defaultName = 'SEP_MUX2_S_4'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.1, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_S_6(ComponentXY):
	__defaultName = 'SEP_MUX2_S_6'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2_S_8(ComponentXY):
	__defaultName = 'SEP_MUX2_S_8'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.92, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2AN2_MG_0P75(ComponentXY):
	__defaultName = 'SEP_MUX2AN2_MG_0P75'

	def __init__(self, name = __defaultName, in1='D0A1', in2='D0A2', in3='D1', in4='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2AN2_MG_1(ComponentXY):
	__defaultName = 'SEP_MUX2AN2_MG_1'

	def __init__(self, name = __defaultName, in1='D0A1', in2='D0A2', in3='D1', in4='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2AN2_MG_2(ComponentXY):
	__defaultName = 'SEP_MUX2AN2_MG_2'

	def __init__(self, name = __defaultName, in1='D0A1', in2='D0A2', in3='D1', in4='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUX2AN2_MG_3(ComponentXY):
	__defaultName = 'SEP_MUX2AN2_MG_3'

	def __init__(self, name = __defaultName, in1='D0A1', in2='D0A2', in3='D1', in4='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_MG_1P5(ComponentXY):
	__defaultName = 'SEP_MUXI2_MG_1P5'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_2(ComponentXY):
	__defaultName = 'SEP_MUXI2_2'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_S_0P5(ComponentXY):
	__defaultName = 'SEP_MUXI2_S_0P5'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_S_1(ComponentXY):
	__defaultName = 'SEP_MUXI2_S_1'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_S_2(ComponentXY):
	__defaultName = 'SEP_MUXI2_S_2'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_S_3(ComponentXY):
	__defaultName = 'SEP_MUXI2_S_3'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_S_4(ComponentXY):
	__defaultName = 'SEP_MUXI2_S_4'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_S_6(ComponentXY):
	__defaultName = 'SEP_MUXI2_S_6'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.92, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_S_8(ComponentXY):
	__defaultName = 'SEP_MUXI2_S_8'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.9, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_UG_1(ComponentXY):
	__defaultName = 'SEP_MUXI2_UG_1'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_MG_0P5(ComponentXY):
	__defaultName = 'SEP_MUXI2_MG_0P5'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_MG_0P75(ComponentXY):
	__defaultName = 'SEP_MUXI2_MG_0P75'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_MG_1(ComponentXY):
	__defaultName = 'SEP_MUXI2_MG_1'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_MG_12(ComponentXY):
	__defaultName = 'SEP_MUXI2_MG_12'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(7.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_MG_2(ComponentXY):
	__defaultName = 'SEP_MUXI2_MG_2'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_MG_3(ComponentXY):
	__defaultName = 'SEP_MUXI2_MG_3'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_MG_4(ComponentXY):
	__defaultName = 'SEP_MUXI2_MG_4'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.8, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_MG_6(ComponentXY):
	__defaultName = 'SEP_MUXI2_MG_6'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.92, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_MUXI2_MG_9(ComponentXY):
	__defaultName = 'SEP_MUXI2_MG_9'

	def __init__(self, name = __defaultName, in1='D0', in2='D1', in3='S', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.88, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_10(ComponentXY):
	__defaultName = 'SEP_ND2_10'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_12(ComponentXY):
	__defaultName = 'SEP_ND2_12'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_16(ComponentXY):
	__defaultName = 'SEP_ND2_16'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_24(ComponentXY):
	__defaultName = 'SEP_ND2_24'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.86, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_4(ComponentXY):
	__defaultName = 'SEP_ND2_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_5(ComponentXY):
	__defaultName = 'SEP_ND2_5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_6(ComponentXY):
	__defaultName = 'SEP_ND2_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_8(ComponentXY):
	__defaultName = 'SEP_ND2_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_G_1P5(ComponentXY):
	__defaultName = 'SEP_ND2_G_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_G_2(ComponentXY):
	__defaultName = 'SEP_ND2_G_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_G_3(ComponentXY):
	__defaultName = 'SEP_ND2_G_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_G_4(ComponentXY):
	__defaultName = 'SEP_ND2_G_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_0P5(ComponentXY):
	__defaultName = 'SEP_ND2_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_0P8(ComponentXY):
	__defaultName = 'SEP_ND2_0P8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_1(ComponentXY):
	__defaultName = 'SEP_ND2_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_1P5(ComponentXY):
	__defaultName = 'SEP_ND2_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_2(ComponentXY):
	__defaultName = 'SEP_ND2_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_3(ComponentXY):
	__defaultName = 'SEP_ND2_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_0P5(ComponentXY):
	__defaultName = 'SEP_ND2_S_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_0P65(ComponentXY):
	__defaultName = 'SEP_ND2_S_0P65'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_0P8(ComponentXY):
	__defaultName = 'SEP_ND2_S_0P8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_1(ComponentXY):
	__defaultName = 'SEP_ND2_S_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_10(ComponentXY):
	__defaultName = 'SEP_ND2_S_10'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_12(ComponentXY):
	__defaultName = 'SEP_ND2_S_12'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_16(ComponentXY):
	__defaultName = 'SEP_ND2_S_16'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_1P5(ComponentXY):
	__defaultName = 'SEP_ND2_S_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_2(ComponentXY):
	__defaultName = 'SEP_ND2_S_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_24(ComponentXY):
	__defaultName = 'SEP_ND2_S_24'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.9, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_3(ComponentXY):
	__defaultName = 'SEP_ND2_S_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_4(ComponentXY):
	__defaultName = 'SEP_ND2_S_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_5(ComponentXY):
	__defaultName = 'SEP_ND2_S_5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_6(ComponentXY):
	__defaultName = 'SEP_ND2_S_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_7(ComponentXY):
	__defaultName = 'SEP_ND2_S_7'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_S_8(ComponentXY):
	__defaultName = 'SEP_ND2_S_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2_G_1(ComponentXY):
	__defaultName = 'SEP_ND2_G_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_10(ComponentXY):
	__defaultName = 'SEP_ND2B_10'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.64, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_16(ComponentXY):
	__defaultName = 'SEP_ND2B_16'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.74, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_2(ComponentXY):
	__defaultName = 'SEP_ND2B_2'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_3(ComponentXY):
	__defaultName = 'SEP_ND2B_3'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_4(ComponentXY):
	__defaultName = 'SEP_ND2B_4'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_6(ComponentXY):
	__defaultName = 'SEP_ND2B_6'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_8(ComponentXY):
	__defaultName = 'SEP_ND2B_8'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_MM_8(ComponentXY):
	__defaultName = 'SEP_ND2B_MM_8'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_V1_2(ComponentXY):
	__defaultName = 'SEP_ND2B_V1_2'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_V1DG_16(ComponentXY):
	__defaultName = 'SEP_ND2B_V1DG_16'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.18, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_V1DG_2(ComponentXY):
	__defaultName = 'SEP_ND2B_V1DG_2'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_V1DG_4(ComponentXY):
	__defaultName = 'SEP_ND2B_V1DG_4'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_V1DG_8(ComponentXY):
	__defaultName = 'SEP_ND2B_V1DG_8'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_V1DG_1(ComponentXY):
	__defaultName = 'SEP_ND2B_V1DG_1'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_0P5(ComponentXY):
	__defaultName = 'SEP_ND2B_0P5'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_1(ComponentXY):
	__defaultName = 'SEP_ND2B_1'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_V1U_1(ComponentXY):
	__defaultName = 'SEP_ND2B_V1U_1'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_MM_0P5(ComponentXY):
	__defaultName = 'SEP_ND2B_MM_0P5'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_MM_1(ComponentXY):
	__defaultName = 'SEP_ND2B_MM_1'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_MM_2(ComponentXY):
	__defaultName = 'SEP_ND2B_MM_2'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND2B_MM_4(ComponentXY):
	__defaultName = 'SEP_ND2B_MM_4'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3_2(ComponentXY):
	__defaultName = 'SEP_ND3_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3_4(ComponentXY):
	__defaultName = 'SEP_ND3_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3_6(ComponentXY):
	__defaultName = 'SEP_ND3_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3_8(ComponentXY):
	__defaultName = 'SEP_ND3_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3_0P5(ComponentXY):
	__defaultName = 'SEP_ND3_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3_0P75(ComponentXY):
	__defaultName = 'SEP_ND3_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3_1(ComponentXY):
	__defaultName = 'SEP_ND3_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3_16(ComponentXY):
	__defaultName = 'SEP_ND3_16'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.44, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3_3(ComponentXY):
	__defaultName = 'SEP_ND3_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3B_V1DG_2(ComponentXY):
	__defaultName = 'SEP_ND3B_V1DG_2'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3B_V1DG_4(ComponentXY):
	__defaultName = 'SEP_ND3B_V1DG_4'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3B_V1DG_8(ComponentXY):
	__defaultName = 'SEP_ND3B_V1DG_8'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3B_2(ComponentXY):
	__defaultName = 'SEP_ND3B_2'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3B_4(ComponentXY):
	__defaultName = 'SEP_ND3B_4'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.1, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3B_8(ComponentXY):
	__defaultName = 'SEP_ND3B_8'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.06, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3B_V1DG_1(ComponentXY):
	__defaultName = 'SEP_ND3B_V1DG_1'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3B_0P5(ComponentXY):
	__defaultName = 'SEP_ND3B_0P5'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND3B_1(ComponentXY):
	__defaultName = 'SEP_ND3B_1'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_1P5(ComponentXY):
	__defaultName = 'SEP_ND4_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_2(ComponentXY):
	__defaultName = 'SEP_ND4_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_4(ComponentXY):
	__defaultName = 'SEP_ND4_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_MM_1P5(ComponentXY):
	__defaultName = 'SEP_ND4_MM_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_MM_8(ComponentXY):
	__defaultName = 'SEP_ND4_MM_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_0P5(ComponentXY):
	__defaultName = 'SEP_ND4_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_0P75(ComponentXY):
	__defaultName = 'SEP_ND4_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_1(ComponentXY):
	__defaultName = 'SEP_ND4_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_12(ComponentXY):
	__defaultName = 'SEP_ND4_12'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.58, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_16(ComponentXY):
	__defaultName = 'SEP_ND4_16'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(8.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_8(ComponentXY):
	__defaultName = 'SEP_ND4_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.34, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_MM_0P5(ComponentXY):
	__defaultName = 'SEP_ND4_MM_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_MM_1(ComponentXY):
	__defaultName = 'SEP_ND4_MM_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_MM_2(ComponentXY):
	__defaultName = 'SEP_ND4_MM_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.68, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_MM_3(ComponentXY):
	__defaultName = 'SEP_ND4_MM_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.1, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4_MM_4(ComponentXY):
	__defaultName = 'SEP_ND4_MM_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.1, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4B_2(ComponentXY):
	__defaultName = 'SEP_ND4B_2'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', in4='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4B_4(ComponentXY):
	__defaultName = 'SEP_ND4B_4'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', in4='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4B_1(ComponentXY):
	__defaultName = 'SEP_ND4B_1'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', in4='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4BB_2(ComponentXY):
	__defaultName = 'SEP_ND4BB_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4BB_4(ComponentXY):
	__defaultName = 'SEP_ND4BB_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4BB_0P5(ComponentXY):
	__defaultName = 'SEP_ND4BB_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4BB_0P75(ComponentXY):
	__defaultName = 'SEP_ND4BB_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4BB_1(ComponentXY):
	__defaultName = 'SEP_ND4BB_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_ND4BB_3(ComponentXY):
	__defaultName = 'SEP_ND4BB_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_4(ComponentXY):
	__defaultName = 'SEP_NR2_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_6(ComponentXY):
	__defaultName = 'SEP_NR2_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_8(ComponentXY):
	__defaultName = 'SEP_NR2_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_S_1P5(ComponentXY):
	__defaultName = 'SEP_NR2_S_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_S_2(ComponentXY):
	__defaultName = 'SEP_NR2_S_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_S_3(ComponentXY):
	__defaultName = 'SEP_NR2_S_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_G_12(ComponentXY):
	__defaultName = 'SEP_NR2_G_12'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_G_16(ComponentXY):
	__defaultName = 'SEP_NR2_G_16'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_G_1P5(ComponentXY):
	__defaultName = 'SEP_NR2_G_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_G_2(ComponentXY):
	__defaultName = 'SEP_NR2_G_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_0P5(ComponentXY):
	__defaultName = 'SEP_NR2_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_1(ComponentXY):
	__defaultName = 'SEP_NR2_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_1P5(ComponentXY):
	__defaultName = 'SEP_NR2_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_2(ComponentXY):
	__defaultName = 'SEP_NR2_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_3(ComponentXY):
	__defaultName = 'SEP_NR2_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_S_0P5(ComponentXY):
	__defaultName = 'SEP_NR2_S_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_S_0P65(ComponentXY):
	__defaultName = 'SEP_NR2_S_0P65'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_S_0P8(ComponentXY):
	__defaultName = 'SEP_NR2_S_0P8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_S_1(ComponentXY):
	__defaultName = 'SEP_NR2_S_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_S_16(ComponentXY):
	__defaultName = 'SEP_NR2_S_16'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.78, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_S_20(ComponentXY):
	__defaultName = 'SEP_NR2_S_20'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_S_4(ComponentXY):
	__defaultName = 'SEP_NR2_S_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_S_5(ComponentXY):
	__defaultName = 'SEP_NR2_S_5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_S_6(ComponentXY):
	__defaultName = 'SEP_NR2_S_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_S_8(ComponentXY):
	__defaultName = 'SEP_NR2_S_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_G_0P5(ComponentXY):
	__defaultName = 'SEP_NR2_G_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_G_0P8(ComponentXY):
	__defaultName = 'SEP_NR2_G_0P8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_G_1(ComponentXY):
	__defaultName = 'SEP_NR2_G_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.42, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_G_3(ComponentXY):
	__defaultName = 'SEP_NR2_G_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_G_4(ComponentXY):
	__defaultName = 'SEP_NR2_G_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_G_5(ComponentXY):
	__defaultName = 'SEP_NR2_G_5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_G_6(ComponentXY):
	__defaultName = 'SEP_NR2_G_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2_G_8(ComponentXY):
	__defaultName = 'SEP_NR2_G_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2B_16(ComponentXY):
	__defaultName = 'SEP_NR2B_16'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.74, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2B_4(ComponentXY):
	__defaultName = 'SEP_NR2B_4'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2B_6(ComponentXY):
	__defaultName = 'SEP_NR2B_6'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2B_8(ComponentXY):
	__defaultName = 'SEP_NR2B_8'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2XB_2(ComponentXY):
	__defaultName = 'SEP_NR2XB_2'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2B_V1DG_2(ComponentXY):
	__defaultName = 'SEP_NR2B_V1DG_2'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2B_V1DG_3(ComponentXY):
	__defaultName = 'SEP_NR2B_V1DG_3'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2B_V1DG_4(ComponentXY):
	__defaultName = 'SEP_NR2B_V1DG_4'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2XB_U_1(ComponentXY):
	__defaultName = 'SEP_NR2XB_U_1'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2B_V1DG_1(ComponentXY):
	__defaultName = 'SEP_NR2B_V1DG_1'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2B_0P5(ComponentXY):
	__defaultName = 'SEP_NR2B_0P5'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2B_1(ComponentXY):
	__defaultName = 'SEP_NR2B_1'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2B_1P5(ComponentXY):
	__defaultName = 'SEP_NR2B_1P5'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2B_2(ComponentXY):
	__defaultName = 'SEP_NR2B_2'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR2B_3(ComponentXY):
	__defaultName = 'SEP_NR2B_3'

	def __init__(self, name = __defaultName, in1='A', in2='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_2(ComponentXY):
	__defaultName = 'SEP_NR3_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_4(ComponentXY):
	__defaultName = 'SEP_NR3_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_8(ComponentXY):
	__defaultName = 'SEP_NR3_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_G_12(ComponentXY):
	__defaultName = 'SEP_NR3_G_12'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.18, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_G_16(ComponentXY):
	__defaultName = 'SEP_NR3_G_16'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.86, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_G_1P25(ComponentXY):
	__defaultName = 'SEP_NR3_G_1P25'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_G_1P5(ComponentXY):
	__defaultName = 'SEP_NR3_G_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_G_2(ComponentXY):
	__defaultName = 'SEP_NR3_G_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_G_4(ComponentXY):
	__defaultName = 'SEP_NR3_G_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_G_8(ComponentXY):
	__defaultName = 'SEP_NR3_G_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_0P75(ComponentXY):
	__defaultName = 'SEP_NR3_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_1(ComponentXY):
	__defaultName = 'SEP_NR3_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_G_0P5(ComponentXY):
	__defaultName = 'SEP_NR3_G_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_G_0P65(ComponentXY):
	__defaultName = 'SEP_NR3_G_0P65'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_G_0P8(ComponentXY):
	__defaultName = 'SEP_NR3_G_0P8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_G_1(ComponentXY):
	__defaultName = 'SEP_NR3_G_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_G_3(ComponentXY):
	__defaultName = 'SEP_NR3_G_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3_G_5(ComponentXY):
	__defaultName = 'SEP_NR3_G_5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3B_G_2(ComponentXY):
	__defaultName = 'SEP_NR3B_G_2'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3B_MG_2(ComponentXY):
	__defaultName = 'SEP_NR3B_MG_2'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3B_UG_1(ComponentXY):
	__defaultName = 'SEP_NR3B_UG_1'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3B_MG_0P75(ComponentXY):
	__defaultName = 'SEP_NR3B_MG_0P75'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3B_MG_1(ComponentXY):
	__defaultName = 'SEP_NR3B_MG_1'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR3B_MG_3(ComponentXY):
	__defaultName = 'SEP_NR3B_MG_3'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4_2(ComponentXY):
	__defaultName = 'SEP_NR4_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4_4(ComponentXY):
	__defaultName = 'SEP_NR4_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4_0P5(ComponentXY):
	__defaultName = 'SEP_NR4_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4_0P75(ComponentXY):
	__defaultName = 'SEP_NR4_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4_1(ComponentXY):
	__defaultName = 'SEP_NR4_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4_3(ComponentXY):
	__defaultName = 'SEP_NR4_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4_6(ComponentXY):
	__defaultName = 'SEP_NR4_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.22, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4_8(ComponentXY):
	__defaultName = 'SEP_NR4_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.34, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4B_2(ComponentXY):
	__defaultName = 'SEP_NR4B_2'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', in4='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4B_4(ComponentXY):
	__defaultName = 'SEP_NR4B_4'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', in4='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4B_1(ComponentXY):
	__defaultName = 'SEP_NR4B_1'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', in4='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4BB_2(ComponentXY):
	__defaultName = 'SEP_NR4BB_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4BB_4(ComponentXY):
	__defaultName = 'SEP_NR4BB_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4BB_0P5(ComponentXY):
	__defaultName = 'SEP_NR4BB_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4BB_0P75(ComponentXY):
	__defaultName = 'SEP_NR4BB_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4BB_1(ComponentXY):
	__defaultName = 'SEP_NR4BB_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_NR4BB_3(ComponentXY):
	__defaultName = 'SEP_NR4BB_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA21_V2_8(ComponentXY):
	__defaultName = 'SEP_OA21_V2_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA21_4(ComponentXY):
	__defaultName = 'SEP_OA21_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA21_8(ComponentXY):
	__defaultName = 'SEP_OA21_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA21_V2_4(ComponentXY):
	__defaultName = 'SEP_OA21_V2_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA21_1(ComponentXY):
	__defaultName = 'SEP_OA21_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA21_2(ComponentXY):
	__defaultName = 'SEP_OA21_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA21_V2_1(ComponentXY):
	__defaultName = 'SEP_OA21_V2_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA21_V2_2(ComponentXY):
	__defaultName = 'SEP_OA21_V2_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA21B_4(ComponentXY):
	__defaultName = 'SEP_OA21B_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA21B_8(ComponentXY):
	__defaultName = 'SEP_OA21B_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA21B_0P5(ComponentXY):
	__defaultName = 'SEP_OA21B_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA21B_1(ComponentXY):
	__defaultName = 'SEP_OA21B_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA21B_2(ComponentXY):
	__defaultName = 'SEP_OA21B_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA22_3(ComponentXY):
	__defaultName = 'SEP_OA22_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.68, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA22_4(ComponentXY):
	__defaultName = 'SEP_OA22_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA22_DG_8(ComponentXY):
	__defaultName = 'SEP_OA22_DG_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA22_1(ComponentXY):
	__defaultName = 'SEP_OA22_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA22_2(ComponentXY):
	__defaultName = 'SEP_OA22_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA22_DG_1(ComponentXY):
	__defaultName = 'SEP_OA22_DG_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA22_DG_2(ComponentXY):
	__defaultName = 'SEP_OA22_DG_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA22_DG_4(ComponentXY):
	__defaultName = 'SEP_OA22_DG_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA2BB2_4(ComponentXY):
	__defaultName = 'SEP_OA2BB2_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.52, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA2BB2_8(ComponentXY):
	__defaultName = 'SEP_OA2BB2_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA2BB2_0P5(ComponentXY):
	__defaultName = 'SEP_OA2BB2_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA2BB2_1(ComponentXY):
	__defaultName = 'SEP_OA2BB2_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA2BB2_2(ComponentXY):
	__defaultName = 'SEP_OA2BB2_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA2BB2_U_1(ComponentXY):
	__defaultName = 'SEP_OA2BB2_U_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA31_4(ComponentXY):
	__defaultName = 'SEP_OA31_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA31_1(ComponentXY):
	__defaultName = 'SEP_OA31_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA31_2(ComponentXY):
	__defaultName = 'SEP_OA31_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA32_4(ComponentXY):
	__defaultName = 'SEP_OA32_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.1, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA32_1(ComponentXY):
	__defaultName = 'SEP_OA32_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA32_2(ComponentXY):
	__defaultName = 'SEP_OA32_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA33_4(ComponentXY):
	__defaultName = 'SEP_OA33_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', in6='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA33_1(ComponentXY):
	__defaultName = 'SEP_OA33_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', in6='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OA33_2(ComponentXY):
	__defaultName = 'SEP_OA33_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', in6='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI2111_2(ComponentXY):
	__defaultName = 'SEP_OAI2111_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI2111_4(ComponentXY):
	__defaultName = 'SEP_OAI2111_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI2111_1(ComponentXY):
	__defaultName = 'SEP_OAI2111_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI211_1P5(ComponentXY):
	__defaultName = 'SEP_OAI211_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI211_2(ComponentXY):
	__defaultName = 'SEP_OAI211_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI211_4(ComponentXY):
	__defaultName = 'SEP_OAI211_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI211_8(ComponentXY):
	__defaultName = 'SEP_OAI211_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI211_0P5(ComponentXY):
	__defaultName = 'SEP_OAI211_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI211_0P75(ComponentXY):
	__defaultName = 'SEP_OAI211_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI211_1(ComponentXY):
	__defaultName = 'SEP_OAI211_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI211_3(ComponentXY):
	__defaultName = 'SEP_OAI211_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI211_V3_1(ComponentXY):
	__defaultName = 'SEP_OAI211_V3_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21_12(ComponentXY):
	__defaultName = 'SEP_OAI21_12'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.18, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21_16(ComponentXY):
	__defaultName = 'SEP_OAI21_16'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.86, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21_2(ComponentXY):
	__defaultName = 'SEP_OAI21_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21_3(ComponentXY):
	__defaultName = 'SEP_OAI21_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21_4(ComponentXY):
	__defaultName = 'SEP_OAI21_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21_6(ComponentXY):
	__defaultName = 'SEP_OAI21_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.66, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21_8(ComponentXY):
	__defaultName = 'SEP_OAI21_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21_0P5(ComponentXY):
	__defaultName = 'SEP_OAI21_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21_0P75(ComponentXY):
	__defaultName = 'SEP_OAI21_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21_1(ComponentXY):
	__defaultName = 'SEP_OAI21_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21_1P5(ComponentXY):
	__defaultName = 'SEP_OAI21_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21B_2(ComponentXY):
	__defaultName = 'SEP_OAI21B_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21B_4(ComponentXY):
	__defaultName = 'SEP_OAI21B_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21B_8(ComponentXY):
	__defaultName = 'SEP_OAI21B_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.2, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21B_0P5(ComponentXY):
	__defaultName = 'SEP_OAI21B_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI21B_1(ComponentXY):
	__defaultName = 'SEP_OAI21B_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI221_2(ComponentXY):
	__defaultName = 'SEP_OAI221_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.68, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI221_4(ComponentXY):
	__defaultName = 'SEP_OAI221_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.08, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI221_0P5(ComponentXY):
	__defaultName = 'SEP_OAI221_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI221_1(ComponentXY):
	__defaultName = 'SEP_OAI221_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI222_1P5(ComponentXY):
	__defaultName = 'SEP_OAI222_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C1', in6='C2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI222_2(ComponentXY):
	__defaultName = 'SEP_OAI222_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C1', in6='C2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.96, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI222_4(ComponentXY):
	__defaultName = 'SEP_OAI222_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C1', in6='C2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.64, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI222_8(ComponentXY):
	__defaultName = 'SEP_OAI222_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C1', in6='C2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI222_0P75(ComponentXY):
	__defaultName = 'SEP_OAI222_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C1', in6='C2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI222_1(ComponentXY):
	__defaultName = 'SEP_OAI222_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', in5='C1', in6='C2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI22_12(ComponentXY):
	__defaultName = 'SEP_OAI22_12'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.86, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI22_2(ComponentXY):
	__defaultName = 'SEP_OAI22_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI22_4(ComponentXY):
	__defaultName = 'SEP_OAI22_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI22_6(ComponentXY):
	__defaultName = 'SEP_OAI22_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI22_8(ComponentXY):
	__defaultName = 'SEP_OAI22_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI22_0P5(ComponentXY):
	__defaultName = 'SEP_OAI22_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI22_0P75(ComponentXY):
	__defaultName = 'SEP_OAI22_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI22_1(ComponentXY):
	__defaultName = 'SEP_OAI22_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI22_3(ComponentXY):
	__defaultName = 'SEP_OAI22_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI22_5(ComponentXY):
	__defaultName = 'SEP_OAI22_5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI22_V3S_1(ComponentXY):
	__defaultName = 'SEP_OAI22_V3S_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B1', in4='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI311_2(ComponentXY):
	__defaultName = 'SEP_OAI311_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI311_4(ComponentXY):
	__defaultName = 'SEP_OAI311_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI311_1(ComponentXY):
	__defaultName = 'SEP_OAI311_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI31_2(ComponentXY):
	__defaultName = 'SEP_OAI31_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI31_G_2(ComponentXY):
	__defaultName = 'SEP_OAI31_G_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI31_G_3(ComponentXY):
	__defaultName = 'SEP_OAI31_G_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI31_G_4(ComponentXY):
	__defaultName = 'SEP_OAI31_G_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI31_G_8(ComponentXY):
	__defaultName = 'SEP_OAI31_G_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI31_1(ComponentXY):
	__defaultName = 'SEP_OAI31_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI31_G_0P5(ComponentXY):
	__defaultName = 'SEP_OAI31_G_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI31_G_0P75(ComponentXY):
	__defaultName = 'SEP_OAI31_G_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI31_G_1(ComponentXY):
	__defaultName = 'SEP_OAI31_G_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI32_2(ComponentXY):
	__defaultName = 'SEP_OAI32_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI32_4(ComponentXY):
	__defaultName = 'SEP_OAI32_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAI32_1(ComponentXY):
	__defaultName = 'SEP_OAI32_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='B1', in5='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAO211_DG_8(ComponentXY):
	__defaultName = 'SEP_OAO211_DG_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAO211_1(ComponentXY):
	__defaultName = 'SEP_OAO211_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAO211_D_2(ComponentXY):
	__defaultName = 'SEP_OAO211_D_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAO211_DG_1(ComponentXY):
	__defaultName = 'SEP_OAO211_DG_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAO211_DG_2(ComponentXY):
	__defaultName = 'SEP_OAO211_DG_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAO211_DG_4(ComponentXY):
	__defaultName = 'SEP_OAO211_DG_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAOI211_12(ComponentXY):
	__defaultName = 'SEP_OAOI211_12'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.86, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAOI211_2(ComponentXY):
	__defaultName = 'SEP_OAOI211_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAOI211_3(ComponentXY):
	__defaultName = 'SEP_OAOI211_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAOI211_4(ComponentXY):
	__defaultName = 'SEP_OAOI211_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAOI211_6(ComponentXY):
	__defaultName = 'SEP_OAOI211_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAOI211_8(ComponentXY):
	__defaultName = 'SEP_OAOI211_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAOI211_V2_4(ComponentXY):
	__defaultName = 'SEP_OAOI211_V2_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAOI211_0P5(ComponentXY):
	__defaultName = 'SEP_OAOI211_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAOI211_1(ComponentXY):
	__defaultName = 'SEP_OAOI211_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAOI211_V2_1(ComponentXY):
	__defaultName = 'SEP_OAOI211_V2_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OAOI211_V2_2(ComponentXY):
	__defaultName = 'SEP_OAOI211_V2_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='B', in4='C', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_12(ComponentXY):
	__defaultName = 'SEP_OR2_12'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_16(ComponentXY):
	__defaultName = 'SEP_OR2_16'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_20(ComponentXY):
	__defaultName = 'SEP_OR2_20'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(5.74, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_2P5(ComponentXY):
	__defaultName = 'SEP_OR2_2P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_3(ComponentXY):
	__defaultName = 'SEP_OR2_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_4(ComponentXY):
	__defaultName = 'SEP_OR2_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_8(ComponentXY):
	__defaultName = 'SEP_OR2_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_U_0P75(ComponentXY):
	__defaultName = 'SEP_OR2_U_0P75'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_1(ComponentXY):
	__defaultName = 'SEP_OR2_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_10(ComponentXY):
	__defaultName = 'SEP_OR2_10'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_1P5(ComponentXY):
	__defaultName = 'SEP_OR2_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_2(ComponentXY):
	__defaultName = 'SEP_OR2_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_5(ComponentXY):
	__defaultName = 'SEP_OR2_5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.68, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR2_6(ComponentXY):
	__defaultName = 'SEP_OR2_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3_12(ComponentXY):
	__defaultName = 'SEP_OR3_12'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.34, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3_3(ComponentXY):
	__defaultName = 'SEP_OR3_3'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.4, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3_4(ComponentXY):
	__defaultName = 'SEP_OR3_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.54, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3_8(ComponentXY):
	__defaultName = 'SEP_OR3_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.94, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3_0P5(ComponentXY):
	__defaultName = 'SEP_OR3_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3_1(ComponentXY):
	__defaultName = 'SEP_OR3_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3_1P5(ComponentXY):
	__defaultName = 'SEP_OR3_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3_2(ComponentXY):
	__defaultName = 'SEP_OR3_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3_6(ComponentXY):
	__defaultName = 'SEP_OR3_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.24, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3_L_0P5(ComponentXY):
	__defaultName = 'SEP_OR3_L_0P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3_L_1(ComponentXY):
	__defaultName = 'SEP_OR3_L_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3_L_1P5(ComponentXY):
	__defaultName = 'SEP_OR3_L_1P5'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3B_2(ComponentXY):
	__defaultName = 'SEP_OR3B_2'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.98, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3B_4(ComponentXY):
	__defaultName = 'SEP_OR3B_4'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.82, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3B_8(ComponentXY):
	__defaultName = 'SEP_OR3B_8'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3B_0P5(ComponentXY):
	__defaultName = 'SEP_OR3B_0P5'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3B_0P75(ComponentXY):
	__defaultName = 'SEP_OR3B_0P75'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR3B_1(ComponentXY):
	__defaultName = 'SEP_OR3B_1'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.7, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR4_12(ComponentXY):
	__defaultName = 'SEP_OR4_12'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(6.86, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR4_2(ComponentXY):
	__defaultName = 'SEP_OR4_2'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.26, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR4_4(ComponentXY):
	__defaultName = 'SEP_OR4_4'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.38, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR4_6(ComponentXY):
	__defaultName = 'SEP_OR4_6'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(3.5, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR4_8(ComponentXY):
	__defaultName = 'SEP_OR4_8'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.62, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR4_1(ComponentXY):
	__defaultName = 'SEP_OR4_1'

	def __init__(self, name = __defaultName, in1='A1', in2='A2', in3='A3', in4='A4', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR4B_2(ComponentXY):
	__defaultName = 'SEP_OR4B_2'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', in4='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(1.12, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR4B_4(ComponentXY):
	__defaultName = 'SEP_OR4B_4'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', in4='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(2.1, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR4B_8(ComponentXY):
	__defaultName = 'SEP_OR4B_8'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', in4='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.06, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_OR4B_1(ComponentXY):
	__defaultName = 'SEP_OR4B_1'

	def __init__(self, name = __defaultName, in1='A', in2='B1', in3='B2', in4='B3', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.84, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_TIE0_1(ComponentXY):
	__defaultName = 'SEP_TIE0_1'


class SEP_TIE1_1(ComponentXY):
	__defaultName = 'SEP_TIE1_1'


class SEP_TIEDIN_Y2_1(ComponentXY):
	__defaultName = 'SEP_TIEDIN_Y2_1'

	def __init__(self, name = __defaultName, in1='X', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(0.56, 1.8)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)

class SEP_DCAP_4(ComponentXY):
	__defaultName = 'SEP_DCAP_4'


class SEP_DCAP_6(ComponentXY):
	__defaultName = 'SEP_DCAP_6'


class SEP_DCAP_8(ComponentXY):
	__defaultName = 'SEP_DCAP_8'


class SEP_FILL32(ComponentXY):
	__defaultName = 'SEP_FILL32'


class SEP_FILL_ECONOPG19(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG19'


class SEP_FILL_ECONOPG18(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG18'


class SEP_FILL128(ComponentXY):
	__defaultName = 'SEP_FILL128'


class SEP_FILL8(ComponentXY):
	__defaultName = 'SEP_FILL8'


class SEP_FILL_ECONOPG11(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG11'


class SEP_FILL_ECONOPG10(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG10'


class SEP_FILL_ECONOPG13(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG13'


class SEP_FILL_ECONOPG12(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG12'


class SEP_FILL_ECONOPG15(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG15'


class SEP_FILL_ECONOPG14(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG14'


class SEP_FILL3(ComponentXY):
	__defaultName = 'SEP_FILL3'


class SEP_FILL2(ComponentXY):
	__defaultName = 'SEP_FILL2'


class SEP_FILLV2Y256(ComponentXY):
	__defaultName = 'SEP_FILLV2Y256'


class SEP_FILLV2Y32(ComponentXY):
	__defaultName = 'SEP_FILLV2Y32'


class SEP_DCAP_ECOCT_20(ComponentXY):
	__defaultName = 'SEP_DCAP_ECOCT_20'


class SEP_FILL_ECONOPG20(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG20'


class SEP_FILLV2Y128(ComponentXY):
	__defaultName = 'SEP_FILLV2Y128'


class SEP_FILLV2Y3(ComponentXY):
	__defaultName = 'SEP_FILLV2Y3'


class SEP_FILLV2Y2(ComponentXY):
	__defaultName = 'SEP_FILLV2Y2'


class SEP_FILLV2Y1(ComponentXY):
	__defaultName = 'SEP_FILLV2Y1'


class SEP_FILLV2Y6(ComponentXY):
	__defaultName = 'SEP_FILLV2Y6'


class SEP_FILLV2Y5(ComponentXY):
	__defaultName = 'SEP_FILLV2Y5'


class SEP_FILLV2Y4(ComponentXY):
	__defaultName = 'SEP_FILLV2Y4'


class SEP_FILLV2Y8(ComponentXY):
	__defaultName = 'SEP_FILLV2Y8'


class SEP_FILL_ECONOPG9(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG9'


class SEP_FILL_ECONOPG8(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG8'


class SEP_FILLNOPG6(ComponentXY):
	__defaultName = 'SEP_FILLNOPG6'


class SEP_FILL_ECONOPG1(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG1'


class SEP_FILL_ECOCT20(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT20'


class SEP_FILL_ECONOPG3(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG3'


class SEP_FILL_ECONOPG2(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG2'


class SEP_FILL_ECONOPG5(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG5'


class SEP_FILL_ECONOPG4(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG4'


class SEP_FILL_ECONOPG7(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG7'


class SEP_FILL_ECONOPG6(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG6'


class SEP_FILL_ECO19(ComponentXY):
	__defaultName = 'SEP_FILL_ECO19'


class SEP_FILL_ECO18(ComponentXY):
	__defaultName = 'SEP_FILL_ECO18'


class SEP_DCAP_ECOCT_4(ComponentXY):
	__defaultName = 'SEP_DCAP_ECOCT_4'


class SEP_FILL_ECO13(ComponentXY):
	__defaultName = 'SEP_FILL_ECO13'


class SEP_FILL_ECO12(ComponentXY):
	__defaultName = 'SEP_FILL_ECO12'


class SEP_FILL_ECO11(ComponentXY):
	__defaultName = 'SEP_FILL_ECO11'


class SEP_FILL_ECO10(ComponentXY):
	__defaultName = 'SEP_FILL_ECO10'


class SEP_FILL_ECO17(ComponentXY):
	__defaultName = 'SEP_FILL_ECO17'


class SEP_FILL_ECO16(ComponentXY):
	__defaultName = 'SEP_FILL_ECO16'


class SEP_FILL_ECO15(ComponentXY):
	__defaultName = 'SEP_FILL_ECO15'


class SEP_FILL_ECO14(ComponentXY):
	__defaultName = 'SEP_FILL_ECO14'


class SEP_FILL_ECOCT8(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT8'


class SEP_FILL_ECOCT9(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT9'


class SEP_FILL_ECOCT6(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT6'


class SEP_FILL_ECOCT7(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT7'


class SEP_FILL_ECOCT4(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT4'


class SEP_FILL_ECOCT5(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT5'


class SEP_FILL_ECOCT2(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT2'


class SEP_FILL_ECOCT3(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT3'


class SEP_FILL_ECOCT1(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT1'


class SEP_FILLNOPG256(ComponentXY):
	__defaultName = 'SEP_FILLNOPG256'


class SEP_FILLV2Y16(ComponentXY):
	__defaultName = 'SEP_FILLV2Y16'


class SEP_FILLNOPG5(ComponentXY):
	__defaultName = 'SEP_FILLNOPG5'


class SEP_FILLNOPG4(ComponentXY):
	__defaultName = 'SEP_FILLNOPG4'


class SEP_FILLNOPG3(ComponentXY):
	__defaultName = 'SEP_FILLNOPG3'


class SEP_FILLNOPG2(ComponentXY):
	__defaultName = 'SEP_FILLNOPG2'


class SEP_FILLNOPG1(ComponentXY):
	__defaultName = 'SEP_FILLNOPG1'


class SEP_FILLNOPG8(ComponentXY):
	__defaultName = 'SEP_FILLNOPG8'


class SEP_FILL64(ComponentXY):
	__defaultName = 'SEP_FILL64'


class SEP_FILL5(ComponentXY):
	__defaultName = 'SEP_FILL5'


class SEP_FILL_ECO9(ComponentXY):
	__defaultName = 'SEP_FILL_ECO9'


class SEP_FILL_ECO8(ComponentXY):
	__defaultName = 'SEP_FILL_ECO8'


class SEP_FILL4(ComponentXY):
	__defaultName = 'SEP_FILL4'


class SEP_FILL_ECO3(ComponentXY):
	__defaultName = 'SEP_FILL_ECO3'


class SEP_FILL_ECO2(ComponentXY):
	__defaultName = 'SEP_FILL_ECO2'


class SEP_FILL_ECO1(ComponentXY):
	__defaultName = 'SEP_FILL_ECO1'


class SEP_FILL_ECO7(ComponentXY):
	__defaultName = 'SEP_FILL_ECO7'


class SEP_FILL_ECO6(ComponentXY):
	__defaultName = 'SEP_FILL_ECO6'


class SEP_FILL_ECO5(ComponentXY):
	__defaultName = 'SEP_FILL_ECO5'


class SEP_FILL_ECO4(ComponentXY):
	__defaultName = 'SEP_FILL_ECO4'


class SEP_FILL6(ComponentXY):
	__defaultName = 'SEP_FILL6'


class SEP_FILL1(ComponentXY):
	__defaultName = 'SEP_FILL1'


class SEP_FILL_ECONOPG17(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG17'


class SEP_FILLNOPG16(ComponentXY):
	__defaultName = 'SEP_FILLNOPG16'


class SEP_DCAPN_V1_16(ComponentXY):
	__defaultName = 'SEP_DCAPN_V1_16'


class SEP_FILL_ECONOPG16(ComponentXY):
	__defaultName = 'SEP_FILL_ECONOPG16'


class SEP_FILLNOPG12(ComponentXY):
	__defaultName = 'SEP_FILLNOPG12'


class SEP_FILL256(ComponentXY):
	__defaultName = 'SEP_FILL256'


class SEP_FILLV2Y12(ComponentXY):
	__defaultName = 'SEP_FILLV2Y12'


class SEP_CAPLRNOPG4(ComponentXY):
	__defaultName = 'SEP_CAPLRNOPG4'


class SEP_FILLNOPG64(ComponentXY):
	__defaultName = 'SEP_FILLNOPG64'


class SEP_TAPPN(ComponentXY):
	__defaultName = 'SEP_TAPPN'


class SEP_FILL12(ComponentXY):
	__defaultName = 'SEP_FILL12'


class SEP_CAPLR2(ComponentXY):
	__defaultName = 'SEP_CAPLR2'


class SEP_FILLV2Y64(ComponentXY):
	__defaultName = 'SEP_FILLV2Y64'


class SEP_FILL16(ComponentXY):
	__defaultName = 'SEP_FILL16'


class SEP_DCAPN_V1_32(ComponentXY):
	__defaultName = 'SEP_DCAPN_V1_32'


class SEP_DCAP_ECOCT_8(ComponentXY):
	__defaultName = 'SEP_DCAP_ECOCT_8'


class SEP_DCAP_ECOCT_12(ComponentXY):
	__defaultName = 'SEP_DCAP_ECOCT_12'


class SEP_CAPLRV2Y4(ComponentXY):
	__defaultName = 'SEP_CAPLRV2Y4'


class SEP_DCAPN_V1_8(ComponentXY):
	__defaultName = 'SEP_DCAPN_V1_8'


class SEP_DCAP_ECOCT_16(ComponentXY):
	__defaultName = 'SEP_DCAP_ECOCT_16'


class SEP_DCAPN_V1_4(ComponentXY):
	__defaultName = 'SEP_DCAPN_V1_4'


class SEP_TAPDS(ComponentXY):
	__defaultName = 'SEP_TAPDS'


class SEP_FILL_ECOCT10(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT10'


class SEP_FILL_ECOCT11(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT11'


class SEP_FILL_ECOCT12(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT12'


class SEP_FILL_ECOCT13(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT13'


class SEP_FILL_ECOCT14(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT14'


class SEP_FILL_ECOCT15(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT15'


class SEP_FILL_ECOCT16(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT16'


class SEP_FILL_ECOCT17(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT17'


class SEP_FILL_ECOCT18(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT18'


class SEP_FILL_ECOCT19(ComponentXY):
	__defaultName = 'SEP_FILL_ECOCT19'


class SEP_FILLNOPG128(ComponentXY):
	__defaultName = 'SEP_FILLNOPG128'


class SEP_DCAP_16(ComponentXY):
	__defaultName = 'SEP_DCAP_16'


class SEP_DCAP_12(ComponentXY):
	__defaultName = 'SEP_DCAP_12'


class SEP_FILL_ECO20(ComponentXY):
	__defaultName = 'SEP_FILL_ECO20'


class SEP_FILLNOPG32(ComponentXY):
	__defaultName = 'SEP_FILLNOPG32'


	def __init__(self, name = __defaultName, in1='i1', in2='i0', in3='s0', out1='X'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='i3', in2='i2', in3='i1', in4='i0', in5='s1', in6='s0', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='s', in3='r', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='s', in3='r', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='clk', in3='d', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='clk', in3='d', in4='r', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='clk', in3='d', in4='s', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='clk', in3='clka', in4='d', in5='si', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='clk', in3='d', in4='s', in5='r', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='clk', in3='d', in4='s', in5='r', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='clk', in2='d', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='clk', in3='d', in4='xcr', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='clk', in2='d', in3='r', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='clk', in3='d', in4='r', in5='xcr', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='clk', in2='d', in3='s', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='clk', in3='d', in4='s', in5='xcr', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='clk', in2='d', in3='s', in4='r', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='clk', in2='d', in3='s', in4='r', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='clk', in3='d', in4='s', in5='r', in6='xcr', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='clk', in3='d', in4='b2', in5='lq', in6='xcr', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='clk', in3='d', in4='r', in5='b2', in6='lq', in7='xcr', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Input(in7) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='clk', in3='d', in4='s', in5='b2', in6='lq', in7='xcr', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Input(in7) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='clk', in3='d', in4='s', in5='r', in6='xcr', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='v', in2='clk', in3='d', in4='s', in5='r', in6='xcr', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
	def __init__(self, name = __defaultName, in1='i3', in2='i2', in3='i1', in4='i0', in5='s3', in6='s2', in7='s1', in8='s0', in9='sb3', in10='sb2', in11='sb1', in12='sb0', out1='q'):
		ComponentXY.__init__(self,name)
		self.add_pin(Input(in1) )
		self.add_pin(Input(in2) )
		self.add_pin(Input(in3) )
		self.add_pin(Input(in4) )
		self.add_pin(Input(in5) )
		self.add_pin(Input(in6) )
		self.add_pin(Input(in7) )
		self.add_pin(Input(in8) )
		self.add_pin(Input(in9) )
		self.add_pin(Input(in10) )
		self.add_pin(Input(in11) )
		self.add_pin(Input(in12) )
		self.add_pin(Output(out1) )
		self.set_component_dimensions(4.48, 0.9)
		self.set_dont_uniq(True)
		self.set_dont_write_verilog(True)
