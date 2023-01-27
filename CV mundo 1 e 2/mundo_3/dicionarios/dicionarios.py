pessoas = list()
individuo = dict()
for i in range(0,2):
    individuo['nome']=str(input('Nome: '))
    individuo['altura'] = float(input('altura: '))
    individuo['peso']=float(input('Peso: '))
    pessoas.append(individuo.copy())
    print(individuo)
print(individuo)
print(pessoas)

while True:
    ask = input('quem voce quer consultar? ("ninguem" para): ')
    if ask == 'ninguem':
        break
    for i in range(0,len(pessoas)):
        n = pessoas[i]['nome']
        if n == ask:
            print(pessoas[i])