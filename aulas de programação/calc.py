import functions as fun
while True:
    op = int(input(f"""Qual operação voe deseja realizar??\n[1 = adição, 2 = subtração, 3 = divisão, 4 = multiplicação]"""))
    num1 = int(input('\n\nAgora digite o primeiro elemnto de sua multiplicação: '))
    num2 = int(input('E o segundo tambem: '))
    if op == 1: print(fun.add(num1,num2))
    elif op == 2: print(fun.sub(num1,num2))
    elif op == 3: print(fun.div(num1,num2))
    elif op == 4: print(fun.multi(num1,num2))
    else: print(f'{op} não é uma opção valida! tente novamente.')