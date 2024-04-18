"""
split e join com list e str
split - Divide uma string
Join - Une uma string
"""

#Vai pegar a frase da variável e vai dividir como elementos em uma lista.
frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split()
print(lista_palavras)
#A função Split separa a stirng por meio do que a gente escolher. No exemplo acima foi separado por espaços split()
# Resultado: ['Olha', 'só', 'que,', 'coisa', 'interessante']

#Agora podemos separa pela vírgula, deixando uma lista de frases.

frase = 'Olha só que, coisa interessante'
lista_frases = frase.split(',')
print(lista_frases)
#Resultado: ['Olha só que', ' coisa interessante']

# Utilizando o for para fazer sepração:
# A função Strip faz com que elimine os espaços.

frase = 'Olha só que, coisa interessante'
lista_frase = frase.split(',')

for i, frase in enumerate(lista_frase):
        print(lista_frase[i].strip())

#Questão de formatação é interessante, pois não é interessante fazer o que foi feito acima. A melhor maneira é fazer assim:
#Melhor maneira
frase = '    Olha só que    ,coisa interessante      '
lista_frase_cruas = frase.split(',')

lista_frase = []
for i, frase in enumerate(lista_frase_cruas):
        lista_frase.append(lista_frase_cruas[i].strip())

print(lista_frase)
print(lista_frase_cruas)

#Funçao Join: Serve para unir strings, tuplas, listas.

frases_unidas = '-'.join('abc')
print(frases_unidas) 
#Neste exemplo temos a sting abc que será separada pelo (-) a-b-c

frases_unidas1 = '-'.join(lista_frase)
print(frases_unidas1)

#obs: Só funciona com interáveis lista,strings e tuplas