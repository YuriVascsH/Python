"""
Self faz referência ao paramêtro do objeto
Self = This
Podemos tbm utilizar o this
"""

#Criando uma classe
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, ):
        #Atributos
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor 
        
        #Métodos são funções dentro de uma classe
    def buzinar(self):
        print('Plim plim....')

    def parar(self):
        print('Parando bicilceta...')
        print('Bicicleta parada!')

    def correr(self):
        print('Vrummmmmm...')

    #Método com get e return:Prátiica ñ muito utilizada em python
    def get_cor(self):
        return self.cor

    #Primeira maneira é no manual:
    # def __str__(self):    
    #     return f"Bicicleta: {self.cor}, Modelo:{self.modelo}, Ano:{self.ano}, Valor:{self.valor}"
    
    # #Segunda maneira é mais automatizado:
    # Esse é melhor:
    def __str__(self): 
        return f"{self.__class__.__name__}:{', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    
#Instância da classe
caloi =Bicicleta('vermelha', 'caloi', 2022, 600)

#Executando os métodos:
caloi.buzinar()
caloi.parar()
caloi.correr()

#Acessar Atributos:
print(caloi.cor, caloi.cor)

print(caloi)

print(caloi.get_cor())


"""
Método construtor: É  executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado do nss objeto
__init__ também pode ser método inicializador
"""

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

"""
Método Destrutor: É executado quando uma instância(objeto) é destruida. Não é tão utilizado em Python.
__del__ 
"""
class Cachorro:
    def __del__(self):
        print("Destruindo a instância")

c = Cachorro()
del c