# List comprehesion em Python
# List Comprehesion é uma forma rápida para criar listas
# a partir de iteráveis

lista = []
for numero in range(10):
    lista.append(numero)

# Mesma coisa, mas estamos utilizando List Comprehesion

lista = [numero for numero in range(10)]
print(lista)

# Também podemos colocar lógica no programa
lista = [numero * 2  for numero in range(10)]
print(lista)

# Mapeamento pegar um dado de uma lista e colocar em outra lista, tendo ao final o mesmo tamanho 

produtos = [
    {'nome':'p1','preco':20,},
    {'nome':'p2','preco':10,},
    {'nome':'p3','preco':30,},
]
# Utilizando condicional para mapeamento
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
print(*novos_produtos, sep= '\n') 