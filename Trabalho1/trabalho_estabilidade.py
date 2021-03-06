# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:49:23 2019

@author: gabic
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.pyplot import figure

#define o tamanho dos graficos

figure(num=None, figsize=(8, 6), dpi=72, facecolor='w', edgecolor='k')

arr_u = [-0.1, -0.05, -0.025, -0.0125]
arr_v = [0.5, 0.25, 0.125, 0.0625]

#Definicao de valores
dt = 1 #espaco de tempo 
n = 10 #quantidade de pontos
u = arr_u[3]
v = arr_v[0]

passos = 200 #quantos passos no tempo vai dar
temperatura_inicial = 26.8

h = 10.0/n #espacamento da grade

def imprimeMatriz(matriz):
        ordem = len(matriz[0])
        just_space = 5
        for i in range(ordem):
            for j in range(ordem):
                sys.stdout.write("{0:.1f}".format(matriz[i][j]).ljust(just_space))
            #sys.stdout.write("| " + repr(vetor_solucao[i]).ljust(just_space))
            sys.stdout.flush()
            print("")
        print("--------------------------")

def matrizEuler(n, u, v, h, dt):
    
    p = 1 - ((u-v)*(dt/h))
    q = (u*dt) / h
    r = -(v*dt) / h    
    
    diagonal_principal = np.ones((n,), np.float64) * p
    diagonal_q = np.ones((n-1,), np.float64) * q
    diagonal_r = np.ones((n,), np.float64) * r
    
    T = np.diagflat(diagonal_principal, 0) + np.diagflat(diagonal_q, -1)
    I = np.diagflat(diagonal_r, 0)
    
    diagonal_k = np.ones((n-1,), np.float64)
    K = np.diagflat(diagonal_k, 1)
    
    A = np.kron(np.identity(n), T) + np.kron(K, I)

    '''
    print(T)
    print("------")
    print(I)
    print("------")
    print(K)
    print("------")
    imprimeMatriz(A)
    '''
    
    return A

def matrizEulerEstatico(n, u, v, h):
    
    p = (u-v)/h
    q = -u/h
    r = v/h
    
    diagonal_principal = np.ones((n,), np.float64) * p
    diagonal_r = np.ones((n-1,), np.float64) * r
    diagonal_q = np.ones((n,), np.float64) * q
    
    T = np.diagflat(diagonal_principal, 0) + np.diagflat(diagonal_r, 1)
    I = np.diagflat(diagonal_q, 0)
    
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
    imprimeMatriz(A)
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
    imprimeMatriz(A)
    '''
    
    return A   


#vetor de vetores
Ta = np.zeros((passos+1, n**2), np.float64)
Tb = np.zeros((passos+1, n**2), np.float64)
Tc = np.zeros((passos+1, n**2), np.float64)

temperatura_media = np.zeros((passos+1), np.float64)

#vetor pra armazenar os dados de um ponto pro teste de estabilidade
posicao_estabilidade = np.zeros((passos+1), np.float64)
vetor_estabilidade = np.zeros((passos+1), np.float64)
vetor_estabilidade_mais20 = np.zeros((passos+1), np.float64)
vetor_estabilidade_menos20 = np.zeros((passos+1), np.float64)

'''
Sistema:
    T(n+1) = (I + dt*A) * T(n)
    T(0) = Temperatura inicial
    
Com:
    I: matriz identidade
    dt: variacao de tempo
    A: matriz de diferencas finitas
    T(n): matriz atual
    T(n+1): proxima matriz
'''    



    
matriz = matrizEulerEstatico(n, u, v, h)
#matriz = matrizEuler(n, u, v, h, dt)
#matriz = matrizDiferencaCentral(n, u, v, h, dt)

C = np.identity(n**2) + (matriz * dt)


#Aqui ativa aquela variavel aleatoria que o professor pediu pra colocar
#usar True ou False
usarVetorAleatorio = False


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
Tb[0] = np.ones((n**2), np.float64) * (temperatura_inicial + 5)

#calcula a formula
for i in range(passos):
    
    if(usarVetorAleatorio):
        W = np.random.rand(n**2,)
        Tb[i+1] = np.dot(C, Tb[i]) + W
    else:
        Tb[i+1] = np.dot(C, Tb[i])
    

#------ Temperatura a verificar - 20 graus -------
        

#cria matriz com a temperatura inicial
Tc[0] = np.ones((n**2), np.float64) * (temperatura_inicial - 5)

#calcula a formula
for i in range(passos):
    
    if(usarVetorAleatorio):
        W = np.random.rand(n**2,)
        Tc[i+1] = np.dot(C, Tc[i]) + W
    else:
        Tc[i+1] = np.dot(C, Tc[i])
    



#pega um ponto que nao esta no meio
iP = int(n * 0.25)
jP = int(n * 0.45)

#imprime e separa pontos pra testar a estabilidade
for k in range(passos+1):
    
    #converte de vetor pra matriz
    Ma = Ta[k].reshape((n, n))
    Mb = Tb[k].reshape((n, n))
    Mc = Tc[k].reshape((n, n))

    
     #tira um ponto pra testar a estabilidade
    posicao_estabilidade[k] = k * dt
    vetor_estabilidade[k] = Ma[iP][jP]
    vetor_estabilidade_mais20[k] = Mb[iP][jP]
    vetor_estabilidade_menos20[k] = Mc[iP][jP]
    
    #aqui imprime a matriz numa imagem colorida
    '''
    #plt.switch_backend('Agg')
    plt.matshow(Ma, vmin=-temperatura_inicial, vmax=temperatura_inicial)
    #plt.matshow(Ma)
    plt.colorbar()
    plt.show()
    #plt.savefig("matriz/matriz" + str(k) + ".png")
    '''
    temperatura_media[k] = np.mean(Ma)
        

#------ Imprime o grafico de teste de estabilidade -------
plt.switch_backend('Agg')
figure(num=None, figsize=(8, 6), dpi=72, facecolor='w', edgecolor='k')

plt.plot(
    posicao_estabilidade, vetor_estabilidade, 'r-' 
    )
plt.plot(
    posicao_estabilidade, vetor_estabilidade_mais20, 'g--' 
    )
plt.plot(
    posicao_estabilidade, vetor_estabilidade_menos20, 'b--' 
    )

plt.ylabel(u"temperatura") #esse 'u' antes da string é pra converter o texto pra unicode
plt.xlabel(u"tempo")


#legendas do grafico    
a_line = mlines.Line2D([], [], color='red', marker='', linestyle='-', markersize=0, label=u'Temperatura')
b_line = mlines.Line2D([], [], color='green', marker='', linestyle='--', markersize=0, label=u'Temperatura + 5 graus)')
c_line = mlines.Line2D([], [], color='blue', marker='', linestyle='--', markersize=0, label=u'Temperatura - 5 graus)')

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

plt.title(u"Temperatura no ponto ("+str(iP)+","+str(jP)+") (n="+str(n)+")", )
plt.show()
plt.savefig("estabilidade/u_" + str(u) + "v_" +str(v) + ".png")
