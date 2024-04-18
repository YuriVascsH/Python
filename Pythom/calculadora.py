#numero = input("Digite um número: ")
#try:
 #   int_numero = int(numero)
#except:
 #   print("Você não digitou um número")

#contador = 1
#while contador <= 10:
 #   print(f"{int_numero} X {contador} = {int_numero * contador}")
  #  contador += 1

#USANDO IF AND ELSE

#numero = input('Digite o primeiro número: ')
#numero2 = input('Digite o segundo número: ')
#try:
 #  float_numero = float(numero)
 #   float_numero2 = float(numero2)
#except:
 #  print('Você não digitou um número.')

#operacao = input('Digite o tipo de operação que você deseja:')

#if operacao == 'adição':
 #   print(f'{float_numero} + {float_numero2} = {float_numero + float_numero2}')
#elif operacao == "Subtração":
 #    print(f'{float_numero} - {float_numero2} = {float_numero - float_numero2}')
#elif operacao == "Multiplicação":
 #    print(f'{float_numero} * {float_numero2} = {float_numero * float_numero2}')
#else:
#     print(f'{float_numero} / {float_numero2} = {float_numero / float_numero2}')
# while pergunta != "S":

# numero = input('Digite o primeiro número: ')
# numero2 = input('Digite o segundo número: ')
# try:
#     float_numero = float(numero)
#     float_numero2 = float(numero2)
# except:
#    print('Você não digitou um número.')

# operacao = input('Digite o tipo de operação que você deseja:')

# if operacao == 'adição':
#     print(f'{float_numero} + {float_numero2} = {float_numero + float_numero2}')
# elif operacao == "Subtração":
#      print(f'{float_numero} - {float_numero2} = {float_numero - float_numero2}')
# elif operacao == "Multiplicação":
#      print(f'{float_numero} * {float_numero2} = {float_numero * float_numero2}')
# else:
#      print(f'{float_numero} / {float_numero2} = {float_numero / float_numero2}')

# pergunta = input('Deseja sair da calculadora:[S/N]:')

# while True:
#     print('------------------CALCULADORA---------------------')
#     numero = input('Digite o primeiro valor: ')
#     numero2 = input('Digite o segundo valor: ')
    
#     try:
#         float_numero = float(numero)
#         float_numero2 = float(numero2)
#     except ValueError:
#         print('Erro: Os valores inseridos não são válido.')

#     operacao = input('Digite o operador desejado: ')
#     if operacao == '+':
#      print(f'{float_numero} + {float_numero2} = {float_numero + float_numero2: .2f}')
#     elif operacao == "-":
#       print(f'{float_numero} - {float_numero2} = {float_numero - float_numero2: .2f}')
#     elif operacao == "*":
#       print(f'{float_numero} * {float_numero2} = {float_numero * float_numero2: .2f}')
#     elif operacao == "/":
#       print(f'{float_numero} / {float_numero2} = {float_numero / float_numero2: .2f}')

#     condicao = input('Deseja sair?[S/N]:')
#     if condicao.upper() == "S":
#             print('Você saiu do programa.')
#             break    

# while True:
#     print('------------------CALCULADORA---------------------')
#     numero = input('Digite o primeiro valor: ')
#     numero2 = input('Digite o segundo valor: ')
    
#     try:
#         float_numero = float(numero)
#         float_numero2 = float(numero2)
#     except ValueError:
#         print('Erro: Os valores inseridos não são válido.')

#     operacao = input('Digite o operador desejado: ')
#     if operacao == '+':
#      print(f'{float_numero} + {float_numero2} = {float_numero + float_numero2: .2f}')
#     elif operacao == "-":
#       print(f'{float_numero} - {float_numero2} = {float_numero - float_numero2: .2f}')
#     elif operacao == "*":
#       print(f'{float_numero} * {float_numero2} = {float_numero * float_numero2: .2f}')
#     elif operacao == "/":
#       print(f'{float_numero} / {float_numero2} = {float_numero / float_numero2: .2f}')

#     condicao = input('Deseja sair?[S/N]:')
    
#     while condicao != "S" or "N":
#         condicao = input('Deseja sair?[S/N]:')
#     if condicao.upper() == "S":
#             print('Você saiu do programa.')
#             break
#     else: condicao.upper() == "N"

#-----Calculadrora Finalizada-----#
while True:
    print('----------CALCULADORA----------')

    numero = input('Digite o primeiro valor: ')
    numero2 = input('Digite o segundo valor: ')
    
    #converter de string para Float
    try:
        float_numero = float(numero)
        float_numero2 = float(numero2)
    except ValueError:
        print('Erro: Os valores inseridos não são válido.')
        continue

    operadores_permitidos = '+-/*'    
    operacao = input('Digite o operador desejado(+-/*): ')
    
    #Verificação dos operadores
    if operacao not in operadores_permitidos:
       print("Você digitou um operador inválido.") 
       continue
    
    if len(operacao) > 1:
       print("Você digitou mais de um operador.")
       continue 

    #Operações
    if operacao == '+':
        print(f'{float_numero} + {float_numero2} = {float_numero + float_numero2: .2f}')
    elif operacao == "-":
        print(f'{float_numero} - {float_numero2} = {float_numero - float_numero2: .2f}')
    elif operacao == "*":
        print(f'{float_numero} * {float_numero2} = {float_numero * float_numero2: .2f}')
    elif operacao == "/":
        print(f'{float_numero} / {float_numero2} = {float_numero / float_numero2: .2f}')
    condicao = input('Deseja sair?[S/N]:').upper()

    #Encerrar programa 
    while condicao not in ["S", "N"]:
        print('Você Digtou uma opção diferente de S ou N')
        condicao = input('Deseja sair?[S/N]:').upper()

    if condicao == "S":
            print('Você saiu do programa.')
            break

           

