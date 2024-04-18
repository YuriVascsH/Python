primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

n1 = int(primeiro_valor)
n2 = int(segundo_valor)

if n1 > n2:
    print("primeiro_valor='{}' é maior do que o segundo_valor='{}'".format(primeiro_valor, segundo_valor))

elif n1 < n2:
    print("segundo_valor='{}' é maior que o primeiro_valor='{}'".format(segundo_valor, primeiro_valor))

else:
    print('Os valores são iguais.')