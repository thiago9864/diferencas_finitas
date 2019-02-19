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
u = 4.0 #vento leste-oeste
v = 3.0 #vento sul-norte
h = 0.2 #espacamento da grade
dt = 0.2; #espaco de tempo 

n = 30 #quantidade de pontos
passos = 50 #quantos passos no tempo vai dar
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

def contornoEuler(n, u, v, h, contorno):
    
    q = -u/h
    r = v/h
    V = np.zeros((n**2), np.float64)
    indice = 0
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i-1 == 0):
                V[indice] = V[indice] + contorno * q
            if(j == n):
                V[indice] = V[indice] + contorno * r
            indice += 1
    return V

#matriz = matrizEulerEstatico(n, u, v, h)
matriz = matrizDiferencaCentral(n, u, v, h, dt)

Q = contornoEuler(n, u, v, h, temperatura_inicial)

#print(Q)

#vetor de vetores
Ta = np.zeros((passos+1, n**2), np.float64)
Tb = np.zeros((passos+1, n**2), np.float64)
Tc = np.zeros((passos+1, n**2), np.float64)

#vetor pra armazenar os dados de um ponto pro teste de estabilidade
posicao_estabilidade = np.zeros((passos+1), np.float64)
vetor_estabilidade = np.zeros((passos+1), np.float64)
vetor_estabilidade_mais20 = np.zeros((passos+1), np.float64)
vetor_estabilidade_menos20 = np.zeros((passos+1), np.float64)

'''
Sistema:
    T(n+1) = (I + dt*A) * T(n) + Q
    T(0) = Temperatura inicial
    
Com:
    I: matriz identidade
    dt: variacao de tempo
    A: matriz de diferencas finitas
    T(n): matriz atual
    T(n+1): proxima matriz
'''    


#parte da formula que nao muda
#C = (I + dt*A)
C = (matriz + np.identity(n**2)) * dt

#Aqui ativa aquela variavel aleatoria que o professor pediu pra colocar
#usar True ou False
usarVetorAleatorio = True


#------ Temperatura a verificar -------


#cria matriz com a temperatura inicial
Ta[0] = np.ones((n**2), np.float64) * temperatura_inicial

#calcula a formula
for i in range(passos):
    if(usarVetorAleatorio):
        W = np.random.rand(n**2,)
        Ta[i+1] = np.dot(C, Ta[i]) + W
    else:
        Ta[i+1] = np.dot(C, Ta[i])
    

#------ Temperatura a verificar + 20 graus -------
        

#cria matriz com a temperatura inicial
Tb[0] = np.ones((n**2), np.float64) * (temperatura_inicial + 20)

#calcula a formula
for i in range(passos):
    if(usarVetorAleatorio):
        W = np.random.rand(n**2,)
        Tb[i+1] = np.dot(C, Tb[i]) + Q + W
    else:
        Tb[i+1] = np.dot(C, Tb[i]) + Q
    

#------ Temperatura a verificar - 20 graus -------
        

#cria matriz com a temperatura inicial
Tc[0] = np.ones((n**2), np.float64) * (temperatura_inicial - 20)

#calcula a formula
for i in range(passos):
    if(usarVetorAleatorio):
        W = np.random.rand(n**2,)
        Tc[i+1] = np.dot(C, Tc[i]) + Q + W
    else:
        Tc[i+1] = np.dot(C, Tc[i]) + Q
    



#imprime e separa pontos pra testar a estabilidade
for k in range(passos+1):
    
    #converte de vetor pra matriz
    Ma = Ta[k].reshape((n, n))
    Mb = Tb[k].reshape((n, n))
    Mc = Tc[k].reshape((n, n))

    #pega um ponto que nao esta no meio
    i = int(n * 0.75)
    j = int(n * 0.75)
    
     #tira um ponto pra testar a estabilidade
    posicao_estabilidade[k] = k * dt
    vetor_estabilidade[k] = Ma[i][j]
    vetor_estabilidade_mais20[k] = Mb[i][j]
    vetor_estabilidade_menos20[k] = Mc[i][j]
    
    #aqui imprime a matriz numa imagem colorida
    
    #plt.matshow(Ma, vmin=-temperatura_inicial, vmax=temperatura_inicial)
    plt.matshow(Ma)
    plt.colorbar()
    plt.show()
    




#------ Imprime o grafico de teste de estabilidade -------
    
plt.plot(
    posicao_estabilidade, vetor_estabilidade, 'r-' 
    )
plt.plot(
    posicao_estabilidade, vetor_estabilidade_mais20, 'g-' 
    )
plt.plot(
    posicao_estabilidade, vetor_estabilidade_menos20, 'b-' 
    )

plt.ylabel(u"temperatura") #esse 'u' antes da string é pra converter o texto pra unicode
plt.xlabel(u"tempo")


#legendas do grafico    
a_line = mlines.Line2D([], [], color='red', marker='', markersize=0, label=u'Temperatura')
b_line = mlines.Line2D([], [], color='green', marker='', markersize=0, label=u'Temperatura + 20 graus)')
c_line = mlines.Line2D([], [], color='blue', marker='', markersize=0, label=u'Temperatura - 20 graus)')

plt.legend(handles=[a_line, b_line, c_line], loc='upper right')

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
plt.show()
