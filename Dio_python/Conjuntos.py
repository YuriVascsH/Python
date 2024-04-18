#Conjuntos

# É uma coleção com elementos únicos não possui objeot repetidos

set([1,2,3,3,4])# {1,2,3,4}

#o set espera um interável, logo as string também sofrem. Não garante ordem 

set("abacaxi") #{"b", "a", "c", "x", "i"}

#Acessando dados em um set- Como não tem ordem não é possível acessar pelo index

numeros = {1,2,3,4}

numeros = list(numeros)

print(numeros[0])#1

#Percorrendo um set

carros = {"gol", "celta", "Palio"}

for carro in carros:
    print(carro)

#Métodos da classe set

#União de dois conjuntos:
conjunto_a = {1,2}
conjunto_b = {3,4}

conjunto_a.union(conjunto_b) #{1,2,3,4}

#Intersecção de dois conjuntos:

conjunto_a = {1,2,3}
conjunto_b = {4,5,6}

conjunto_a.intersection(conjunto_b) #{2,3}

#Diferença entre os dois conjuntos

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.difference(conjunto_b)#{1}
conjunto_b.difference(conjunto_a)#{4}

#Pegar todos os elementos que não estão na intersecção

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.symmetric_difference(conjunto_b) #{1,4}

#Veriificar se tds os elementos esão no subconjunto

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

conjunto_a.issubset(conjunto_b)#True Todos os elementos de a estão em b
conjunto_b.issubset(conjunto_a)#False

#Verifica se ele é o conjunto dominante
conjunto_a = {1,2,3} 
conjunto_b = {4,1,2,5,6,3}

conjunto_a.issubset(conjunto_b)#False
conjunto_b.issubset(conjunto_a)#True

# Verifica se os elementos se tocam/esa presente 

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

conjunto_a.isdisjoint(conjunto_b) #True Não se tocam
conjunto_a.isdisjoint(conjunto_c) #False Se tocam

#Adcionar itens no set

sorteio = {1,23}

sorteio.add(25)#{1,23,25}
sorteio.add(42)#{1,23,25,42}
sorteio.add(25)#{1,23,25,42} Não repete 

# clear e copy msm coisa da lista

# descartar elementos

numeros = {1,2,3,4,5,6,6,7,8,9,0,1}

numeros #{1,2,3,4,5,6,7,8,9,0}
numeros.discard(1)
numeros.discard(45) #Não dá erro
numeros #{2,3,4,5,6,7,8,9,0}

# remove o valor da frente
numeros = {1,2,3,4,5,6,6,7,8,9,0,1}
print(numeros.pop())#1

# remove o valor = o discard, mas ele dá erro quando não tem o elemento

# Verificar se o elemento tem no conjunto

numeros = {1,2,3,4,5,6,6,7,8,9,0,1}

1 in numeros #True
10 in numeros #False