def votar(nasci):
    import datetime
    agora = datetime.datetime.now().year
    idade = agora - nasci

    if idade<16:
        print(f'Seu voto foi negado, espera mais {16-idade} anos')
    
    if idade >= 16 and idade <= 18:
        print(f'Com {idade} seu voto é opcional ainda')

    if idade >= 18 and idade <= 65:
        print(f'seu voto é obrigatorio, vamos lá eleger o mito. {idade} anos nas costas já.')
    
    if idade >= 65:
        print(f'{idade} anos, tá veio, seu voto é opcional')

    
anos = int(input('digite o ano de seu nascimento: '))
votar(anos)