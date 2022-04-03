#class matriz com os metodo print e adicionar valores
class Matriz:
    
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.matrizTermos = []
        self.matrizCoeficient = []
        self.addValues()

    def addValues(self):
        matrizAux = []
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                value  = int(input('Digite o valor do coeficiente para a posição [{}][{}]: '.format(linha,coluna)))
                matrizAux.append(value)
            self.matrizCoeficient.append(matrizAux)
            matrizAux = []

        for linha in range(self.linhas):
            value = int(input('Digite o valor do termo independente valor para a posição [{}][{}]: '.format(linha, (self.colunas))))
            self.matrizTermos.append(value)
    
    def determinante(self):
        if(self.linhas == 3):

            primeiraColuna = self.matrizCoeficient[0][0] * self.matrizCoeficient[1][1] * self.matrizCoeficient[2][2]
            segundaColuna = self.matrizCoeficient[0][1] * self.matrizCoeficient[1][2] * self.matrizCoeficient[2][0]
            terceiraColuna = self.matrizCoeficient[0][2] * self.matrizCoeficient[1][0] * self.matrizCoeficient[2][1]

            primeiraSoma = primeiraColuna + segundaColuna + terceiraColuna

            quartaColuna = self.matrizCoeficient[0][2] * self.matrizCoeficient[1][1] * self.matrizCoeficient[2][0]
            quintaColuna = self.matrizCoeficient[0][0] * self.matrizCoeficient[1][2] * self.matrizCoeficient[2][1]
            sextaColuna = self.matrizCoeficient[0][1] * self.matrizCoeficient[1][0] * self.matrizCoeficient[2][2]

            segundaSoma = quartaColuna + quintaColuna + sextaColuna

            det = primeiraSoma - segundaSoma

            return det
        else:
            print('Não é possivel calcular o determinante de uma matriz não quadrada')

    def matrizAmpliada(self):
        matrizGeral = []
        for linha in range(self.matrizCoeficient.__len__()):
            matrizGeral.append(self.matrizCoeficient[linha])
        for linha in range(matrizGeral.__len__()):
            matrizGeral[linha].append(self.matrizTermos[linha])
        return matrizGeral
   
    def toString(self, matriz):
        print()

        print('-'*60)

        print('\nMatriz:')

        for linha in range(matriz.__len__()):
            for coluna in range(matriz[linha].__len__()):
                print(f"{self.__formatValue__(matriz[linha][coluna])}", end=" ")
            print()
        print()
  
    @staticmethod
    def __formatValue__(value):
        if(value < 0):
            return f'({value})'
        else:
            return str(value).replace('.0', '')

    @staticmethod
    def printList(matriz):
        print()

        print('-'*60)

        print('\nsolução:')

        for linha in range(matriz.__len__()):
            print(f"{Matriz.__formatValue__(matriz[linha])}", end=" ")
        print()