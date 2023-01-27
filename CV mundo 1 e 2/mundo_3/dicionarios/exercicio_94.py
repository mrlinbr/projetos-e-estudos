#um programa que leia nome, sexo, e idade de uma pessoa, adicone esses dados num dicionario e esse dicionario numa lista.
#Em sequida, dê um display na media de idade, quais individuos estão acima da média (lá ele) e quantas pessoas foram cadastradas

"primeiro, vamos pôr os dados num dicionario, e adicionalo numa lista"
lst = list()
soma = 0
while True:
    dicio = {}
    dicio['nome'] = str(input('qual o nome? '))
    sx = str(input('Qual o sexo? '))
    while sx not in 'MmFf':
        print('sexo invalido kkjj')
        sx = str(input('digite um sexo valido')).lower()
    dicio['sexo'] =  sx
    dicio['idade'] = int(input('qual a idade? '))
    soma += dicio['idade']
    lst.append(dicio.copy())
    ask = input('quer continuar? [S/N]').lower()
    while ask not in 'sn':
        ask = input('quer continuar? [S/N]').lower()
    if ask == 'n':
        break

print(lst)
print(f'foram cadastradas {len(lst)} pessoas')
print(f'A media de idade do grupo foi de {soma/len(dicio):.2f}')
print(f'as mulheres foram: ', end='')
for i in lst:
    if i['sexo']== 'f':
        print(i['nome'], end='')
print(f'\n As pessoas com a idade acima da media foram: ', end='')
for p in lst:
    if p['idade']>soma/len(dicio):
        print(p['nome'],'',end='')