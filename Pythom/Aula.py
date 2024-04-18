"""while i < len(frase):
    letra_mais_repetida =  frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_mais_repetida)

    if quantidade_atual < quantas_vezes_letra_apareceu:
        quantidade_atual = quantas_vezes_letra_apareceu

    print(quantidade_atual)
    #print(letra_mais_repetida , quantas_vezes_letra_apareceu)
    
   i += 1"""

























frase ='O Python é uma linguagem de programção ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

letra_armazenda = ""
quantidade_atual = 0
i = 0

while i < len(frase):
    
    letra_atual = frase[i]
    
    if letra_atual == " ":
         i += 1
         continue

    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if quantidade_atual < quantas_vezes_letra_apareceu:
        quantidade_atual = quantas_vezes_letra_apareceu
        letra_armazenda = letra_atual
        
    i += 1

print(f'A letra que apareceu mais vezes foi {letra_armazenda} e ela apareceu {quantidade_atual}x.')