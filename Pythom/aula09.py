#numero = input('Vou dobrar o número que vc digitou: ')

#numero_float = float(numero)
#print('O dobro de {} é {:.2}'.format(numero,numero_float * 2))

numero_str = input('Digite um número: ')
try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print("Float:", numero_float)
    print('O dobbro do número {} é de {:.2f}'.format(numero_float, numero_float * 2))
except:
    print('Isso não é um número: ')
 
#numero_str = input('Digite um numero: ')

#if numero_str.isdigit():
 #   numero_float = float(numero_str)
  #  print('O dobro de {} é {:.2f}'.format(numero_float,numero_float *2))
#else:
 #   print('Isso não é um número:')