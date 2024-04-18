num = input('Digite um númro inteiro: ')

try:
    num_int = int(num)
    if (num_int % 2 == 0):
        print('O valor informado é par')
    else:
        print('O valor informado é impar')
except:
    print('Você não informou um número.')