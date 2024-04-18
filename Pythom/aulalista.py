"""
Listas em Python
Mutável
Suporta valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
Métodos Úteis:
        Append, Insert, Pop, Del, Clear, Extend, +
Create Read Update Delete
Criar  ler  alterar Apagar = lista[i] (CRUD)
"""
# lista = [123, True, 'Luiz Otávio, 1.2, []']
# print(lista)



# Armazenando um dado da lista em uma varíavel:
lista = [10, 20, 30, 40]
numero = lista[2]
print(numero)

# Alterando um valor de um dado em uma lista:
lista[2] = 300
print(lista)

#Apagando um Valor de um dado em uma lista:
del lista[2]
print(lista)

"""Quando deletamos um dado na lista fazemos com que o todos os valores que estão no indice posteiror a ele desçam uma casa:
Exemplo:
                [-0---1---2---3---4-]
        lista = [10, 20, 30, 40, 50]
        del lista[2]
                [-0---1---2---3-]
        lista = [10, 20, 40, 50]
Tentar evitar ao máximo de eliminar elementos no meio da lista, pois vai haver mais processamento do Programa.
Exemplo:
        Uma lista de 10.000 valores se eu quiser apagar o índice 2 os outro 9998 itens terão que ser movido para as suas novas posições.    
        Em lista removemos sempre o primeiro ou o último
"""
# Caso a gente queira adicionar um novo elemento ao final da lista, utilizamos o comando "APPEND"
# Exemplo:
# Esse comando é bom, pois é útil para lista. Não há muito processamento 
lista.append(50)
lista.append(60)
print(lista)
# Caso a gente queira remover um elemento ao final da lista, utilizamos o comando "POP"
# Exemplo:
lista.pop()
ultimo_valor = lista.pop()
print(lista, "Removido", ultimo_valor)
# Caso a gente queira remover um elemento que não seja o ultimo elemento da lista, utilizamos o comando "POP"
# Exemplo:
lista.pop()
ultimo_valor = lista.pop(2)
print(lista, "Removido", ultimo_valor)
# Se  a lista for muito grande evitar ao máximo

