#Empacotamento e Desempacotamento de Dicionários

# args e kwargs
#
# kwargs - keyword arguments (argumentos nomeados)

a, b = 1, 2
a,b = b, a

# pessoa = {
#     'nome': 'Aline',
#     'Sobrenome': 'Souza',
# }
# (a1, a2), (b1, b2) = pessoa.items()
#Desempacotamento


pessoa = {
    'nome': 'Aline',
    'Sobrenome': 'Souza',
}

dados_pessoal = {
    'idade': 16,
    'altura': 1.6,
}
pessoa_completa = {**pessoa, **dados_pessoal}

print(pessoa, dados_pessoal)
#Mesma coisa
print(pessoa_completa)



def mostrar_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)
    
mostrar_argumentos_nomeados(1, 2, nome ='Joana', qlq = 123)

configuracoes = {
    'arg1': 1,
    'arg2': 2, 
    'arg3': 3,
    'arg4': 4,
}
mostrar_argumentos_nomeados(**configuracoes)
