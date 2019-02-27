#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 19:23:48 2019

@author: thiagoalmeida
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.pyplot import figure
from metodos_numericos.LU import LU

def imprimeMatriz(matriz):
    ordem = len(matriz[0])
    casas_decimais = 1
    just_space = 7
    for i in range(ordem):
        for j in range(ordem):
            fmt_string = "{0:."+str(casas_decimais)+"f}"
            sys.stdout.write(fmt_string.format(matriz[i][j]).ljust(just_space))
        sys.stdout.flush()
        print("")


#######################################
########## Definição Inicial ##########
#######################################
    
    
#ordem da matriz discretizada    
N = 10

#coordenadas polares
hp = 1.0 / N
kp = (np.pi*2.0) / N

#coordenadas retangulares
hr = 1.0 / N
kr = 1.0 / N
    


#########################################################
########## Cria matriz por coordenadas polares ##########
#########################################################



#Monta coeficientes (como na pag 2)
def a(i,h): 
    return (1.0/h**2) + (1.0 / (2.0 * i * h**2))

def b(i,h):
    return (1.0/h**2) - (1.0 / (2.0 * i * h**2))

def c(i, h, k):
    return (2.0/h**2) + (2.0 / ((i * h)**2 * k**2))

def d(i, h, k):
    return (1.0 / ((i * h)**2 * k**2))

#Matriz T
#declara variaveis
diagonal_principal = np.zeros((N,), np.float64)
diagonal_superior = np.zeros((N-1,), np.float64)
diagonal_inferior = np.zeros((N-1,), np.float64)

#preenche diagonal principal da matriz T
for i in range(N):
    diagonal_principal[i] = c(i+1, hp, kp) * -1
    
#preenche as diagonais secundarias da matriz T
for i in range(N-1):
    diagonal_superior[i] = a(i+1, hp)
    diagonal_inferior[i] = b(i+1, hp)

#monta a matriz T
T = np.diagflat(diagonal_principal, 0) + np.diagflat(diagonal_superior, 1) + np.diagflat(diagonal_inferior, -1)

#Matriz I
#declara variavel
diagonal_principal = np.zeros((N,), np.float64)

#preenche diagonal da matriz I
for i in range(N):
    diagonal_principal[i] = d(i+1, hp, kp)
    
#monta matriz I
I = np.diagflat(diagonal_principal, 0)

#Matriz completa
k_diag = np.ones((N-1,), np.float64)
k_sup = np.diagflat(k_diag, 1)
k_inf = np.diagflat(k_diag, -1)

#usa produto eletronico
Ap = np.kron(np.identity(N), T) + np.kron(k_sup, I) + np.kron(k_inf, I)

'''
print ("\n--- Cria matriz por coordenadas polares ---\n")
print ("--- Matriz T ---\n")
print(T)
print ("\n--- Matriz I ---\n")
print(I)
print ("\n--- Matriz Polar Completa ---\n")
imprimeMatriz(Ap)
'''


##############################################################
########## Cria matriz por coordenadas retangulares ##########
##############################################################


#Monta coeficientes (como na pag 4)
a = (1.0/hr**2)
b = (2.0 / hr**2) + (2.0 / kr**2)
c = (1.0/kr**2)

#Matriz T
diagonal_principal = np.ones((N,), np.float64) * b * -1.0
diagonal_superior = np.ones((N-1,), np.float64) * a
diagonal_inferior = np.ones((N-1,), np.float64) * a

T = np.diagflat(diagonal_principal, 0) + np.diagflat(diagonal_superior, 1) + np.diagflat(diagonal_inferior, -1)

#Matriz I
diagonal_principal = np.ones((N,), np.float64) * c

I = np.diagflat(diagonal_principal, 0)

#Matriz completa
k_diag = np.ones((N-1,), np.float64)
k_sup = np.diagflat(k_diag, 1)
k_inf = np.diagflat(k_diag, -1)

#usa produto eletronico
Ar = np.kron(np.identity(N), T) + np.kron(k_sup, I) + np.kron(k_inf, I)

'''
print ("\n--- Cria matriz por coordenadas retangulares ---")
print ("\n--- Matriz T ---\n")
print(T)
print ("\n--- Matriz I ---\n")
print(I)
print ("\n--- Matriz Retangular Completa ---\n")
imprimeMatriz(Ar)
'''

###########################################
########## Resolucao do Problema ##########
###########################################


'''
O problema dado resultou nos dois casos em um sistema AU = F
Fazendo as considerações

q(r, theta) = 20
e g=0

para o sistema com coordenadas polares, e

f(x, y) = 20
e g=0

para p sistema com coordenadas retangulares, temos:
'''

F = np.ones(N**2, np.float64)*20.0

#calcula sistema com coordenadas polares usando LU
Up = LU().executar(Ap, F, np.float64)

#calcula sistema com coordenadas retangulares usando LU
Ur = LU().executar(Ar, F, np.float64)

#monta vetor X pra plotar um grafico
X = range(N**2)



###########################################
########## Geracao de graficos ############
###########################################

#define tamanho da figura
figure(num=None, figsize=(8, 6), dpi=72, facecolor='w', edgecolor='k')

plt.plot(
    X, Up, 'r-' 
    )
plt.plot(
    X, Ur, 'g-' 
    )

plt.ylabel(u"f") #esse 'u' antes da string é pra converter o texto pra unicode
plt.xlabel(u"x")


#legendas do grafico    
a_line = mlines.Line2D([], [], color='red', marker='', linestyle='-', markersize=0, label=u'Solução com coordenadas polares')
b_line = mlines.Line2D([], [], color='green', marker='', linestyle='-', markersize=0, label=u'Solução com coordenadas retangulares')

plt.legend(handles=[a_line, b_line], loc='upper right')

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

plt.title(u"Trabalho 2 - Diferenças Finitas (N="+str(N)+")", )
plt.show()