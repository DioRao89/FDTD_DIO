"""
Created on Wed Aug 22 01:06:30 2018

@author: Dionisio
TMz Basico Gaussian pulse
"""

from matplotlib import pyplot as plt
from math import exp

ez = [] # inicializando vetor campo eletrico
hy = [] # inicializando vetor campo magnetico

nx = 201 #maximo espaco
nt = 600 #maximo tempo
t0 = 40 # Ponto central do pulso
wid = 12 #largura do pulso

isrc = int((nx)/2) #posicao da fonte
vet_x = list(range(0,nx)) #vetor do espaco
#quad = tempo, vet_x = espaco, campo = amplitudes
def savequad(quad,vet_x,campo):
    namequad = "quad" +  str(quad)
    plt.clf() #limpa o grafico antigo
    plt.xlabel("X")
    plt.ylabel("Ez")
    #mandar listas para definir os eixos
    plt.plot(vet_x,campo) 
    plt.savefig(namequad)
#zerando todos os valores dos campos E e H
for i in range(0,nx):
    ez.append(0)
    hy.append(0)

for n in range(0,nt): #laco do tempo
    for i in range(1,nx): #laco do espaco para o campo E
        ez[i] = ez[i] + 0.5*(hy[i-1]-hy[i])
    ez[0] = 0     #PEC - condutor eletrico perfeito
    ez[nx-1] = 0  #PEC
    pulse = exp(-0.5*((t0-n)/wid)**2)
    #ez[isrc] = pulse #hard source
    # += atualiza o valor antigo da componente de campo
    ez[isrc] += pulse #soft source 
     
    if n%5 == 0: 
        savequad(n,vet_x,ez),print (n,ez[isrc+20])
    for i in range(0,nx-1):
        hy[i] =  hy[i] + 0.5*(ez[i] - ez[i+1])
    
    
#    create_gif()
    
