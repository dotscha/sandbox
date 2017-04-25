import sys
import os 
import subprocess
import importlib.util
import re

############################################################################################

def parseNum(n):
	try:
		n = n.strip()
		if n.startswith("$"):
			n="0x"+n[1:]
		return eval(n)
	except:
		raise "Not a number: {n}".format(n=n)
	
############################################################################################

class File:
	
	def __init__(self, dir, fileDesc):
		p = "([^@\[\]]+)(\[(.+)\])?(@(.+))?"
		m = re.search(p,fileDesc) #partial parsing
		if m==None:
			raise "Invalid file descriptor: {f}".format(f=fileDesc)
		g = m.groups()
		data_filename = g[0].strip()
		self.filename = "{d}/{f}".format(d=dir,f=data_filename)
		with open(self.filename,'rb') as r:
			self.data = [b for b in r.read()]
		data_range = g[2]
		data_reloc = g[4]
		print(g)
		if data_range==None and data_reloc==None:
			if len(self.data)>1:
				self.address = self.data[0]+self.data[1]*256;
				self.data = self.data[2:]
			else:
				raise "{f} is too short!".format(f=self.filename)
		else:
			is_prg = data_filename.lower().endswith(".prg")
			if data_reloc!=None:
				self.address = parseNum(data_reloc)
				if data_range==None and is_prg:
					print ("Waring: PRG relocation without skiping first two bytes: {f}".format(f=fileDesc))
			else:
				raise "Load address missing: {f}".format(f=fileDesc)
			if data_range!=None:
				if (not ':' in data_range) or len(data_range.split(':'))!=2:
					raise "Invalid data range format: {f}".format(f=fileDesc)
				else:
					begin,end = data_range.split(':')
					if len(begin):
						begin = parseNum(begin)
					else:
						begon = 0
					if len(end):
						end = parseNum(end)
					if is_prg and begin in [0,1,-len(self.data),-len(self.data)+1]:	 #no, not smarter than that
						print ("Waring: PRG relocation without skiping first two bytes: {f}".format(f=fileDesc))
					self.data = eval("self.data[{b}:{e}]".format(b=begin,e=end))
		if len(self.data)==0:
			print ("Zero length data: {f}".format(f=fileDesc))

	def size(self):
		return len(self.data)


############################################################################################
############################################################################################
############################################################################################

partdirs = []
for (dirpath, dirnames, filenames) in os.walk("."):
	partdirs.extend(sorted([d for d in dirnames if d[0] in "0123456789"]))
	break

for d in partdirs:
	#TODO:linking.py exists?
	spec = importlib.util.spec_from_file_location(d,"{d}/linking.py".format(d=d))
	part = spec.loader.load_module()
	for f in part.meta['requires']:
		_f = File(d,f)
		print (_f.filename)
		print (_f.address)
		print (_f.size())
