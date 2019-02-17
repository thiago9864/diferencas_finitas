# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:49:23 2019

@author: gabic
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.pyplot import figure

#define o tamanho dos graficos
figure(num=None, figsize=(8, 6), dpi=72, facecolor='w', edgecolor='k')

#Definicao de valores
u = -4.0 #vento leste-oeste
v = 3.0 #vento sul-norte
h = 0.2 #espacamento da grade
dt = 0.2; #espaco de tempo 

n = 30 #quantidade de pontos
passos = 10 #quantos passos no tempo vai dar
temperatura_inicial = 25.0

def matrizEulerEstatico(n, u, v, h):
    
    p = (u-v)/h
    q = -u/h
    r = v/h
    
    diagonal_principal = np.ones((n,), np.float64) * p
    diagonal_r = np.ones((n-1,), np.float64) * r
    diagonal_p = np.ones((n,), np.float64) * q
    
    T = np.diagflat(diagonal_principal, 0) + np.diagflat(diagonal_r, 1)
    I = np.diagflat(diagonal_p, 0)
    
    diagonal_k = np.ones((n-1,), np.float64)
    K = np.diagflat(diagonal_k, -1)
    
    A = np.kron(np.identity(n), T) + np.kron(K, I)

    '''
    print(T)
    print("------")
    print(I)
    print("------")
    print(K)
    print("------")
    print(A)
    '''
    
    return A

def matrizDiferencaCentral(n, u, v, h, dt):
    
    p = -(u*dt)/(2.0*h)
    q = -(v*dt)/(2.0*h)
    
    diagonal_principal = np.ones((n,), np.float64)
    diagonal_q = np.ones((n-1,), np.float64) * q
    diagonal_p = np.ones((n,), np.float64) * p
    
    T = np.diagflat(diagonal_principal, 0) + np.diagflat(diagonal_q, 1) + np.diagflat(diagonal_q, -1) * -1
    I = np.diagflat(diagonal_p, 0)
    
    diagonal_k = np.ones((n-1,), np.float64)
    K = np.diagflat(diagonal_k, -1) * -1 + np.diagflat(diagonal_k, 1)
    
    A = np.kron(np.identity(n), T) + np.kron(K, I)

    '''
    print(T)
    print("------")
    print(I)
    print("------")
    print(K)
    print("------")
    print(A)
    '''
    
    return A   

#matriz = matrizEulerEstatico(n, u, v, h)
matriz = matrizDiferencaCentral(n, u, v, h, dt)


#vetor de vetores
T = np.zeros((passos+1, n**2), np.float64)

#vetor pra armazenar os dados de um ponto pro teste de estabilidade
posicao_estabilidade = np.zeros((passos+1), np.float64)
vetor_estabilidade = np.zeros((passos+1), np.float64)

#cria matriz com a temperatura inicial
T[0] = np.ones((n**2), np.float64) * temperatura_inicial


#print(T[0])
#print("------")
#print(matriz)

#parte da formula que nao muda
C = (matriz + np.identity(n**2)) * dt

#print("------")
#print(C)


#calcula a formula
for i in range(passos):
    T[i+1] = np.dot(C, T[i])

#print("------")
#print(T)

for k in range(passos+1):
    
    #converte de vetor pra matriz
    M = T[k].reshape((n, n))

    #pega um ponto que nao esta no meio
    i = int(n * 0.75)
    j = int(n * 0.75)
    
     #tira um ponto pra testar a estabilidade
    posicao_estabilidade[k] = k
    vetor_estabilidade[k] = M[i][j]
    
    plt.matshow(M, vmin=-temperatura_inicial, vmax=temperatura_inicial)
    plt.colorbar()
    plt.show()






#imprime o teste de estabilidade
plt.plot(
    posicao_estabilidade, vetor_estabilidade, 'r-' 
    )
plt.ylabel(u"valor") #esse 'u' antes da string é pra converter o texto pra unicode
plt.xlabel(u"passo")


#legendas do grafico    
#se_line = mlines.Line2D([], [], color='blue', marker='', markersize=0, label=u'Solução Exata')
#ac_line = mlines.Line2D([], [], color='red', marker='', markersize=0, label=u'Aproximação)')

#plt.legend(handles=[se_line, ac_line], loc='lower center')

'''Posicoes da legenda 
    upper right
    upper left
    lower left
    lower right
    right
    center left
    center right
    lower center
    upper center
    center
'''

plt.title(u"Temperatura no ponto pesquisado", )

#muda os limites dos eixos
#por: x_inicial, x_final, y_inicial, y_final
#plt.axis([0, 1, 0, 1.05])

plt.show()
