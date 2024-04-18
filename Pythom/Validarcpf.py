cpf_lista = []
caracteres_proibidos = ('.', '/', ';',)
cpf_resultado = []
contador = 10

while True:
    print('==========Validar CPF==========')

    #Verifica se tem menos ou mais caracteres
    Cpf_digitado= input('Digite o cpf sem caracteres especiais: ')
    if Cpf_digitado == "":
        print("Você nã digitou nada!")
        continue
    #Caractere mais
    elif len(Cpf_digitado) > 9:
        print('Você digitou caracteres a mais.')
        continue
    #Caractere menos
    elif len(Cpf_digitado) < 9:
        print('Você digitou caractere a menos')
        continue
    elif not Cpf_digitado.isdigit:
        print("Digite apenas números")
        continue
    #caractere especial dgiitado
    elif Cpf_digitado in caracteres_proibidos:
        print("Você digitou algum caractere especial.")
        continue
    #colocando os dígitos do cpf na lista
    for i in Cpf_digitado:
        cpf_lista.append(i)
    print(cpf_lista)
    #Transformando indice em numero e multiplicando
    for indice in cpf_lista:
        try:
            indice_int = int(indice)
        except:
            print('Erro na conversão')    
        armazenado = indice_int * contador
        contador -=1
        cpf_resultado.append(armazenado)
    #Somando tudo
    soma = sum(cpf_resultado)
    multiplica = soma * 10
    resto = multiplica % 11    
    #Condição
    if resto > 9:
        print('O seu primeiro número do cpf é 0')
        
    else:
        print(f'O seu primeiro dígito do seu cpf é {resto}')

    #Continuar ou encerrar programa
    opcao = (input('Você Deseja verificar um novo cpf[S/N]?'))

    if opcao == "S":
        cpf_lista.clear()
        cpf_resultado.clear()
        
        continue
    else:
        print('Você Encerrou seu programa')
        break





# cpf_lista = []
# caracteres_proibidos = ('.', '/', ';',)
# i = 10
# while True:
#     print('==========Validar CPF==========')

#     #VErifica se tem menos ou mais caracteres
#     Cpf_digitado= input('Digite o cpf sem caracteres especiais: ')
#     if len(Cpf_digitado) > 9:
#         print('Você digitou caracteres a mais.')
#         continue
#     if len(Cpf_digitado) < 9:
#         print('Você digitou caractere a menos')
#         continue
#     #caractere especial dgiitado
#     if Cpf_digitado in caracteres_proibidos:
#         print("Você digitou algum caractere especial.")
#         continue
#     #colocando o cpf na lista
#     cpf_lista.append(Cpf_digitado)
#     print(cpf_lista)
#     for indice in cpf_lista:
#         for numero in indice:
#             int_numero = int(numero)
#             while i != 2:    
#                 result = int_numero * i
#                 i -= 1
#                 print(result)








#     # for indice in cpf_lista:
#     #   print(indice)
#     # for numeros in indice:  
#     #     numeros_armazenados = numeros
#     #     print(numeros_armazenados)
#     #     try:
#     #         int_numeros_armazenados = int(numeros_armazenados)
#     #     except:
#     #         print('erro')
#     # while i < 11:
#     #     resultado = int_numeros_armazenados * i
#     #     print(resultado)    
#     #     i += 1
                

#     # try:
#     #     int_numero = int(numeros)
#     # except:
#             # print('erro')
#     # # print(int_numero * (11 - 1))
