#!/usr/bin/env python

import os
import time
import multiprocessing
import threading
import subprocess


NUM_WORKERS = 4
BASH_FILE = "./wait.sh"

def crunch_numbers():
	print "PID: %s, Process Name: %s, Thread Name: %s" % ( os.getpid(), multiprocessing.current_process().name, threading.current_thread().name)
	bash_process = subprocess.Popen(BASH_FILE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, error = bash_process.communicate()
	# Get output data
	cmd_out = out.splitlines()
	for line in cmd_out:
		print(line.decode('utf-8')) 
    

start_time = time.time()
threads = [threading.Thread(target=crunch_numbers) for _ in range(NUM_WORKERS)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]
end_time = time.time()

print "hello"
