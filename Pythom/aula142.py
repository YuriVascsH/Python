#Comando dir, Hasattr, Gettar

string = 'Yuri'
metodo = 'upper'
print(string)

if hasattr(string, 'upper'):
    print('Existe Upper')
    print(getattr(string , metodo)())
else:
    print('Não possui upper')