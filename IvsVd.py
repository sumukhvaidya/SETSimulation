# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:29:24 2019

@author: sumukhvaidya
"""
import numpy as np
import matplotlib.pyplot as plt
#import scipy

def fer(E, mu, T): #Define Fermi function for Energy E, chemical potential mu, Temperature T, ALL IN SI
    return (1/(1+np.exp((E-mu)/(kb*T))))

#Define constants and setup things
hbar=1.05e-34
kb=1.38e-23 #In SI Units
T=300; # Temperature in Kelvin
e=1.6e-19 #electronic charge
n=3000 #Number of points in the linspace
mu=0.5*e #equilibrium chemical potential, input value in eV
E=0.005*e #Setting the energy of the electron state being simulated
gamma1=5E-2*e # Coupling of the island with source. Enter values in electron volts
gamma2=5E-2*e # Coupling of the island with drain. Enter values in electron volts

#Start up stuff
I=np.zeros(n)
f2=np.zeros(n)
Vd=np.linspace(-.5,1.5,n)

for i in range(0,len(Vd)):
    V=Vd[i]
    mu1=mu
    mu2=mu-e*V
    f1=fer(E,mu1,T)
    f2=fer(E,mu2,T)
    I[i]=(e/hbar)*(gamma1*gamma2/(gamma1+gamma2))*(f1-f2)

#Plot of the data
fig=plt.figure()
VdI=fig.add_subplot(111)
p=VdI.plot(Vd,I)
VdI.set_xlabel('Vd values')
VdI.set_ylabel('I values')
VdI.set_title('Plot of I vs. Vd for an SET')
fig.show    
              
              
              
             
              
              