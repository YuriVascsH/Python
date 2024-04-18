"""
Listas em Python
Métodos Úteis:  
        append = Adiciona um item ao final
        insert = Adiciona um item no índice escolhido
        pop = Remove do final ou do índice escolhido
        del = Apaga um índice
        extend = Estende a lista
        + - concatena listas
        (CRUD) Creat Read Update Delete
"""

# Adicionando e Removendo um item na lista e mostrando posteriormente
# lista = [10, 20, 30, 40]
# lista.append('Luiz')
# nome = lista.pop()
# lista.append(1234)
# del lista[-1]
# lista.clear()
# print(lista)


"""O insert permiti a gente adicionar um item em uma determinada posição na lista:
    Ele funciona assim:(Informa o indice em qual posição ele vai entrar, o valor que será armazenado)
    Exemplo:
"""
# lista = [10, 20, 30, 40]
# lista.insert(0 ,5)
# print(lista)

lista_a = [1, 2, 3]
lista_b = [3, 4, 5, 6]
lista_c = lista_a + lista_b
# O metodo extend, ele faz uma ação e não retorna nada
lista_d = lista_a.extend(lista_b)
print(lista_c)
print(lista_d)