#Operadores Úteis:
"""
União | união(union) - Une
Intersecção & (intersecion) - items presentes em ambos
Diferença - itens presentes apenas no set da esquerda
Diferença Simétrica ^ - Itens que não estão em ambos
"""
#União:
s1 ={1, 2, 3}
s2 ={2, 3, 4} 
s3 = s1 | s2
print(s3)
# {1, 2, 3, 4}
#Observe que ele só retorna os valores repetidos uma única vez

#Intersecção:
s3 = s1 & s2
# {2, 3}

#Diferença, depende de quem estiver na esquerda

s3 = s1 - s2
print(s3)
#{1}

s3 = s2 - s1
print(s3)
#{4}

#Diferença Simétrica - itens que não estão presentes em ambos
s3 = s2 ^ s1
print(s3)
# {1, 4}