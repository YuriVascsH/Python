"""
Retorno de valores das funções (return)
"""
#Somente a função tem a função de retornar. Ele para tudo o que estiver após o return
# def soma(x, y):
#     return (x + y)

# variavel = soma(1, 2)
# variavel = int('1')
# print(variavel)

#def soma(x, y):
#   return (x + y)
    
# soma1 = soma(2, 2)
# soma2 = soma(3, 3)
# print(soma1 + soma2)

#Também podemos fazer utilizando condição:

def soma(x, y):
    if x > 10:
        return 10
    return x + y
soma1 = soma(1, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)