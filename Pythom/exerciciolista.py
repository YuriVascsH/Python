lista_compras = []
opcoes_disponiveis = ('a' 'l' 'i' 'e')

while True:

    print('==========Lista de Compras==========')
     
    opcao = input('Selecione uma opção\n [i]nserir [a]pagar [l]istar [e]ncerrar:')
    
    #Verificação de opção
    if len(opcao) > 1:
         
         print("Você digitou mais de uma opção")
         continue
    
    if opcao not in opcoes_disponiveis:
        print('Você digitou uma opção inválida.')
        continue

    #  Opção de Inserir
    if opcao == 'i':
        add_item = input('Digite o item que deseja adicionar:')
        lista_compras.append(add_item)
        print("Item adicionado com sucesso.")
        continue

    #  Opção de Apagar
    if opcao == 'a':  
        if len(lista_compras) == 0:
            print('Sua lista não contem itens para ser apagados.')
            continue
        else:
             for indice in range(len(lista_compras)):
                print(indice,lista_compras[indice])    
        indice_lista = input('Digite o dado a ser apagdo da sua lista:')
        try:
            int_indice_lista = int(indice_lista)
        except:            
            print('Erro na converssão.')
            continue
        if int_indice_lista > indice :
            print('Não foi possível apagar este índice')
        else:
            lista_compras.pop(int_indice_lista)
            print('Item removido da lista com sucesso.')
            

    # Opção de listar
    if opcao == 'l':
       if len(lista_compras) == 0:
           print('Não há itens em sua lista para serem exibidos.')
       else:
            for indice in range(len(lista_compras)):
                print(indice,lista_compras[indice])

    # Opção de Encerrar
    if opcao == 'e':
        print('Você encerrou o seu programa.')
        break

        
            
     