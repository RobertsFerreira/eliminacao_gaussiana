from numpy import mat
from models.matriz import Matriz

class MatrizOperations:
    
    def validateDeterminante(self, determinante):
        if(determinante != 0):
            return True
        else:
            return False

    def algoritmoGauss(self, matriz):
        matrizBase = self.__generateNewMatriz__(matriz)
        matrizResultante =  self.__generateNewMatriz__(matriz)
        if(matriz[0][0] != 0):
            lenMatriz = matriz.__len__()
            for k in range(0, lenMatriz - 1):
                for i in range(k+1, lenMatriz):
                    m = matriz[i][k] / matriz[k][k]
                    for j in range(k, lenMatriz + 1):
                        a = matrizBase[i][j] - (m * matrizBase[k][j])
                        matrizResultante[i][j] = a
                matrizBase = [temp.copy() for temp in matrizResultante]
            return matrizBase
        else:
            print("Matriz Inválida")


    def triangularSuperior(self, matriz):
        results = []
        pos = matriz.__len__() - 1
        result = matriz[pos][pos+1]/matriz[pos][pos]
        results.append(result)
        for i in range(pos-1, -1, -1):
            j = 0
            # print(matriz[i][pos+1])
            # print(matriz[i][pos])
            # print(matriz[i][i])
            b = (matriz[i][pos+1] - (matriz[i][pos] * results[j]))/matriz[i][i]
            results.append(b)
            j += 1
        results.reverse()
        return results

    def __generateNewMatriz__(self, matriz):
        matrizNew = [] 
        matrizNew = [temp.copy() for temp in matriz]
        return matrizNew
