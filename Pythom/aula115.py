# """
# Closure e funções que retornam outras funções
# """


# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f' {saudacao}, {nome}'
#     return saudar

# """
# Qunado temos saudar() estamos executando a função, quando temos saudar() estamos retornadno"""
# s1 = criar_saudacao('Bom dia')

# for nome in ['Yuri', 'Luis', 'Carlos']:
#     print(s1(nome))


# def dobro(x):
#     return x * 2

# def triplo (y):
#     return y *3

# def quadruplicam(z):
#     return z * 4

# primeiro = dobro(5)
# print(primeiro)

# Outra maneira:
# def criar_multiplicador(multiplicador):
#     def numerado(numerador):
#         return numerador * multiplicador
#     return numerado

# x = criar_multiplicador(5)
# print(x(5))