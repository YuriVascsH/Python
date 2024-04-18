"""


def soma (x, y):
    return x + y

def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica"""

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(lambda x, y: x + y, 2, 3
    )
)