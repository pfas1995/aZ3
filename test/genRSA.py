import os
import glob
import time

cur_dir = os.getcwd()
# print cur_dir

array_source = glob.glob(cur_dir + "/src_rsa/*.c")

for source in array_source:
	bname = os.path.basename(source)
	name = os.path.splitext(bname)[0]
	cmd1 = "cbmc --unwind 10 --smt2 --outfile QF_AUFBV/" + name + ".smt2 src_rsa/" + bname
	cmd2 = "java CBMCwrapper QF_AUFBV/" + name + ".smt2"

	start = time.time()
	os.system(cmd1)
	os.system(cmd2)
	end = time.time()
	elapsed = end - start
	print ">>> " + source + ": "
	print elapsed

