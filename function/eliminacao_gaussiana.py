from models.matriz import Matriz
from helpers.matriz_operations import *

class EliminacaoGaussiana:

    helper = MatrizOperations()

    def calculo(self, matriz):
        det = 0
        if(type(matriz) is Matriz):
            det = matriz.determinante()

            if(self.helper.validateDeterminante(det)):            
                matrizAmpliada = matriz.matrizAmpliada()
                result = self.helper.algoritmoGauss(matrizAmpliada)
                solucao = self.helper.triangularSuperior(result)
                return solucao
        else:
            print("Matriz Inválida")
     
            
