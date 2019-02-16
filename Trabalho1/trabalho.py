# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:49:23 2019

@author: gabic
"""

import numpy as np

n = 3
N = n**2
diagonal_principal = np.ones((n,), np.float64)*1
diagonal_r = np.ones((n-1,), np.float64)*2
diagonal_p = np.ones((n,), np.float64)*3

T = np.diagflat(diagonal_principal, 0) + np.diagflat(diagonal_r, 1)
I = np.diagflat(diagonal_p, 0)
print(T)
print("------")
print(I)
#print("------")
#print(A+B)

#A = 