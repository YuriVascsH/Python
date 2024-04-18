# Exercício - sistema de perguntas e respostas

i = 0
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# print('Jogo teste')

# for pergunta in perguntas:
#     print(pergunta.get('Pergunta'))
   
#     for enumerados, opcao in enumerate(per.get('Opções')):
# #         print(f'{enumerados}){numeros}')
 
# #     user = input('Digite uma opção:')

# # if 

print('Jogo Teste')

for pergunta in perguntas:
    print(pergunta['Pergunta'])

    for enumerados, opcao in enumerate(opcoes):
        print(f'{enumerados}) {opcao}')
    user = input('Escolha uma opção:')
    use_int = int(user)
    if opcao[use_int] == pergunta['Resposta']:
        print('Acertou')