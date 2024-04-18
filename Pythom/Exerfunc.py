#Desafio de criar uma função e retornar o total da multiplicação
# def multiplicacao(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#         print(total)


# variavel = multiplicacao(1, 2, 3, 4, 5)
# print(1*2*3*4*5)

#Desafio de criar uma função e falar se é par ou ímpar

#Segunda maneira de fazer
# def verificacao(x):
#     if x % 2 == 0:
#         return True
#     return False

# print(verificacao(2))

#Primeira maneira de fazer
# def verificacao(x):
#     return x % 2 == 0

# print(verificacao(2))
# print(verificacao(3))
# print(verificacao(5))

"""
Higher Order Functions
Funções de Primeira Classe
"""

# def saudacao(msg):
#     return msg

# def executa(funcao):
#     return funcao()

# saudacao_2 = saudacao

# v = executa(saudacao_2)
# print('Bom dia'

def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular
    
duplicar = multiplicar(2)
triplicar = multiplicar(3)

print(duplicar(2))
print(triplicar(3))
