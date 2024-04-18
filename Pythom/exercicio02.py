nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))

if nome and idade:
    print(nome)
    print(nome[::-1])

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
       print ('Seu nome não contém espaços')
    print(len(nome))
    print(nome[0])
    print(nome[-1])
else:
    print('Desculpa, vc deixou campos vazios.')