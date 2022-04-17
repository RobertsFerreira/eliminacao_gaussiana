from models.matriz import Matriz
from function.eliminacao_gaussiana import *

def pause():
    input('\nPressione qualquer tecla para continuar...')
    exit()

def main():
    try:
        linhas = int(input('Digite o numero de linhas: '))
        colunas = int(input('Digite o numero de colunas: '))

        matriz = Matriz(linhas, colunas)

        matriz.toString(matriz.matrizCoeficient)

        eliminacao = EliminacaoGaussiana()

        solucao = eliminacao.calculo(matriz)

        Matriz.printList(solucao)

        pause()
    except KeyboardInterrupt:
        pause()
    except Exception as e:
        print(e)
        pause()

if __name__ == '__main__':
    main()