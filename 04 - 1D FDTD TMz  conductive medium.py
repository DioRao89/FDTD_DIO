# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 01:06:30 2018

@author: Dionisio
TMz Basico Gaussian pulse
dieletric medium
before: explain why 0.5
"""
#import numpy as np
from matplotlib import pyplot as plt
from math import exp,sin,pi
#import create_gif
ez = []
hy = []
eps = []
sig = []##############
nx = 801
nt = 600
t0 = 40
wid = 12
fs = 700e6
lamb = 3e8/fs 
dx= lamb/70
dt = dx/(2*3e8) ###########
isrc = int((nx)/2)
medium = isrc+80
vet_x = list(range(0,nx))
epsr = 2 
sigma = 0.04###############
epsilon = 8.85419e-12 ##############
es  = (dt*sigma)/(2*epsr*epsilon)#############
def savequad(quad,vet_x,campo,n, medium):
    namequad = "quad" +  str(quad)
    plt.clf()
    plt.xlabel("X")
    plt.ylabel("Ez")
    time = "t = " + str(n)
    plt.title(time)
    plt.ylim(-1,1)
    plt.axvline(medium, color='r')
    plt.plot(vet_x,campo)# mandar listas para definir os eixos
    # define axis limits
    plt.savefig(namequad)
    
for i in range(0,nx):
    ez.append(0)
    hy.append(0)
    eps.append(0)
    sig.append(0)################
    
for i in range(0,nx):
    eps[i] = 0.5
    sig[i] = 1.0
    if i >= medium:
        eps[i] = 0.5/(epsr*(1+es))########
        sig[i] = (1-es)/(1+es)##########

for n in range(0,nt):
    for i in range(1,nx):
        ez[i] = sig[i]*ez[i] + eps[i]*(hy[i-1]-hy[i])######### 
    ez[0] = 0     #PEC
    ez[nx-1] = 0  #PEC
   # pulse1 = exp(-0.5*((t0-n)/wid)**2)
    #ez[isrc] = pulse #hard source
    pulse1 = sin(2*pi*fs*dt*n)
 #   ez[isrc+80] += pulse1 #soft source
    ez[isrc-40] += pulse1 #soft source
        
    if float(n)%5 == 0: 
        savequad(n,vet_x,ez,n,medium)
        print (n,ez[isrc+20])
    for i in range(0,nx-1):
        hy[i] =  hy[i] + 0.5*(ez[i] - ez[i+1])
#create_gif()