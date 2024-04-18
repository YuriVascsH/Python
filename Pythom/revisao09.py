nome = input('Digite seu nome: ')
idade = input('Informe sua idade: ')

if(len(nome) != 0) and (len(idade) != 0):
    print(f'Seu nome é {nome}')
    print(nome[::-1])
    print(f'({" " in nome})')
    print(f'Seu nome tem {len(nome)}')
    print(f'A primeira letra do seu nome é {nome[0:1]}')
    print(f'A última letra do seu nome é {nome[-1:]}')
else:
    print('Desculpe, você deixou campos vazios')