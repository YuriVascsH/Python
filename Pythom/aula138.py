lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))

#Mesma coisa
lista = [
    (x,y)#Mapeamento
    for x in range(3)
    for y in range(3)
]

print(lista)