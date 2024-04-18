"""
Lista de listas e seus indices
"""
salas = [
    #   0        1
    ['Maria', 'Helena', ], #0
    #0
    ['Elaine', ],  #1
    # 0         1        2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], #2

]
# Como consultar um lista dentro de outra lista:
#[O primeiro é o indice da lista geral][O segundo é o indice da lista de dentro]
print(salas[2][3][2])
# Para acessar sempre vai entrando um por um é tipo cascata

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)

