#Dicionário

# Conjnto não ordenado de pares de chave:valor
#Delimitados por chaves:{Valor imutável} calor{deve ser valor imutavel ou mutavel}

#Declarando um dicionário:

pessoa = {"nome": "Guilherme", "idade":28}
#OU   
pessoa = dict(nome="Guilherme", idade=28)


pessoa["telefone"] = "3333-1234" #{"nome": "Guilherme","idade":28,"telefone":3333-1234}

#Acessando os dados:

pessoa["nome"]#Guilherme

#Reescrevendo um valor de uma chave 
pessoa["nome"] = "Maria" 

#Dicionários aninhados

contatos = {
    "guilherme@gmail.com:":{"nome":"Guilherme", "telefone":"3333-2221"},
    "giovanna@gmail.com:":{"nome":"Giovanna", "telefone":"3443-2121"},
    "Chappie@gmail.com:":{"nome":"Chappie", "telefone":"3344-9871"},
    "melaine@gmail.com:":{"nome":"Melaine", "telefone":"3333-7766"},
}

contatos["giovanna@gmail.com"]["telefone"]#3443-2121

#interndo uma chave:

for chave, valor in contatos.items():
    print(chave,valor)

#Métodos do dicionário:
    
contatos = {
    "guilherme@gmail.com:":{"nome":"Guilherme", "telefone":"3333-2221"},
    "giovanna@gmail.com:":{"nome":"Giovanna", "telefone":"3443-2121"},
    "Chappie@gmail.com:":{"nome":"Chappie", "telefone":"3344-9871"},
    "melaine@gmail.com:":{"nome":"Melaine", "telefone":"3333-7766"},
}
contatos.clear()
contatos #{}

# copy tira uma copia do dicionário

#Cria chaves para vc:

dict.fromkeys(["nome","telefone"])#{"nome":None, "telefone":None}
dict.fromkeys(["nome","telefone"],"vazio")#{"nome":Vazio, "telefone":Vazio}

# Acessar valores no dicionário. É bom para procurar valores e se não achar, ele vai retornar um none:

contatos = {
    "guilherme@gmail.com:":{"nome":"Guilherme", "telefone":"3333-2221"},
    }
contatos["chave"]#Keyerror
contatos.get("chave")#None
contatos.get("chave")#{}

# items(): Retorna as chaves
# Keys(): Retorna a chave daquele dicionario

# Remove uma chave do dicionario:

contatos = {
    "guilherme@gmail.com:":{"nome":"Guilherme", "telefone":"3333-2221"},
    }

contatos.pop("guilherme@gmail.com") #{'nome':"Guilherme", "telefone": "3333-2221"}
# Caso não ache a chave no dicionario
contatos.pop("guilherme@gmail.com",{})#{}

# popitem(): Remove os itens em sequência

#Setdefault() - Serve para add um valor padrão

contato = {'nome':'Guilherme', 'telefone':'3333-2221'}
# Ele respeita o que já tem no dicionário
contato.setdefault("idade",28) #{'nome':'Guilherme', 'telefone':'3333-2221', "idade": 28}

# Retorna apenas os valores do dicionario:

contato.values()

#Verificar se o valor tem no dicionário utilizamos o in

#Remover chave ou valor

del contatos["Chappie@gmail.com"]#Apaga a chave junto com os valores
del contatos #Apaga tudo