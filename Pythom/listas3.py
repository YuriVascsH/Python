"""
Cuidados com dados mutáveis
    copiando o valor(imutáveis)
    Aponta para o mesmo valor na memória (mutável)
"""
# Dados Mutáveis
"""
nome = 'Yuri'
noutra_variavel = nome
nome = 'Joao'
print(nome)
print(noutra_variavel)
"""
# Dados Imutáveis

# Aqui não ocorre a copia de dados. Agora eles estão apontado para o mesmo valor na memória
lista_a = ['Luiz', 'Yuri']
lista_b = lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_b)