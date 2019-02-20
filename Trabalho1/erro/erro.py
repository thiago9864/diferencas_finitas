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

temperatura_exata =np.array([26.22,26.83,25.96,22.93,21.84,21.46,20.5], np.float64) 
vetor_estabilidade=np.array([ 26.22,27.12337588,27.54682948,25.74461591,19.93455332,15.57173741,10.57125107], np.float64)
hora=[0,1,2,3,4,5,6]
#erro=vetor_estabilidade-temperatura_exata
#print(erro)
#erro2=vetor_estabilidade[1]-temperatura_exata
erro1=vetor_estabilidade[0]-temperatura_exata
print(erro1)
erro2=vetor_estabilidade[1]-temperatura_exata
erro3=vetor_estabilidade[2]-temperatura_exata
erro4=vetor_estabilidade[3]-temperatura_exata
erro5=vetor_estabilidade[4]-temperatura_exata
erro6=vetor_estabilidade[5]-temperatura_exata
erro7=vetor_estabilidade[6]-temperatura_exata
