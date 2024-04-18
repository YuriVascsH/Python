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
        valor_user = input("Digite o valor a ser depositádo: ")

        valor_usuario = float(valor_user) 
        if valor_usuario > 0:
            print(f"O valor de {valor_usuario} foi depositado em sua conta.")
            Saldo += valor_usuario
           
        elif (valor_usuario <= 0 ):
            print('Valor inferior ou igual a zero.')
        else:
            print("Você não inseriu os dados corretamente.")

    elif opcao == 's':
        if numeros_saques != 3:
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
               print(f'Você realizou um saque na quantia de {saqueUser}')
               Saldo -= saqueUser
        else:
            print('Você atingiu a quantidade máxima de realizações de saques diários. Tente novamente amanhã.')
    elif opcao == 'e':
        ...
    elif opcao == 'q':
        break
    else:
        print('Por favor, digite uma opção válida.')
        continue


