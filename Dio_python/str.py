#String- Possui muitos métodos
curso = "pYthon"
#Maiúsculo,minúsculo e título

print(curso.upper())#PYTHON
print(curso.lower())#python
print(curso.title())#Python

#Eliminação de espaços em brancos de uma variavel

curso_espaco = "    Python"

print(curso_espaco.strip())#"Python" REmove todos os espaços
print(curso_espaco.lstrip())#"Python " Remove todo o espaço a esquerda
print(curso_espaco.rstrip())#"  Python" Remove todo o espaço a direita

#Junções e centralização

curso_conta = "Python"

print(curso.center(10,'#'))#"##Python##"
print(".".join(curso_conta))#P.y.t.h.o.n

#FATIAMENTO DE STRINGS

nome = "Yuri Jesus Vasconcelos"

# nome[Inicio:Fim:quanto ele vai pular/step]

nome[0] #"Y"
nome[:3] #Yuri
nome[6:] #Jesus Vasconcelos
nome[5:10] #Jesus
nome[::-1]# solecnocsaV suseJ iruY
nome[:]# Yuri Jesus Vasconcelos
nome[10:10:2]