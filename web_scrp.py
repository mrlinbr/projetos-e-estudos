from bs4 import BeautifulSoup
import requests
from random import randint
def nao_tanko(topico='anao-piadas'):
    piadas_texto = requests.get(f'https://www.piadas.net/{topico}.html').text
    soup_piadas_texto = BeautifulSoup(piadas_texto, 'lxml')
    piada = soup_piadas_texto.find_all('div', class_ ='listjoke')
    p_list = list()
    for e in piada:
        p_list.append(e.text)
    return p_list[randint(0,len(p_list))]


def topico_alatorio():
    lista_topicos = ['anao-piadas','animais-piadas','preto-piadas']
    return lista_topicos[randint(0,len(lista_topicos))]