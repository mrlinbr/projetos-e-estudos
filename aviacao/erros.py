import csv
from os.path import isfile
from datetime import date
import json


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
        # Esta função irá adicionar na lista de assentos usados o número do assento escolhido pelo passageiro.
        voo = int(input('digite o código do voo: '))
        assento = int(input('Em qual assento o passageiro deseja sentar?: '))
        try:
            with open('voos.csv', 'r+') as voos:
                rows = csv.DictReader(voos)
                lista_voos = list(rows)

                for line in lista_voos:
                    if voo == int(line['codigo']):
                        if len(line['assentos-usados']) > 100:
                            print(f'Infelizmente o voo {voo} atingiu sua capacidade máxima de passageiros.')
                        else:
                            if line['assentos-usados']:
                                nova_lista = json.loads(line['assentos-usados'])
                            else:
                                nova_lista = []
                            if assento in nova_lista:print('Assento ocupado!')
                            else: nova_lista.append(assento)
                            line['assentos-usados'] = json.dumps(nova_lista)

                voos.seek(0)
                writer = csv.DictWriter(voos, fieldnames=rows.fieldnames)
                writer.writeheader()
                writer.writerows(lista_voos)
        except FileNotFoundError:
            print('\nBanco de dados não criado. Por favor, selecione a opção 3 e cadastre um voo em seguida..')

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
        while isnumeric(codigo)
        data = input("insira a data do voo no formato 'aaaa/mm/dd': ")
        partida = input('De onde o voo partirá?: ')
        destino = input('Qual será o destino do voo?: ')

        self.infos = [codigo,data,partida,destino,[]]
        fieldnames=['codigo','data','partida','destino','assentos-usados']

        is_file = isfile('voos.csv')

        with open('voos.csv','a+') as voos:
            info_voos = csv.DictWriter(voos,fieldnames=fieldnames)

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
                        varios_assentos = json.loads(line['assentos-usados'])
                        print(line)
                        print(f"Existem {100-len(varios_assentos)} vagos.")


                        while True:
                            assento = input('Digite o numero do assento que voce deseja checar a disponibilidade [N para cancelar]: ')
                            if assento in 'Nn':
                                break
                            else:
                                if assento in varios_assentos: print(f"o assento {assento} está ocupado.")

class Funcoes:
    def __init__(self):
        pass
    def check_data(data):
        data_list = data.split('/')
        

        list_num = []
        num_corretos = [4,2,2]
        for e,i in zip(data_list,num_corretos):
            list_num.append([len(e),i])
        print(list_num)

        for k in list_num:
            if k[0] != k[1]:
                print("Voce digitou a data no Formato erradO. por favor, obedeca o Formato 'AAAA/MM/DD'.")
            break

adm = Gerenciamento()
adm.menu()
