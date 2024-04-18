"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local.
E escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local poden ser alcançados
O escopo vai pulando de dentro para fora tem acesso
Exemplo:
"""

x = 1

def escopo():
    x = 10
    def outra_funcao():
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)
escopo()
print(x)

# Exemplo da utilização do global
# x = 1

# def escopo():
#     global x
#     x = 10
#     def outra_funcao():
#         global x
#         x = 11
#         y = 2
#         print(x, y)

#     outra_funcao()
#     print(x)
# escopo()
# print(x)