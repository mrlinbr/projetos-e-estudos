#um programa que receba varias notas, adicone-as num dicionario, informa qual foi a maior, menor e a situação da turma.
#M.soares
def get_media(lista):
    """função para conseguir a media dos elementos de uma lista qualquer, basta passar a lista como argumento"""
    n = 0
    for i in lista:
        n += i
    return n/len(lista)
def situacao(media):
    """Essa função diz a situação do aluno dada a media dele, passe a media como argumento"""
    if media < 3:
        return('Pessima')
    elif media >=3 and media <=6:
        return('Ruim')
    elif media > 6 and media <=8:
        return('Ok')
    else:
        return('Excelente!')

def boletim(*notas, sit = False):
    """Função para conseguir um dicionario com as informações de uma turma, passa quantas notas forem nescessarias e sinalize ' sit = True' para ver a situação"""
    dic = {}
    dic['total'] = len(notas)
    dic['maior'] = max(notas)
    dic['menor'] = min(notas)
    dic['media'] = get_media(notas)
    if sit == True:
        dic['situação'] = situacao(dic['media'])
    print(dic)
boletim(4,5,6,7,6, sit = True)