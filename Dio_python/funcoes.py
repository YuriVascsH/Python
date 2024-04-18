#Função
#É um bloco de código identificado cpor um nome e pode receber uma lista de parâmetros, tendo ou não valores
##Torna o código mais legível e reaproveita o código
#Programar em maneira estruturada

#Criando função:

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem2(nome):#Valor sem padrão
    print(f"Seja bem vindo {nome}")

def exibir_mensagem_3(nome="Anônimo"):#Valor padrão
    print(f"Seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem2("Yuri")
exibir_mensagem_3()#Valor padrão
exibir_mensagem_3("Katharine")

#Retornando Valores:
#Utilizamos a palavra return.
#Toda função retorna None por padrão. Ele tbm retorna mais de um valor

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_total([10,20,34]))
print(retorna_antecessor_e_sucessor(10))
print(exibir_mensagem)

#Argumentos nomeados:
# São argumentos nomeados, se um argumento estiver nomeado os posteriores devem ser nomeados
