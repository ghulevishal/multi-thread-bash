#!/usr/bin/env python

import subprocess
import os

BASH_FILE = "./wait.sh"

print "hello"
subprocess.call(BASH_FILE, shell=True)

#os.system(BASH_FILE)
#bash_process = subprocess.Popen(BASH_FILE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#out, error = bash_process.communicate()
# Get output data
#cmd_out = out.splitlines()
#for line in cmd_out:
#	print(line.decode('utf-8')) 
 
