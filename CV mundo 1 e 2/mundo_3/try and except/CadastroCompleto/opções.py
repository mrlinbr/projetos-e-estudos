from decoraçoes import linha_simples,sequencia_igual
def ver_lista():
    sequencia_igual('PESSOAS CADASTRADAS')
    with open('cadastroCV.txt','r',encoding='utf-8') as folha_de_anotacoes:
        for l in folha_de_anotacoes.readlines():
            ponto_virgula = 0
            for c in l:
                if c == ';':
                    ponto_virgula = l.index(c)
            l = l.replace('\n','')
            print(f'{l[:ponto_virgula]:<15} {l[ponto_virgula+1:]:>3} anos')
    print()
def adicionar_pessoa():
    from os import replace,remove,listdir
    nome = input('Qual o nome da pessoa? ')
    idade = input('Qual a idade da pessoa? ')
    with open('cadastroCV.txt', 'a',encoding='utf-8') as folha_de_anotacoes:
        folha_de_anotacoes.write(f'{nome};{idade}\n')
    linha_simples()
    print('cadastramento completo')
    linha_simples()