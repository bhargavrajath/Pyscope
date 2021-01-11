# This code reads serial data from a USB port and stores it in a file
# Author: Rajath Bhargav

import serial as ser
import datetime as dt

# configure and open port
port = ser.Serial(port='/dev/ttyACM0',baudrate=115200)

with open('waveform.txt','w+') as fout:
	fout.write('\n')
	fout.write(str(dt.datetime.now())) # date and time stamp
	fout.write('\n')
	count = 0

	while count < 10000:	# read 100000 bytes
		data = port.read(1)
		fout.write(data.decode("UTF-8")) # decode UTF-8 to ASCII
		count = count + 1
