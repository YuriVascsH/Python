nome = input("Digite seu nome: ")
Tamanho_nome = len(nome)
if(Tamanho_nome <= 4):
    print('Seu nome é curto.')
elif(5 <= Tamanho_nome <= 6):
    print('Seu nome é normal.')
else:
    print('Seu nome é grande.')