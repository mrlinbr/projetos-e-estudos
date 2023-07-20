from datetime import date
import csv

def data_hoje():
    today = str(date.today())
    hoje = ''
    for l in today:
        if l == '-':
            l = '/'
        hoje += l
    return hoje

with open('voos.csv') as file:
    voos = csv.DictReader(file)
    for line in voos:
        print(line['assentos-usados'])
        print(type(line['assentos-usados']))
        bancos = [i for i in line['assentos-usados'] ]
        print(bancos)
        print(type(bancos))

#lista = ['m','u','r','i','l','o']
