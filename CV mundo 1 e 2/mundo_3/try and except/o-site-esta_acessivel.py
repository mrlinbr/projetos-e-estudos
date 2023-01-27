import requests
from time import sleep
def is_up(link):
    ta_on = requests.head(link)
    try:
        print(f'O site "{link[7:]}" está acessivel.')
        return ta_on.status_code == 200
        
    except:
        print(f'"{link}" não está acessivel.')

while True:
    sleep(0)
    try:
        is_up('http://pudim.com.br')
    except(KeyboardInterrupt):
        break
    