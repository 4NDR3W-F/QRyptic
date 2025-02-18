import numpy as np
from functions import gate
from math import *
from pulses import double_square
from matplotlib import pyplot as plt


STEPS    = 1000
DURATION = 100
DELTA    = 0

time=np.linspace(0,100,STEPS+1)
# print(len(time))
dt = time[2] -time[0]
# time=np.linspace(0,100+dt,STEPS+1)

    
omega= double_square(time=time, 
                     duration1=DURATION/2,
                     duration2=DURATION/2,
                     area1=pi,
                     area2=0)

plt.plot(time, np.real(omega))
plt.plot(time, np.imag(omega))
plt.show()
GATE=gate(time=time, omega3=omega, delta=DELTA)

print(GATE)
