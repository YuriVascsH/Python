"""
Métodos úteis dos dicionários em Python
LEN - Quantas chaves
KEYS - iterável com as chaves
VALUES - iteravel com os Valores
ITEMS - iterável com chaves e valores
SETDEFAULT - adiciona valor se a chave não existe
COPY - Retorna uma cópia rasa(Shallow copy)
GET - Obtém uma Chave
POP - Apaga um item com a chave especificada (DEL)
POPITEM - Apaga o último item adicionado
UPDATE - Atualiza um dicionário com outro
"""

pessoa = {
    'nome': 'Yuri',
    'sobrenome': 'Jesus',
    'idade': 18,
}

#Verifica a quantidade de chaves que um dicionário possui
print(pessoa.__len__())
#OU
print(len(pessoa))
#Obs.: Se tivermos uma chave duplicata em um dicionário, o Python não considera
#e só conta uma.


#Retorna as chaves presentes no dicionário:
print(pessoa.keys()) 
#dict_keys(['nome', 'sobrenome'])
#Podemos converter para lista ou tplas para ficar melhor a visualização.
print(list(pessoa.keys())) 
#['nome', 'sobrenome']


#Retorna os valores presentes no dicionário:
print(list(pessoa.values()))
#['Yuri', 'Jesus']
#Utilizando o for para ver oos valores do dicionário
for valor in pessoa.values():
    print(valor)


#Retorna as chaves e os valores:
print(list(pessoa.items()))
#([('nome', 'Yuri'), ('sobrenome', 'Jesus')])
#Perceba que tem uma tupla interna, logo podemos acessar o seu índice
for chave, valor in pessoa.items():
    print(chave, valor)


#Funciona como um valor padrão. Se não tiver um valor naquela chave, add esse

pessoa.setdefault('idade', 0)
print(pessoa['idade'])

#GET
#Funciona para obter o valor de uma chave:

print(pessoa.get('nome'))

#POP
#È tipo o DEL, mas ainda podemos visualizar o item que foi apagado

idade = pessoa.pop('idade')
print(idade)
print(pessoa)

#POPITEM
#Deleta a última chave de um dicionário

ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)

#UPDATE
#Serve para atualizar um dicionário

pessoa.update(nome='Novo valor', idade=30)
print(pessoa)
