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
kb=1.38e-23 #In SI Units
T=300; # Temperature in Kelvin
e=1.6e-19 #electronic charge
hbar=1.05e-34

mu=0*e #equilibrium chemical potential, input value in eV
E1=0.005*e #Setting the energy of the electron state being simulated
gamma1=5E-2*e # Coupling of the island with source. Enter values in electron volts
gamma2=5E-2*e # Coupling of the island with drain. Enter values in electron volts

n=3000 #Number of points in the Vd space
Evb=-3.5 #Lower limit of Vd
Evt=3.5 #Upper limit of Vd
nstates=4 #No. of single electron states in metal island 
Esb=-1.5*e #Energy of bottom state in metal island
Est=1.5*e #Energy of top state in metal island

#Start up stuff
I=np.zeros(n)
f2=np.zeros(n)

Vd=np.linspace(Evb,Evt,n)
E=np.linspace(Esb,Est,nstates)

for i in range(0,len(Vd)):
    V=Vd[i]
    mu1=mu
    mu2=mu-e*V
    I[i]=(e/hbar)*(gamma1*gamma2/(gamma1+gamma2))*sum(fer(E,mu1,T)-fer(E,mu2,T))


#Plot of the data
fig=plt.figure()
VdI=fig.add_subplot(111)
p=VdI.plot(Vd,I)
VdI.set_xlabel('Vd values')
VdI.set_ylabel('I values')
VdI.set_title('Plot of I vs. Vd for an SET')
fig.show    
              
              
              
             
              
              