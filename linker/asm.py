
cpu6502ops = {
	0x00:('brk',''     ,6),
	0x60:('rts',''     ,6),
	0xa0:('ldy','#'    ,2),
	0xa2:('ldx','#'    ,2),
	0xa9:('lda','#'    ,2),
	0xbd:('lda','abs_x',4,5),
	  -1:-1
}

class ASM:
	
	def __init__(self):
		self.ram = []
		self.start = None
		self.pc = 0x0200
		self.labels = {}
		self.resolve = []
		
	def compile(self):
		for r in self.resolve:
			r(self)
		
	def pc(self):
		return self.pc
		
	def setpc(self,newpc):
		self.pc = newpc & 0xffff
		return self
		
	def label(self,name):
		return self.labels[name]
		
	def setlabel(self,name,value=None):
		self.labels[name] = self.pc if value==None else value
		return self
	
	def poke(self,addr,byte):
		byte = int(byte)&0xff
		if len(self.ram)==0:
			self.start = addr
		if addr==self.start+len(self.ram):
			self.ram.append(byte)
		elif self.start<=addr<self.start+len(self.ram):
			self.ram[addr-self.start] = byte
		elif addr<self.start:
			self.ram = [byte] + [None]*(self.start-addr-1) + self.ram
			self.start = addr
		else:
			self.ram.extend([None]*(addr-self.start-len(self.ram)))
			self.ram.append(byte)
			
	def pokes(self,addr,bytes):
		for b in bytes:
			self.poke(addr,b)
			addr = (addr+1) & 0xffff
		
	def code(self,bytes):
		self.pokes(self.pc,bytes)
		self.pc = (self.pc+len(bytes)) & 0xffff
		return self
	
	def op_b(self,op,b):
		if type(b)==type(""):
			self.resolve.append(eval("lambda _asmctx_: _asmctx_.poke({pc},{b})".format(
				pc = self.pc+1, b = b
			),self.labels))
			b = 0
		return self.code([op,b])
		
	def op_w(self,op,w):
		if type(w)==type(""):
			self.resolve.append(eval("lambda _asmctx_: _asmctx_.pokes({pc},_asmctx_.word({w}))".format(
				pc = self.pc+1, w = w
			),self.labels))
			w = 0
		return self.code([op]+self.word(w))
	
	def word(self,w):
		w = int(w)
		return [w&255,w/256]
			
	def lda(self,b):
		return self.op_b(0xa9,b)
		
	def lda_abs_x(self,w):
		return self.op_w(0xbd,w)
	
	def ldx(self,b):
		return self.op_b(0xa2,b)
		
	def ldy(self,b):
		return self.op_b(0xa0,b)

a = ASM()
a.setpc(0x1028).lda(13).lda_abs_x("l")
a.setpc(0x1020).setlabel("l").lda("l/256").ldx("l&255")

print(a.ram)
a.compile()
print(a.ram)
