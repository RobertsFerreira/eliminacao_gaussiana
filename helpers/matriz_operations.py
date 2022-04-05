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
        x1 = matriz[pos][pos+1]/matriz[pos][pos]
        results.append(x1)
        x2 = (matriz[pos-1][pos+1] - (matriz[pos-1][pos] * x1))/matriz[pos-1][pos-1]
        results.append(x2)
        x3 = (matriz[pos-2][pos+1] - ((matriz[pos-2][pos-1] * x2) + (matriz[pos-2][pos] * x1)))/matriz[pos-2][pos-2]
        results.append(x3)
        results.reverse()
        return results

    def __generateNewMatriz__(self, matriz):
        matrizNew = [] 
        matrizNew = [temp.copy() for temp in matriz]
        return matrizNew
