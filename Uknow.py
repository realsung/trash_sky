import random
import time
import signal
import os
import sys
import base64
import binascii

signal.alarm(5)

print """
 _____  _                  _    
/  __ \| |                | |   
| /  \/| |__    ___   ___ | | __
| |    | '_ \  / _ \ / __|| |/ /
| \__/\| | | ||  __/| (__ |   < 
 \____/|_| |_| \___| \___||_|\_\\
                                
"""

print "Plz Send Me Correct Answer!\n"
time.sleep(0.5)
try:
	for i in range(100):
		go = ""
		print "==== Level " + str(i+1) + " ====" 
		for i in range(random.randint(30,50)):
			tmp = random.randint(65,90)
			go += chr(tmp)
		f = open("a.c","w")
		f.write('#include <stdio.h>\nint main(){\nprintf("'+go+'");}')
		f.close()
		os.system("gcc a.c")
		f = open('a.out','rb')
		data = f.read()
		f.close()
		b = binascii.hexlify(data)
		print base64.b64encode(b)
		print 
		a = raw_input("Input >> ")
		if a == go:
			print "Correct!"
		else:
			sys.exit()
except:
	print 
	print "Failed"
	sys.exit()
