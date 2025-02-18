## Introduction

In the theory of quantum optics, it is proven that various quantum gates can be formulated by manipulating the pulse area $\theta$ of the interaction of the Rydberg atom with the field, called Rabi pulses. Specifically, the atom and the cavity mode can be thought of as qubits and the hamiltonian that describe the evolution of this system is:
H = $\Delta$(t) |e><e| - $1 / 2$ * $\Omega$(t) |e><g| + hermitian_conjugate
Using arithmetic solutions, specifically the runge-kutta method, I calculated the effects of this hamiltonian for different t durations and different $\Omega$ functions. Until now, I have assumed resonance, meaning  $\Delta$(t)=0 for the sake of simplicity. The gates that are I have depicted in this project are the X and Y Pauli gates and the Hadamard gate (and of course the unity as a starting point). In this theoretical model, my simulations show perfect alignment of the gates as we know them from quantum information theory with the Rabi pulses realisation.
The same model can be used to simulate multiple qubit gates which is something that I will probably implement in the future.

## Contents

*in order of importance*
1) Functions
2) Pulses
3) Unity Gate
4) Gate_X
5) Gate_Y
6) Gate_Z
7) Gate_Hadamard

## Instrunctions

Running in a new session, 1st the functions file and then the Pulses, the kerner is initiallized to produce all the other gates when each respective file is run. These 2 are needed for initializing the session. A good update will be to set up the functions and pulses scripts to be importable to the gate scripts.

## Requirements

The only external libraries needed are numpy and matplotlib.pyplot.






