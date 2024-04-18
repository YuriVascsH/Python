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
limite_SAQUES = 3

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
        if (numeros_saques < 3):
            user = input('')
            if 
    elif opcao == 'e':
        ...
    elif opcao == 'q':
        break
    else:
        print('Por favor, digite uma opção válida.')
        continue

