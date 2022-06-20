import this
import ExerciciosModel
this.opcao = -1
this.bas = -1
this.altura = -1

def Menu():
    print('Menu\n\n'          +
          '\n1. Exercício 01' +
          '\n2. Exercício 02' +
          '\n3. Exercício 03' +
          '\n0. Sair'         +
          '\nEscolha uma das opções acima: ')
    this.opcao = int(input())

def Executar():
    while(this.opcao != 0):
        Menu()
        if this.opcao == 0:
            print('Obrigado!')
        elif this.opcao == 1:
            print(ExerciciosModel.exercicio01())
        elif this.opcao == 2:
            print('Informe um número')
            num1 = int(input())
            print(ExerciciosModel.exercicio02(num1))
        elif this.opcao == 3:
            while this.bas <= 0:
                print('Informe a base do retângulo: ')
                this.bas = float(input())
                if this.bas <= 0:
                    print('Informe uma base com valor positivo')

            while this.altura <= 0:
                print('Informe a altura do retângulo: ')
                this.altura = float(input())
                if this.altura <= 0:
                    print('Informe uma base com valor positivo')

            print(ExerciciosModel.exercicio03(this.bas,this.altura))
        else:
            print('Opção informada não é válida!')
