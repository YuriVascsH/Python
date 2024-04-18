# while True:
#     palavra_secreta = input('Digite a palavra secreta:')

#     tentativas = 3
#     letra_acertada = ''
#     while tentativas != 0:
        
       
                
#         letra_digitada = input('Digite uma letra: ')
        
#         if len(letra_digitada) > 1:
#             print('Você digitou mais de uma letra.')
#             continue

#         if letra_digitada == ' ':
#             print('Você digitou um espaço.')
#             continue

#         if letra_digitada in palavra_secreta:
#             print(f'Letra {letra_digitada} está contida na palavra secreta')
#             letra_acertada += letra_digitada
#         else:
#             tentativas-=1
#             print('Você digitou um letra que não contém na palavra secreta \n' 
#                 f'Tentativas restantes:{tentativas}')
        
#         palavra_formada = ""
#         for letra_secreta in palavra_secreta:
#             if letra_secreta in letra_acertada:
#                 palavra_formada += letra_secreta
#             else:
#                 palavra_formada += '*'
            
#         # if palavra_secreta :
#         #     print(f'VOCÊ GANHOU PARABÉNS!!'\
#         #         f'A palavra era:{palavra_secreta}'\
#         #         f'Você ainda tinha {tentativas}x') 
#         #     break

#     palavra_maiuscula = palavra_secreta.upper() 
#     print(f'Você perdeu.\nA palavra secreta era {palavra_maiuscula}.')
#     escolha = input("Deseja jogar Novamente:[S/N]:")
#     opcao = "sn"
#     if len(escolha) > 1:
#         print('VocÊ digitou mais de uma opção')

#     if escolha in opcao:
#         if escolha == "s":
#             continue
#         else:
#             print('Encerrando programa.')
#             break
#     else:
#         print('Você digitou uma opção inválida.')



        
