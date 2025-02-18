import numpy as np
from matplotlib import pyplot as plt
from math import *
import cmath

def square(time, start, duration, area):
    if start<=time<start + duration:
        pulse = area/duration
    else:
        pulse = 0
    return pulse

def double_square(time, duration1 ,duration2, area1, area2):
    pulse_sequence=[]
    for t in time:
        pulse_sequence.append(square(t,start=0, duration=duration1, area=area1 )+square(t,start=duration1, duration=duration2, area=area2))
   
    return pulse_sequence

def c_pulses(time, duration1, duration2, duration3):
    pulse_sequence=[]
    for t in time:
        pulse_sequence.append(square(t, start=0, duration=duration1, area=pi )
                              +square(t, start=duration1, duration=duration2, area=2*pi)
                              +square(t, start=duration1+duration2,duration=duration3, area=pi))
    return pulse_sequence

'''if __name__=="__main__":
    time = np.linspace(0,100,1000)

    omega= double_square(time, duration1=20, area1=1, duration2= 20, area2=1/2)
    plt.plot(time, omega)
    plt.show()'''

