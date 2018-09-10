# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 01:06:30 2018

@author: Dionisio
TMz Basico Gaussian pulse
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 20:10:45 2018

@author: Cliente

FDTD 1D EX HY
TMx
"""
#import numpy as np
from matplotlib import pyplot as plt
from math import exp,sin,pi
#import create_gif 

ez = []
hy = []

nx = 801
nt = 600
t0 = 40
wid = 12
fs = 0.5/t0
isrc = int((nx)/2)
vet_x = list(range(0,nx))

def savequad(quad,vet_x,campo,n):
    namequad = "quad" +  str(quad)
    plt.clf()
    plt.xlabel("X")
    plt.ylabel("Ez")
    time = "t = " + str(n)
    plt.title(time)
    plt.ylim(-2,2)
    plt.plot(vet_x,campo)# mandar listas para definir os eixos
    # define axis limits
    plt.savefig(namequad)
    

for i in range(0,nx):
    ez.append(0)
    hy.append(0)

for n in range(0,nt):
    for i in range(1,nx):
        ez[i] = ez[i] + 0.5*(hy[i-1]-hy[i])
    ez[0] = 0     #PEC
    ez[nx-1] = 0  #PEC
    pulse1 = exp(-0.5*((t0-n)/wid)**2)
    #ez[isrc] = pulse #hard source
    pulse2 = sin(2*pi*fs*n)
    ez[isrc+80] += pulse1 #soft source
    ez[isrc-80] += pulse2 #soft source
        
    if float(n)%5 == 0: 
        savequad(n,vet_x,ez,n)
        print (n,ez[isrc+20])
    for i in range(0,nx-1):
        hy[i] =  hy[i] + 0.5*(ez[i] - ez[i+1])
    
#    create_gif()
    
