#Dictionary Comprehension e Set comprehension

produto = {
    'nome': 'Cantea Azul',
    'preco': 2.5,
    'Categoria': 'Escritório',
}


dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
}

print(dc)

s1 = {i for i in range(10)}
print(s1)