from serial import*
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import time

serialPort = "/dev/ttyACM0"
baudRate = 9600
ser = Serial(serialPort, baudRate)  # ensure non-blocking

gData = []

fig = plt.figure()
ax = fig.add_subplot(111)

plt.ylim(0, 4)
plt.xlim(0, 256)

def update_line(i):
    line = ser.readline().strip().decode('utf8')
    gData.append(int(line))
    print(line)
    ax.clear()
    ax.plot(gData,)

line_ani = animation.FuncAnimation(fig, update_line, interval=500)

plt.show()

