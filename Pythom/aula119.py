"""
Continuação da última aula
Copy and Shallow Copy
"""

d1 = {
    'c1': 1,
    'c2': 2,
}
d2 = d1

d2['c1'] = 100
print(d1)
#Perceba que d1 sofre alteração em d1, Logo não é uma cópia
#{'c1': 100, 'c2': 2}

d1 = {
    'c1': 1,
    'c2': 2,
}
d2 = d1.copy()

d2['c1'] = 100
print(d1)
print(d2)
#Perceba que agora temos uma cópia
#{'c1': 1, 'c2': 2}
#{'c1': 100, 'c2': 2}

#Definição de cópia rasa:
#Quando temos uma lista ou ... ele não vai realizar uma cópia, 
#mas sim ele vai apontar para o endereço de memória em que está armazenado

d3 = {
    'c3': 2,
    'c4': 3,
    'lis':[0, 1, 3],
}

d4 = d3.copy()
#Perceba que na lista alteramos também o valor nas duas
d4['lis'][1] = 33333

print(d3)
print(d4)

#Nesse caso utilizamos o "Import copy" e depois utilizamos o "copy.deepcopy" 
#realizando uma cópia profunda.

import copy

d3 = {
    'c3': 2,
    'c4': 3,
    'lis':[0, 1, 3],
}

d4 = copy.deepcopy(d3)

d4['lis'][1] = 33333

print(d3)
print(d4)

#Perceba que agora temos uma cópia profunda:

# {'c3': 2, 'c4': 3, 'lis': [0, 1, 3]}
# {'c3': 2, 'c4': 3, 'lis': [0, 33333, 3]}
