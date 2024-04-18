"""
Imprecisão de pontos flutuantes 
Double-precision floating-point format IEE 754
"""

import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
# Primeira forma:
# Retorna string
print(f'{numero_3:.2f}')
# Segunda Forma:
# Retorna número flutuante
print(round(numero_3))
# Terceira Forma
# Importar biblioteca
# Vai retornar precisamnete 
numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2
print(numero_3)
# Podemos transformar ela em uma string e vai ficar certo
#Vai retornando arredondado
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)


