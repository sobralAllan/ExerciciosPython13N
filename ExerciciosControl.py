import this
import ExerciciosModel
this.opcao = -1

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
            print('Escreva aqui a solução para o exercício 02')
        else:
            print('Opção informada não é válida!')
