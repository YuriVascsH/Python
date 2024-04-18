#Exercícios - Sistemas de Perguntas e Respostas
i = 0
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4'
    },

    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55', '35', '85'],
        'Resposta': '25'
    },  
    
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['1','4', '8', '5'],
        'Resposta':'5'

    },
]
for indice in perguntas:
    print(indice.get('Pergunta'))

    for opcao in perguntas['Opcoes']:
        print(opcao)
        # print(indice.get('Opções'))
    
    digito = input('Digite a alternativa correta:')
    
    if digito in indice.get('Resposta'):
        print('Você acertou.')
        i += 1
    else:
        print('Você errou.')

print(f'Você acertou {i} de 3 perguntas') 