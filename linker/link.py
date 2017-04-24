import sys
import os 
import subprocess
import importlib.util

partdirs = []
for (dirpath, dirnames, filenames) in os.walk("."):
	partdirs.extend(sorted([d for d in dirnames if d[0] in "0123456789"]))
	break

for d in partdirs:
	spec = importlib.util.spec_from_file_location(d,"{d}/linking.py".format(d=d))
	part = spec.loader.load_module()
	print (part.meta)
