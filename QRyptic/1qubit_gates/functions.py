import numpy as np
import matplotlib.pyplot as plt
from math import *
import cmath

def right_hand_side(y, omega1, delta=0):
    
    matrix = np.array(
        [[0, 1.j * 0.5 * omega1], [1.j * 0.5 * omega1.conjugate(), -1.j * delta]])
    return np.einsum('ij,j->i', matrix, y)

def runge_kutta(time, omega2,  delta=0, input = np.array([1, 0])):
    dt = time[2] - time[0]
    y_list = [input]
    for ii  in range(0, len(time)-2, 2):
        k1 = right_hand_side(input, omega2[ii], delta)
        k2 = right_hand_side(input + dt * k1 / 2, omega2[ii], delta)
        k3 = right_hand_side(input + dt * k2 / 2, omega2[ii], delta)
        k4 = right_hand_side(input + dt * k3, omega2[ii], delta)
        y_new = input + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        input = y_new

        y_list.append(y_new)
        
    
    y_list1 = np.array(y_list)
    
    return y_list1[-1]

def gate(time, omega3, delta):
    basis = np.eye(2)
   
    output=[]
    for input in basis:
    
        output.append(runge_kutta(time, omega2=omega3, delta=delta, input=input))
    
    output = np.squeeze(np.vstack(output)) 
    return output.T