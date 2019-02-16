# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:49:23 2019

@author: gabic
"""

import numpy as np
import matplotlib.pyplot as plt

#Definicao de valores
u = 1.0 #vento leste-oeste
v = 1.0 #vento sul-norte
h = 0.5 #espacamento da grade

def matrizEulerEstatico(n, u, v, h):
    
    p = 1#(u-v)/h
    q = 3#-u/h
    r = 2#v/h
    
    diagonal_principal = np.ones((n,), np.float64) * p
    diagonal_r = np.ones((n-1,), np.float64) * r
    diagonal_p = np.ones((n,), np.float64) * q
    
    T = np.diagflat(diagonal_principal, 0) + np.diagflat(diagonal_r, 1)
    I = np.diagflat(diagonal_p, 0)
    
    diagonal_k = np.ones((n-1,), np.float64)
    K = np.diagflat(diagonal_k, -1)
    
    A = np.kron(np.identity(n), T) + np.kron(K, I)

    
    print(T)
    print("------")
    print(I)
    print("------")
    print(K)
    print("------")
    print(A)
    
    return A

def matrizDiferencaCentral(n, u, v, h):
    
    p = 1
    q = 3
    r = 2
    
    diagonal_principal = np.ones((n,), np.float64) * p
    diagonal_r = np.ones((n-1,), np.float64) * r
    diagonal_p = np.ones((n,), np.float64) * q
    
    T = np.diagflat(diagonal_principal, 0) + np.diagflat(diagonal_r, 1) + np.diagflat(diagonal_r, -1) * -1
    I = np.diagflat(diagonal_p, 0)
    
    diagonal_k = np.ones((n-1,), np.float64)
    K = np.diagflat(diagonal_k, -1) * -1 + np.diagflat(diagonal_k, 1)
    
    A = np.kron(np.identity(n), T) + np.kron(K, I)

    
    print(T)
    print("------")
    print(I)
    print("------")
    print(K)
    print("------")
    print(A)
    
    return A   

matriz = matrizEulerEstatico(3, u, v, h)
#matriz = matrizDiferencaCentral(3, u, v, h)