import csv
class Item:
    taxa_pagamento = 0.8
    all = []
    def __init__(self,nome,preco,quant):
        self.nome = nome
        self.preco = preco
        self.quant = quant

        assert preco >=0, f'{preco} não é valido, digite um vaor maior que zero.'
        assert isinstance(nome,str), f'Mano, custa digitar a porra de uma string?'

        Item.all.append(self)

    def valor(self):
        print(f'O valor de {self.nome} é igual a {self.preco * self.quant} ')

    def __repr__(self):
        return f"Item('{self.nome}',{self.preco},{self.quant})"
    
    @classmethod
    def instanciar_do_csv(cls):
        with open('data.csv','r') as d:
            reader =  csv.DictReader(d)
            print(reader)
            items = list(reader)
            
        for item in items:
            print(item)
            Item(
                nome= item.get('name'),
                preco= float(item.get('price')),
                quant= int(item.get('quantity'))
            )

    @isinstance
    def is_integer(self,num):
        if isinstance(num,float):
            return num.is_integer()
        
        elif isinstance(num,int):
            return True
        else:
            return False

Item.instanciar_do_csv()