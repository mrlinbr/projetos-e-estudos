import csv
from os.path import isfile
from datetime import date

class Gerenciamento:
    def __init__(self):
        pass

    def menu(self):
        while True:
            opcao = int(input("""\n\nCompahia aerea - menu de gerenciamento.
    para prosseguir, selecione um das seguintes opções:
    1 - Adicionar passageiro a um voo
    2 - Listar voos do dia
    3 - cadastrar um novo voo
    4 - checar voos cadastrados
    5 - sair
    """))
            if opcao == 1:
                self.adicionar_passageiro()

            if opcao == 2:
                self.voos_do_dia()

            if opcao == 3:
                self.cadastro_voo()

            if opcao == 4:
                self.mostrar_voos()

            if opcao == 5:
                break

        print('programa finalizado.')

    def adicionar_passageiro(self):
        # Esta função irá adicionar na lista de assentos usados o numero do assento escolhido pelo passageiro.
        voo = int(input('digite o codigo do voo: '))
        assento = int(input('Em qual assento o passageiro deseja sentar sentar?: '))
    
        with open('voos.csv','r+') as voos:
            rows = csv.DictReader(voos)
            lista_voos = list(rows)

            for line in lista_voos:
                print(line)
                if voo == int(line['codigo']):
                    if len(list(line['assentos-usados'])) > 100: 
                        print(f'infelizmente o voo {voo} atingiu sua capacidade maxima de passageiros.')
                    else:
                        nova_lista = line['assentos-usados']
                        nova_lista.append(assento)
                        line['assentos-usados'] = nova_lista

            voos.seek(0)
            writer = csv.DictWriter(voos,fieldnames=rows.fieldnames)
            writer.writeheader()
            writer.writerows(lista_voos)

#essa desgraça não funciona
    def voos_do_dia(self):
        data = self.data_hoje()
        with open('voos.csv','r+') as voos:
            info_voos = csv.DictReader(voos)
            print(f'Para o dia de hoje ({data}), os seguintes voos estão agendados: ')
            for voo in info_voos:
                if voo['data'] == data:
                    print(voo)
            print('\n')

    def cadastro_voo(self):
        # aqui, deve-se realizar o cadastro de um novo voo ao sistema de forma que este não ocupe
        # um espaço já utilizado na tebela
        codigo = int(input('Por favor, digite o codigo do voo: '))
        data = input("insira a data do voo no formato 'dd/mm/aa': ")
        partida = input('De onde o voo partirá?: ')
        destino = input('Qual será o destino do voo?: ')

        self.infos = [codigo,data,partida,destino,list()]
        fieldnames=['codigo','data','partida','destino','assentos-usados']

        is_file = isfile('voos.csv')

        with open('voos.csv','a+') as voos:
            info_voos = csv.DictWriter(voos,fieldnames=fieldnames,delimiter='\t')

            if not is_file or voos.tell() == 0:
                info_voos.writeheader()

            info_voos.writerow(dict(zip(info_voos.fieldnames, self.infos)))

        print(f'Voo {codigo} cadastrado.')

    def mostrar_voos(self):
        op = int(input('Voce deseja ver TODOS os voos[1] ou checar informações de um especifico?[2]: '))

        if op == 1:
            with open('voos.csv','r+') as voos:
                info_voos = csv.DictReader(voos)

                for line in info_voos:
                    print(line)
        
        if op == 2:
            codigo = int(input('Qual o codigo do voo que voce deseja ver?: '))
            with open('voos.csv','r+') as voos:
                info_voos = csv.DictReader(voos)

                for line in info_voos:
                    if line['codigo'] == str(codigo):
                        print(line)

                        while True:
                            assento = input('Deseja checar a disponibilidade de um assento? [N para cancelar]: ')
                            if assento in 'Nn':
                                break
                            else:
                                if int(line['assentos-usados']) < int(assento) and int(assento) < 100:
                                    print(f'O assento {assento} está vago.')

    def data_hoje(self):
        #consertar isso aqui, a formatação tá errada.
        today = str(date.today())
        hoje = ''
        for l in today:
            if l == '-':
                l = '/'
            hoje += l
        return hoje

adm = Gerenciamento()
adm.menu()