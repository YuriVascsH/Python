#Manipulando Chaves e Valores em Dicionários
pessoa = {}

pessoa['nome'] = 'Yuri'

print(pessoa)

#Chave Dinámica:
pessoa1 = {}

#Podemos alterear o nome da chave, para qualquer outroa agora, 
#pois o que importa é a variável
chave = 'nomes'
pessoa1[chave] = 'Fernanda'
pessoa1['sobrenome'] = 'Pessoa'

print(pessoa1[chave])
print(pessoa1['sobrenome'])

#DEletando a chave(sobrenome) do dicionário Pessoa1
del pessoa1['sobrenome']

print(pessoa1)
#Caso a gente queira acessar uma chave no dicionário, 
#utilizamos nomedodicionário.get(nome da chave). Por padrão, se a chave não existir retorna none
print(pessoa1.get('sobrenome'))
#É utilizado condição para verificar:
if pessoa1.get('sobrenome') is None:
    print('Não Existe')
else:
    print(pessoa1['sobrenome'])