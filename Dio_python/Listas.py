"""
LISTAS
"""

# Criando Listas- Armazena qualquer objeto/item(int,string,float)

frutas = ['laranja', 'maca', 'uva']
frutas = []

letas = list("python") #Cada letra é um item na lista

numeros = list(range(10))

carro = ["Ferrari", "F8", 420000, 2020, 2900, "SP", True]

#Como acessar?

print(frutas[0]) #laranja
print(frutas[2]) #Uva

#TAmbém podemos utilizar o indice negativo

print(frutas[-1])
print(frutas[-2])

#listas aninhaddas- permiti colocoar outras listas dentro de uma lista
#Criando estruturas bidimensionais tendo índice e coluna

matriz = [
    [1,"a",2],
    ["b",3,4],
    [6,5,"c"]
]

# matriz[linha][coluna]

matriz[0] # [1,,"a",2]
matriz[0][0] #1
matriz[0][-1] #2
matriz[-10][-1] #"c"

#Fatiamento
# lista[londe inicia: onde vai terminar: como vai pular 2 em 2, 3 em 3]
lista = ["p","y","t","h","o","n"]


lista[2:] #["y","t","h","o","n"]
lista[:2] #["p","y"]
lista[1:3] #["y","t"]
lista[::] #["p","y","t","h","o","n"]
lista[0:3:2] #["p","t"]
lista[::-1] #lista invertida

#Percorrendo uma lista

carro = ["gol","celta","palio"]

for indice, carro in enumerate(carro):
    print(f"{indice}: {carro}")

#add um item na lista

lista = []

lista.append(1)
lista.append("Puthon")
lista.append([40,30,50])

print(lista) #[1, "Python", [40,30,50]]

#Limpando minha lista

lista.clear()

#Copia uma lista para outra lista. Podendo a gente alterar a lista nova e não alterar a antiga

l2 = lista.copy()

#Serve para verificar quantas vezes aquele item aparece naquela lista

cores = ["Vermelho","Azul","Verde","Azul"]

cores.count("Vermelho") #1
cores.count("Azul") #2

#Serve para verificar o indice daquele item

cores = ["Vermelho","Azul","Verde","Azul"]

cores.index("Verde") #2

#Serve para retirar o último elemento da lista

cores.pop()#Azul
cores.pop()#Verda

#Serve para escolher um elemento e remover ele da lista

cores.remove("Verde") #["Vermelho","Azul","Azul"]

#Serve para inverter a lista

cores.reverse()

# Ordenar uma lista
#Temos varios tipos

cores.sort()#Oredenação alfabética

cores.sort(reverse=True) # Ordenação invertida

cores.sort(ket=lambda x: len(x)) #Ordena pelo tamanho da palavra


#Verificar o tamanho da lista 

len(cores)#Tamanho da lista



