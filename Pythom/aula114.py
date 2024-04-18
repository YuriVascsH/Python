"""
Higher Order Functions
Funções de Primeira Classe
"""

def saudacao(msg):
    return msg

def executa(funcao,msg):
    return funcao(msg)

v = executa(saudacao, 'Bom dia')
print(v)

# print(saudacao('Bom dia'))