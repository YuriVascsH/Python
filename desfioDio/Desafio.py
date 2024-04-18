#Funções:
# Menu
menu = """

[d] Depositar
[S] Sacar
[E] Extrato
[Q] Sair
""" 
Saldo = 0
limite = 500
Extrato = ""
numeros_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)
    if opcao == 'd':
        valor_usuario = float(input("Digite o valor a ser depositádo: "))

        if valor_usuario > 0:
            print(f"O valor de {valor_usuario} foi depositado em sua conta.")
            Saldo += valor_usuario
            Extrato += f'Depósito de {valor_usuario:.2f}'
        elif (valor_usuario <= 0 ):
            print('Valor inferior ou igual a zero.')
        else:
            print("Você não inseriu os dados corretamente.")

    elif opcao == 's':
        if Saldo <= 0:
            print('Não é possível realizar um saque porque o saldo da sua conta é zero.')
        elif numeros_saques >= limite_saques:
            user = input('Digite um quantia para sacar: ')
            saqueUser = float(user)

            if saqueUser > 500.00:
                print('Digite um valor inferior ao limite.')
            elif saqueUser <= 0:
                print('Você digitou um valor inferior ou igual a zero.')
            elif saqueUser > Saldo: 
                print('Você não possui essa quantia em sua conta')
            else:
                numeros_saques += 1
                print(f'saque de R${saqueUser:.2f}')
                Saldo -= saqueUser
                Extrato += f'Saque de: R${saqueUser}' 
        else:
            print('Você atingiu a quantidade máxima de realizações de saques diários. Tente novamente amanhã.')

    elif opcao == 'e':
        print('\n########## EXTRATO ##########')
        print('Não foram realizadas operações' if not Extrato else Extrato)
        print(f'Saldo de: R${Saldo:.2f}')
        print('###############################')
    elif opcao == 'q':
        print('Você finalizou sua sessão')
        break
    else:
        print('Por favor, digite uma opção válida.')
        continue


