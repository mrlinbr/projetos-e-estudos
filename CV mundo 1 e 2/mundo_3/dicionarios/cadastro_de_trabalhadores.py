while True:
    trabalhador = {}
    trabalhador['nome'] = str(input('nome: '))
    trabalhador['idade'] = 2022 -int(input('ano de nascimento: '))
    trabalhador['carteira_trabalho'] = int(input('numero da carteira de trabalho: '))
    trabalhador['aposentadoria'] = trabalhador['idade']+35
    if trabalhador['carteira_trabalho']==0:
        for i in range(0,len(trabalhador.items())):
            for i in trabalhador.items():
                print(f'O {i[0]} é {i[1]}')
        break
    trabalhador['aposentadoria'] = str(input('ano de contratação: '))
    trabalhador['salario'] = str(input('salario: '))
    print(trabalhador)
    for i in trabalhador.items():
        print(f'O {i[0]} é {i[1]}')