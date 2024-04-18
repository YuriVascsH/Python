nome = input("Qual é o seu nome? ")
print(f"Olá, {nome} seja bem-vindo!")


#Maneira mais correta

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro Valor: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f"A soma dos números é: {int_numero_1 + int_numero_2}")

#Maneira correta, mas não é muito sugerida

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro Valor: '))

print(f"A soma dos números é: {int_numero_1 + int_numero_2}")