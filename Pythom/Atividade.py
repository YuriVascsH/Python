nome = 'Yuri Vasconcelos'
tamanho_nome = len(nome)
nome_modificado = ""

contador = 0
while contador < tamanho_nome:
    nome_modificado += nome[contador]

    if contador < tamanho_nome -1:
        nome_modificado += "*"
    contador += 1

print(nome_modificado)