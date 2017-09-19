from opcode import opcodes
from memory import RAM

class CPU:
	def __init__(self):
		self.PC = 0x1000
		self.SP = 0xff
		self.X = 0
		self.Y = 0
		self.A = 0

		self.cycles = 0

		self.C = False
		self.Z = False
		self.I = False
		self.D = False
		self.B = False
		self.V = False
		self.N = False

		self.addressing_mode = {
			"Accumulator"   : ( CPU._get_a      , CPU._set_a     ),
			"Immediate"     : ( CPU._get_imm    , None           ),
			"ZeroPage"      : ( CPU._get_zp     , CPU._set_zp    ),
			"ZeroPage,X"    : ( CPU._get_zp_x   , CPU._set_zp_x  ),
			"ZeroPage,Y"    : ( CPU._get_zp_y   , CPU._set_zp_y  ),
			"Absolute"      : ( CPU._get_abs    , CPU._set_abs   ),
			"Absolute,X"    : ( CPU._get_abs_x  , CPU._set_abs_x ),
			"Absolute,Y"    : ( CPU._get_abs_x  , CPU._set_abs_x ),
			"(Indirect),Y"  : ( CPU._get_ind_y  , CPU._get_ind_y ),
			"(Indirect,X)"  : ( CPU._get_ind_x  , CPU._set_ind_x ),
			"Implied/Stack" : ( CPU._pull       , CPU._push      ),
			"(Abs.Indirect)": ( CPU._get_abs_ind, None           ),
			"Relative"      : ( CPU._get_rel    , None           ),
			"Implied"       : ( None            , None           )
		}

		self.instruction = {
			"LDA" : CPU._lda,
			"STA" : CPU._sta,
			"LDX" : CPU._ldx,
			"STX" : CPU._stx,
			"LDY" : CPU._ldy,
			"STY" : CPU._sty,
			"INX" : CPU._inx,
			"DEX" : CPU._dex,
			"INY" : CPU._iny,
			"DEY" : CPU._dey,
			"JMP" : CPU._jmp,
			"JSR" : CPU._jsr,
			"RTS" : CPU._rts,
			"TAX" : CPU._tax,
			"TXA" : CPU._txa,
			"TAY" : CPU._tay,
			"TYA" : CPU._tya,
			"TSX" : CPU._tsx,
			"TXS" : CPU._txs,
		}

	def step(self,mem):
		opcode, addr_mode, op_name, op_len, op_cycles, opt = opcodes[mem.get(self.PC)]
		inst = self.instruction[op_name]
		gett,sett = self.addressing_mode[addr_mode]
		inst(self,mem,gett,sett,op_len)

	####################
	# Addressing Modes #
	####################

	#Accumulator
	def _get_a(self,mem):
		return self.A

	def _set_a(self,mem,value):
		self.A = value

	#Immediate
	def _get_imm(self,mem):
		return mem.get(self.PC+1)

	#ZeroPage
	def _get_zp(self,mem):
		return mem.get(mem.get(self.PC+1))

	def _set_zp(self,mem):
		mem.set(mem.get(self.PC+1), value)

	#ZeroPage,X
	def _get_zp_x(self,mem):
		return mem.get((mem.get(self.PC+1) + self.X) & 255)

	def _set_zp_x(self,mem,value):
		mem.set((mem.get(self.PC+1) + self.X) & 255, value)

	#ZeroPage,Y
	def _get_zp_y(self,mem):
		return mem.get((mem.get(self.PC+1) + self.Y) & 255)

	def _set_zp_y(self,mem,value):
		mem.set((mem.get(self.PC+1) + self.Y) & 255, value)

	#Absolute
	def _get_abs(self,mem):
		return mem.get(mem.get(self.PC+1)+256*mem.get(self.PC+2))

	def _set_abs(self,mem,value):
		mem.set(mem.get(self.PC+1)+256*mem.get(self.PC+2), value)

	#Absolute,X
	def _get_abs_x(self,mem):
		return mem.get(mem.get(self.PC+1)+256*mem.get(self.PC+2)+self.X)

	def _set_abs_x(self,mem,value):
		mem.set(mem.get(self.PC+1)+256*mem.get(self.PC+2)+self.X, value)

	#Absolute,Y
	def _get_abs_y(self,mem):
		return mem.get(mem.get(self.PC+1)+256*mem.get(self.PC+2)+self.Y)

	def _set_abs_y(self,mem,value):
		mem.set(mem.get(self.PC+1)+256*mem.get(self.PC+2)+self.Y, value)

	#(Indirect),Y
	def _get_ind_y(self,mem):
		zp = mem.get(self.PC+1)
		return mem.get(mem.get(zp)+256*mem.get((zp+1)&255)+self.Y)

	def _set_ind_y(self,mem,value):
		zp = mem.get(self.PC+1)
		mem.set(mem.get(zp)+256*mem.get((zp+1)&255)+self.Y, value)

	#(Indirect,X)
	def _get_ind_x(self,mem):
		zp = (mem.get(self.PC+1)+self.X)&255
		return mem.get(mem.get(zp)+256*mem.get((zp+1)&255))

	def _set_ind_x(self,mem,value):
		zp = (mem.get(self.PC+1)+self.X)&255
		mem.set(mem.get(zp)+256*mem.get((zp+1)&255), value)

	#Implied/Stack
	def _pull(self,mem):
		self.SP = (self.SP+1)&255
		return mem.get(256+self.SP)

	def _push(self,mem,value):
		mem.set(256+self.SP, value)
		self.SP = (self.SP+255)&255

	#(Abs.Indirect)
	def _get_abs_ind(self,mem):
		alo = mem.get(self.PC+1)
		ahi = mem.get(self.PC+2)
		addr_lo = mem.get(alo+256*ahi)
		alo = (alo+1)&255
		return addr_lo + 256*mem.get(alo+256*ahi)

	#Relative
	def _get_rel(self,mem):
		rel = mem.get(self.PC+1)
		if rel<128:
			return self.PC+2+rel
		else:
			return self.PC+2+rel-256

	################
	# Instructions #
	################

	def _update_nz(self,value):
		self.Z = value==0
		self.N = value>127

	def _lda(self,mem,getter,setter,op_len):
		self.A = getter(self,mem)
		self._update_nz(self.A)
		self.PC += op_len

	def _sta(self,mem,getter,setter,op_len):
		setter(self,mem,self.A)
		self.PC += op_len
		
	def _ldx(self,mem,getter,setter,op_len):
		self.X = getter(self,mem)
		self._update_nz(self.X)
		self.PC += op_len

	def _stx(self,mem,getter,setter,op_len):
		setter(self,mem,self.X)
		self.PC += op_len
		
	def _ldy(self,mem,getter,setter,op_len):
		self.Y = getter(self,mem)
		self._update_nz(self.Y)
		self.PC += op_len

	def _sty(self,mem,getter,setter,op_len):
		setter(self,mem,self.Y)
		self.PC += op_len

	def _inx(self,mem,getter,setter,op_len):
		self.X = (self.X+1)&255
		self._update_nz(self.X)
		self.PC += op_len

	def _dex(self,mem,getter,setter,op_len):
		self.X = (self.X+255)&255
		self._update_nz(self.X)
		self.PC += op_len

	def _iny(self,mem,getter,setter,op_len):
		self.Y = (self.Y+1)&255
		self._update_nz(self.Y)
		self.PC += op_len

	def _dey(self,mem,getter,setter,op_len):
		self.Y = (self.Y+255)&255
		self._update_nz(self.Y)
		self.PC += op_len

	def _jmp(self,mem,getter,setter,op_len):
		self.PC = mem.get(self.PC+1)+256*mem.get(self.PC+2)
		
	def _jsr(self,mem,getter,setter,op_len):
		self._push(mem,(seld.PC+2)/255)
		self._push(mem,(seld.PC+2)&255)
		self._jmp(mem,None,None,-1)
	
	def _rts(self,mem,getter,setter,op_len):
		self.PC = self._pull(mem) + 256*self._pull(mem) + 1
		
	def _tax(self,mem,getter,setter,op_len):
		self.X = self.A
		self._update_nz(self.X)
		self.PC += 1
		
	def _txa(self,mem,getter,setter,op_len):
		self.A = self.X
		self._update_nz(self.A)
		self.PC += 1
		
	def _tay(self,mem,getter,setter,op_len):
		self.Y = self.A
		self._update_nz(self.Y)
		self.PC += 1
		
	def _tya(self,mem,getter,setter,op_len):
		self.A = self.Y
		self._update_nz(self.A)
		self.PC += 1
		
	def _tsx(self,mem,getter,setter,op_len):
		self.X = self.SP
		self._update_nz(self.X)
		self.PC += 1
		
	def _txs(self,mem,getter,setter,op_len):
		self.SP = self.X
		self.PC += 1
		
ram = RAM()
cpu = CPU()

ram.set(0x1000,0xA5) #lda $10
ram.set(0x1001,0x10)
ram.set(0x10,0x7)

cpu.step(ram)
print (cpu.A)
print ("Not implemented yet:")
print (set(op[1] for op in opcodes if op[1] not in cpu.addressing_mode ))
print ("Not implemented yet:")
print (set(op[2] for op in opcodes if op[2] not in cpu.instruction))
