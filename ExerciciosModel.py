
def exercicio01():
    A = 10
    B = 20
    msg = "Antes da Troca: A = {}, B = {}".format(A,B)
    aux = A
    A   = B
    B   = aux
    msg = msg + "\nDepois da Troca: A = {}, B = {}".format(A,B)
    return msg

def exercicio02(num1):
    return 'O antecessor é {}'.format(num1-1)

def exercicio03(bas, altura):
    return bas * altura