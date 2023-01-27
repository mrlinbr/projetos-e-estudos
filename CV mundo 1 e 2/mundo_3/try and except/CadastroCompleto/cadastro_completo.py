#Umsistema de cadastramento (nome e idade) que salve os dados em uma documento txt
'''
um menu com 3 opções, 1ver lista, 2cadastrar, 3sair
'''
from decoraçoes import linha_pontilhada,linha_simples,sequencia_igual, menu
from opções import ver_lista,adicionar_pessoa
from time import sleep
while True:
    funcoes = menu('ver lista','cadastrar pessoa', 'sair')
    if funcoes == 1:
        ver_lista()
    elif funcoes == 2:
        adicionar_pessoa()
    elif funcoes == 3:
        print(f'Obrigado por participar!')
        break
    sleep(2)
print('programa finalizado')