"""
args - Argumentos não nomeados
* - *args (Empacotamento e Desaempacotamento)
"""

#Lembete de desempacotamento:
# x, y,*resto = 1, 2, 3, 4  
# print(x, y, *resto)

# def soma(*args):
#     total = 0
#     for indece in args:
#        print('Total', total, indece)
#        total += indece
#        print(total)
# soma(1, 2, 3, 4, 5, 6)



def soma(*args):
    total = 0
    for indece in args:
       total += indece
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

#Função sUM