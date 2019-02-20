# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:49:23 2019

@author: thiagoalmeida
"""

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.pyplot import figure
import numpy as np

#define o tamanho dos graficos
figure(num=None, figsize=(8, 6), dpi=72, facecolor='w', edgecolor='k')

###### Leitura do arquivo de dados #######

arquivo = open("BRB1805ED.csv", 'r');

x = np.empty((0,), dtype=np.float128)
y = np.empty((0,), dtype=np.float128)

#tive que fazer isso pra rodar no Linux
conteudo = arquivo.readlines();
string = ""
for i in conteudo:
   string += i


#prestar atenção nisso, se for windows deve ter q mudar esse if
if(string.find('\r') >= 0):
    #cai nesse se for Linux
    linhas = string.split('\r')
else:
    #cai nesse se for mac
    linhas = string.split('\n')
    
#------ filtro do grafico --------
ano = 2018
dia = 121 #01/05/2018
hora_inicio = 19
hora_fim = 24

def corrigeNumero(dado):
    s = dado.replace(',', '.')
    if(s != "" and s != "N/A"):
        return float(s)
    return 0


indice=0
print ("d_min, tp_sfc, ws_10m, wd_10m | hora indice temp  u  v")

for linha in linhas:
    dados = linha.split(';')

    if(len(dados) == 16):
        d_id = corrigeNumero(dados[0])
        d_year = corrigeNumero(dados[1])
        d_day = corrigeNumero(dados[2])
        d_min = corrigeNumero(dados[3])
        tp_sfc = corrigeNumero(dados[10])
        ws_10m = corrigeNumero(dados[14])
        wd_10m = corrigeNumero(dados[15])
        
        if(d_year == ano and d_day == dia):
            #print(dados)
            #adiciona ao array
            if(d_min >= hora_inicio*60 and d_min <= hora_fim*60):
                a = corrigeNumero(dados[3])
                b = corrigeNumero(dados[10])
                x = np.append(x, np.float64(a))
                y = np.append(y, np.float64(b))
                
                if((d_min-1) % 60 == 0 or d_min==1439):
                    u = np.cos(np.deg2rad(wd_10m)) * ws_10m
                    v = np.sin(np.deg2rad(wd_10m)) * ws_10m
                    hora = np.round(d_min / 60)
                    print (d_min, tp_sfc, ws_10m, wd_10m, "|", hora, indice, tp_sfc, u, v)
                    indice += 1
        
    
#------ Imprime o grafico de teste de estabilidade -------

'''    
id year day min glo_avg dir_avg diff_avg lw_avg par_avg lux_avg tp_sfc humid press rain ws_10m wd_10m
'''
plt.plot(
    x, y, 'r-' 
    )

plt.ylabel(u"tp_sfc") #esse 'u' antes da string é pra converter o texto pra unicode
plt.xlabel(u"min")


#legendas do grafico    
a_line = mlines.Line2D([], [], color='red', marker='', markersize=0, label=u'Temperatura')
b_line = mlines.Line2D([], [], color='green', marker='', markersize=0, label=u'Temperatura + 5 graus)')
c_line = mlines.Line2D([], [], color='blue', marker='', markersize=0, label=u'Temperatura - 5 graus)')

plt.legend(handles=[a_line, b_line, c_line], loc='center')

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