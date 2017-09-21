class RAM:
	def __init__(self):
		self._ram = {}
	def get(self,addr):
		return self._ram.get(addr&65535,0)
	def set(self,addr,value):
		self._ram[addr&65535] = value & 255
