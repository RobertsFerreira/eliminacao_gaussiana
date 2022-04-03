from models.matriz import Matriz
from function.eliminacao_gaussiana import *

def main():
    linhas = int(input('Digite o numero de linhas: '))
    colunas = int(input('Digite o numero de colunas: '))

    matriz = Matriz(linhas, colunas)

    matriz.toString(matriz.matrizCoeficient)

    eliminacao = EliminacaoGaussiana()

    solucao = eliminacao.calculo(matriz)

    Matriz.printList(solucao)


if __name__ == '__main__':
    main()