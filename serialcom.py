# This code reads the serial data from a USB port and plots it in real-time (almost)
# The Acquisition device may send additional channels of data, which needs to be parsed in the 'animate' function/method
# Author: Rajath Bhargav

import serial as serl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as fanim

port = serl.Serial(port='/dev/ttyACM0',baudrate=115200,timeout=0.1)

y = []		# list to hold values

fig = plt.figure()	# create a figure object

def animate(i):
    port.reset_input_buffer()       # clear buffer to get recent value. Some data is lost but plotting is real time
    while not port.inWaiting():
        pass                        # wait till the next byte is recieved
    data = port.readline()
    s = data.decode('UTF-8')
    y.append(float(s[0:4]))
    if len(y)>50:		            # if list grows above 50, remove the oldest value (index 0)
        y.pop(0)                    # this keeps the list from growing and slowing down the re-plotting process
    plt.clf()
    plt.plot(y)
    
ani = fanim(fig,animate,interval=1) # animation method from matplotlib calls animate function repititively on figure supplied
plt.show()
