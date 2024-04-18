hora = input('Digite o horário: ')

hora_int = int(hora)

if (8 <= hora_int <= 11):
    print('Bom dia')
elif (12 <= hora_int <= 17):
    print('Boa tarde')
elif (18 <= hora_int <= 23):
    print('Boa noite')
else:
    print('Boa madrugada')