cpf_lista = []
caracteres_proibidos = ('.', '/', ';',)
cpf_resultado = []
contador = 10

while True:
    print('==========Validar CPF==========')

    #Verifica se tem menos ou mais caracteres
    Cpf_digitado= input('Digite o cpf sem caracteres especiais: ')
    if len(Cpf_digitado) > 9:
        print('Você digitou caracteres a mais.')
        continue
    if len(Cpf_digitado) < 9:
        print('Você digitou caractere a menos')
        continue
    #caractere especial dgiitado
    if Cpf_digitado in caracteres_proibidos:
        print("Você digitou algum caractere especial.")
        continue
    #colocando o cpf na lista
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
    print(cpf_resultado)
    #Somando tudo
    soma = sum(cpf_resultado)
    print(soma)
    multiplica = soma * 10
    print(multiplica)
    resto = multiplica % 11
    print(resto)
    if resto > 9:
        print('O seu primeiro número do cpf é 0')
    else:
        print(f'O seu primeiro dígito do seu cpf é {resto}')

