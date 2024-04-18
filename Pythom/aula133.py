# Função Lambda em Python
# A função Lambda é uma função como qualquer outra em Python.
# Porém, são funções anônimas que contém apenas uma linha. ou seja, tudo deve ser
# contido dentro de uma única expressão.

# lista = [4, 2, 32, 6, 8, 9, 7, 1, 66]
# #lista.sort ele ordena a lista
# lista.sort 
# print(lista)

# Entretanto quando temos um dicionário, não conseguimos ordenar utilizando o sort
#Criamos uma função para realizar a ordenação.

# lista_n = [
#     {'nome': 'Luiz', 'Sobrenome': 'Miranda'},
#     {'nome': 'Yuri', 'Sobrenome': 'Jesus'},
#     {'nome': 'Maria', 'Sobrenome': 'Clara'},
#     {'nome': 'Carlos', 'Sobrenome': 'Miguel'},
#     {'nome': 'Aline', 'Sobrenome': 'Souza'},
# ]

# def ordenar(item):
#     return item['nome']

# lista_n .sort(key=ordenar)

# for item in lista_n:
#     print(item)


#Agora entra a questão da função Lambda.
#Perceba que é a mesma coisa da de cima, mas agora tem menos código.

lista_n = [
    {'nome': 'Luiz', 'Sobrenome': 'Miranda'},
    {'nome': 'Yuri', 'Sobrenome': 'Jesus'},
    {'nome': 'Maria', 'Sobrenome': 'Clara'},
    {'nome': 'Carlos', 'Sobrenome': 'Miguel'},
    {'nome': 'Aline', 'Sobrenome': 'Souza'},
]
# lista_n .sort(key=lambda item: item['nome'])
#Outra maneira de fazer:
l1 = sorted(lista_n, key=lambda item: item['nome'])
l1 = sorted(lista_n, key=lambda item: item['nome'])
#Aqui criamos uma nova lista 
for item in lista_n:
    print(item)

