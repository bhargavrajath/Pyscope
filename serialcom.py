# This code reads serial data from a USB port and stores it in a file

import serial as ser
import datetime as dt

port = ser.Serial(port='/dev/ttyACM0',baudrate=115200)

with open('waveform.txt','w+') as fout:
	fout.write('\n')
	fout.write(str(dt.datetime.now()))
	fout.write('\n')
	count = 0

	while count < 10000:
		data = port.read(1)
		fout.write(data.decode("UTF-8"))
		count = count + 1
