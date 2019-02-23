import numpy as np

class RetroSubstituicao():

    def executar(self, M, B, dataType):
        if(len(M)==0):
            return 0
        
        ordem = len(M[0])
        temp = 0
        passos = 0
        
        #cria array de solucao
        sol = np.zeros((ordem,), dtype=dataType)
        
        #checa se e superior
        isSuperior = (M[ordem-1][0] == 0)
        
        #percorre as linhas da matriz (ta funcionando)
        for n in range(0, ordem):  
            
            #define o i se for superior ou inferior
            if(isSuperior):
                i = ordem - n - 1
            else:
                i = n
            
            #valor do vetor solucao da linha correspondente
            temp = B[i]
            
            #soma os valores exceto o valor do pivo
            for j in range(0, ordem):
                if(j != i):
                    temp += sol[j] * M[i][j] * -1
                    passos += 1
                    
                
            #calcula a solucao da linha, usando a soma e o valor do pivo
            sol[i] = temp / M[i][i]
            

            
        return [list(sol), passos]