# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set ()
# Imutáveis () "" 0 0.0 None Flase range(0, 10)

#Se a gente fizer um if com esses valores teremos um true or false
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'Teste',falsy("TESTE"))
print(f'')
print(f'')
print(f'')
print(f'')
print(f'')
print(f'')
print(f'')