"Um sistema para um cabaré, onde o cliente pode procurar por alguem que está dentro do que seu poder de compra lhe permite ter"
#uma tela de informações como numero de moças, clientes já cadastrados.
"""
Extrair informações da lista onde os dicionarios estão.
Vou importar uma variavel que a cada novo cliente vai receber mais um elemento."""

#Cada nova moça vai receber um dicionario com informações como nome, preferência sexual, altura, experiencia e preço.
"""
Um dicionario simples que será adicionado a uma lista.
"""
#Match
"""
Na tela inicial, o sistema perguntará quanto o cliente tem para investir,e então, mostrar todas as moçãs que estão abaixo do valor indicado pelo usuario.
"""
from os import listdir,replace
trabalhadoras = []
while True:
    print('[1 Para ver nossa lista]\n[2 para se cadastrar]\n[3 para sair]\n')
    ask = int(input('Bem vindo(a)! Qual ação deseja realizar?'))
    print('=+'*30)
    
    if ask == 1:
        print(f'Olá novo usuario, bem vinde! estas pessoas aqui estão prontas para te satisfazer.\n')
        lista_de_nomes = []
        for a in listdir('./ms_bordel'):
            lista_de_nomes.append(a[:-4])
            if a[-4:]=='.txt':
                print(a[0:-4])
        print('se interessou por alguem? digite o nome da pessoa no campo abaixo para ver detalhes sobre ela:\n')
        print(lista_de_nomes)
        n = str(input())
        for item in listdir('./ms_bordel'):
            if item[:-4] == n:
                with open(f'ms_bordel\{item}','r',encoding='utf-8') as pessoa_de_interesse:
                    lista_c_atributos = pessoa_de_interesse.readlines()
                    print(f"""
                    nome: {lista_c_atributos[0]}
                    sexualidade: {lista_c_atributos[1]}
                    experiancia: {lista_c_atributos[2]}
                    valor: {lista_c_atributos[3]}
                    whattsapp: {lista_c_atributos[4]}""")
    if ask == 2:
        dicio_mocas = dict()
        print(f'cadastre-se para trabalhar conosco! insira seus dados e espere entrarmos em contato.')
        dicio_mocas['nome'] = str(input('   Qual seu nome? '))
        dicio_mocas['pref_sex'] = str(input(f'   {dicio_mocas["nome"]}, qual sua sexialidade? (cis,bi,lesbica...) '))
        dicio_mocas['exp'] = int(input('    De 0 a 10, qual a sua experiência nesta aréa? '))
        dicio_mocas['valor'] = float(input('    Quanto você quer cobrar pelo serviço? '))
        dicio_mocas['numero'] = str(input(f'    {dicio_mocas["nome"]}, precisamos do seu numero para entrar em contato, por favor, informe ele: '))
        id = dicio_mocas['nome']
        with open(f"{dicio_mocas['nome']}.txt",'a',encoding='utf-8') as id:
            for i in dicio_mocas.values():
                print(i)
                id.write(f'{str(i)}\n')
                
        replace(f'{dicio_mocas["nome"]}.txt',f'ms_bordel\{dicio_mocas["nome"]}.txt')
        trabalhadoras.append(dicio_mocas.copy())
        dicio_mocas.clear()
    if ask == 3:
        break
print(f'Obrigado por participar')
