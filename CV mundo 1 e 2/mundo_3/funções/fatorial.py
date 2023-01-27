def fat (num,show = False):
    """
    num é o numero a ser fatorado.
    show é para caso voce queira ver a magia.
    """
    t = 1
    for i in range(num,0,-1):
        if show:
            print(i, end = ' ')
            if i>1:
                print('x',end=' ')
            else:
                print('=',end=' ')
        t *= i
#n = int(input('numero: '))
#fat(n,show=True)

help(fat)