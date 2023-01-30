api_key = '1lsASWt3Lad0C3acMl8U3krLE'
api_secret = 'IMwCx2HSjmwBAQGJD6ryn5s75nBJ6RUanCaZSxvE3SpQjV5qpb'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAF4AlgEAAAAASvGZARuUEsufofuvxM9%2BVegRDjw%3DK5b8zMtLB4up0xKFNN7ZAKW3VJFFBx2zZL9HPrSpuhfgXsfh5A'
acess_token = '1064279268660822016-1HllGc7hr6bJVZgdZZF7U4bBOSKX1P'
acess_token_secret = 't1rUPHsluDu6D8KMlWrJHPG40GT7kKjAzNuWate3YEJho'
import tweepy
from web_scrp import nao_tanko
from datetime import datetime
from time import sleep
client = tweepy.Client(bearer_token,api_key,api_secret,acess_token,acess_token_secret)
#response = client.create_tweet(text= nao_tanko())
#print('consegui caraio')
def ler_linhas(numero_id):
    with open('ids.txt','r',encoding='utf-8') as lista_ids:
        if f'{numero_id}\n' in lista_ids.readlines():
            return True
        else:
            return False


while True:
    mentions = client.get_users_mentions(1064279268660822016,since_id=1619851435784667139)
    for mention in mentions.data:
        print(mention.id,'\n')
        with open('ids.txt','w',encoding='utf-8') as ids:
            ids.write(f'{mention.id}\n')
        if 'piada' in mention.text:
            print('lendo ->',ler_linhas(mention.id))
            if ler_linhas(mention.id) == False:
                try:
                    client.create_tweet(in_reply_to_tweet_id=mention.id,text=nao_tanko('pretos-piadas'))
                except Exception as ex:
                    print(ex)
                else:
                    print('consegui, abre o  TT ai')