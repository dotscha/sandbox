
class ASM:
	
	def __init__(self):
		self.ram = []
		self.start = None
		self.pc = 0x0200
		self.lables = {}
		self.resolve = []
		
	def compile(self):
		for r in self.resolve:
			r(self)
		
	def pc(self):
		return self.pc
		
	def setpc(self,newpc):
		self.pc = newpc & 0xffff
		return self
		
	def lable(self,name):
		return self.lables[name]
		
	def setlable(self,name):
		self.lables[name] = self.pc
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
			self.resolve.append(eval("lambda _asmctx_: _asmctx_.pokes({pc},[{op},{b}])".format(
				pc = self.pc,
				op = op,
				b = b.replace("lable(","_asmctx_.lable(")
			)))
			b = 0
		return self.code([op,b])
		
	def op_w(self,op,w):
		if type(w)==type(""):
			self.resolve.append(eval("lambda _asmctx_: _asmctx_.pokes({pc},[{op}]+_asmctx_.word({w}))".format(
				pc = self.pc,
				op = op,
				w = w.replace("lable(","_asmctx_.lable(")
			)))
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
c=23
a.setpc(0x1028).lda(13).lda_abs_x("lable('l')")
a.setpc(0x1020).setlable("l").lda("lable('l')/256").ldx("lable('l')&255").ldy("c")

print(a.ram)
a.compile()
print(a.ram)