import pygame as pg
from sys import exit
from random import randint
class Macaco(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (200,550))

    def movimento(self,vel = 10):
        event = pg.key.get_pressed()
        if event[pg.K_UP]:
            self.rect.y -= vel
        elif event[pg.K_DOWN]:
            self.rect.y += vel
        elif event[pg.K_LEFT]:
            self.rect.x -= vel
        elif event[pg.K_RIGHT]:
            self.rect.x += vel
    

    def update(self):
        self.movimento()

class Bananas(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        banana = pg.image.load('graphics/imagens/banana_descascada.png').convert_alpha()
        width = banana.get_rect().width
        height = banana.get_rect().height
        self.image = pg.transform.scale(banana,(width/10,height/10))
        self.rect = self.image.get_rect(midbottom = (randint(10,390),randint(10,590)))

    def check_for_collision(self):
        global score
        if pg.sprite.spritecollide(self,player,False):
            self.kill()


    def update(self):
        self.check_for_collision()
        

pg.init()

font = pg.font.Font('font/Pixeltype.ttf',50)

tela = pg.display.set_mode((400,600))
relogio = pg.time.Clock()
player = pg.sprite.GroupSingle()
player.add(Macaco())

comida = pg.sprite.Group()

temp0_execução_bananas = 2000
tempo_comida = pg.USEREVENT + 1
pg.time.set_timer(tempo_comida,temp0_execução_bananas)

score = 0
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == tempo_comida:
            temp0_execução_bananas *= 0.9
            comida.add(Bananas())
        
        if event.type == pg.KEYDOWN:
            pass
    

    for banana in comida:
        if banana.rect.colliderect(player.sprite.rect):
            score += 1
            print(score)
    
    tela.fill('Black')
    pontuacao = font.render(f'{score}',False,'Yellow')
    pontuacao_rect = pontuacao.get_rect(center = (10,20))
    tela.blit(pontuacao,pontuacao_rect)

    player.draw(tela)
    player.update()

    comida.draw(tela)
    comida.update()

    
    pg.display.update()
    relogio.tick(30)

    #/home/murilo/Área de Trabalho/codigos/jogos_pygame/UltimatePygameIntro-main/banana_runner.py