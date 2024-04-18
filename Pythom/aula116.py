"""
Dicionário em Python(tipo Dict)
anda em par "Chave" e "Valor".
Chaves podem ser considerados como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualuer tipo, incluido outro dicionário
Usamos chaves {} ou classe dict para criar dicionários
    Imutáveis: str, int, float, bool, tuple
    Mutável: dict, list
"""

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura':1.8,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero':321},
    ]
}
#Para acessar algo no dicionário devemos escrever o nome do dicionário e depois [nome da chave] 

print(pessoa['nome'])
print(pessoa['sobrenome'])



print()
for chave in pessoa:
    print(pessoa[chave])