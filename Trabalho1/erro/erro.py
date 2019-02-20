# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:11:43 2019

@author: gabic
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.pyplot import figure
n1=4
#temperatura_exata =np.array([26.22,26.83,25.96,22.93,21.84,21.46,20.5], np.float64) 
#vetor_estabilidade=np.array([ 26.22,27.12337588,27.54682948,25.74461591,19.93455332,15.57173741,10.57125107], np.float64)
#hora=[0,1,2,3,4,5,6]
#erro=vetor_estabilidade-temperatura_exata
#print(erro)
#erro2=vetor_estabilidade[1]-temperatura_exata
media1=np.ones((n1,n1), np.float64) * 26.83
matriz1=np.array( [[ 19.21702231,20.12724808,19.30953808,18.8417872 ],[ 26.3858533,26.58498325,27.00076519,25.85184652],[ 26.70370107,27.07849351,26.57885735,26.18186603],[ 27.00913184,27.1054638,26.93502346,25.99511572]],np.float64)
#print("media1:", media)
erro1=np.zeros((n1,n1), np.float64)
erro2=media1-matriz1
valor2=np.linalg.norm(erro2)
print("valor1:", valor2)

n2=8
media2=np.ones((n2,n2), np.float64) * 26.83
#print(media2)
matriz2=np.array( [[12.3,12.4,12.9,12.4,12.7,12.2,12.5,10.9],[26.2,26.8,26.7,26.9,27.2,26.3,26.7,25.2 ],[27.0, 26.4, 26.4, 26.6, 26.4, 26.8, 27.0, 25.1],[26.3, 27.1, 26.6, 27.2, 26.7, 26.5, 27.1, 25.6],[26.6, 26.4, 26.3, 26.3, 26.5, 26.8 ,26.8, 25.1 ],[26.3, 26.9, 27.1, 26.5, 26.7, 26.3, 27.1, 25.7],[26.5, 26.8, 26.9, 26.3, 27.1, 27.0, 26.8, 25.2 ],[26.9, 27.2, 27.0, 27.2, 26.7, 27.2, 26.5, 25.6 ]],np.float64)
#print("media2:", media2)
erro3=media2-matriz2
valor2=np.linalg.norm(erro3)
print("valor2:", valor2)

n3=12
media3=np.ones((n3,n3), np.float64) * 26.83
#print("matriz media3:", media3)
matriz3=np.array([[5.8,  5.7,  6.0,  5.6,  5.1,  5.3,  5.1,  5.8,  6.0,  5.7,  6.0,  4.0],[26.3, 26.7, 27.2, 26.4, 26.5, 26.4, 26.4, 26.9, 26.9, 26.6, 27.1, 24.8 ],[27.2, 26.6, 27.0, 26.6, 26.2, 27.1, 26.5, 26.3, 27.2, 26.9, 27.0, 24.9],[26.9, 26.6, 26.7, 27.1, 26.6, 26.7, 27.1, 26.4, 27.2, 26.9, 26.4, 25.0],[27.1, 27.0, 26.6, 26.3, 27.1, 26.6, 27.1, 26.7, 26.3, 26.3, 26.8, 24.4 ],[26.7, 27.0,26.5, 26.6, 27.1, 26.7, 26.8, 26.3, 26.8, 26.7, 26.9, 25.1 ],[26.8, 26.8, 26.4, 26.8, 27.2, 27.0, 26.2, 26.8, 27.1, 27.2, 27.0, 24.8 ],[27.2, 26.2, 26.3, 27.2, 26.8, 26.8, 26.9, 26.7, 27.1, 26.7, 26.3, 24.4 ],[27.2, 27.0, 26.3, 26.9, 26.5, 26.6, 26.7, 26.3, 26.5, 26.7, 27.0, 24.6 ],[26.4, 26.9 ,26.9 ,26.9, 26.5, 27.1, 27.1, 27.0, 26.6, 26.3, 26.3, 24.8],[27.1, 27.1, 26.5 ,27.2, 26.3, 27.0, 26.3, 26.7, 27.2, 26.4, 27.0, 25.0 ],[26.8, 26.3, 27.2, 27.0, 26.9, 26.3 ,26.6, 27.1, 26.4, 27.1, 26.3, 24.5 ]],np.float64)
#print("media2:", media2)
erro4=media3-matriz3
valor2=np.linalg.norm(erro4)
print("valor2:", valor2)


vetor_erro=np.array([15.0290827812,41.4138334376,74.2925406754], np.float64)
vetor=np.array([4,8,12], np.float64)

plt.plot(vetor, vetor_erro, label='Erro com n=4,8,12')
plt.title("Valor do erro para n=4,8,12")
plt.ylabel('Erro')
plt.savefig("erro.png")
plt.show()

