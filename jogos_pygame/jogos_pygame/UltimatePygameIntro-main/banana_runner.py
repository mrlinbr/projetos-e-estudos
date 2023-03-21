import pygame as pg
from sys import exit
from random import randint

class Macaco(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        mamaco = pg.image.load('graphics/imagens/mamaco.png').convert_alpha()
        width = mamaco.get_rect().width
        height = mamaco.get_rect().height
        self.image = pg.transform.scale(mamaco,(width//10,height//10))
        self.rect = self.image.get_rect(midbottom=(200,550))

    def movimento(self,vel=10):
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

class Banana(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        banana = pg.image.load('graphics/imagens/banana_descascada.png').convert_alpha()
        width = banana.get_rect().width
        height = banana.get_rect().height
        self.image = pg.transform.scale(banana, (width//10, height//10))
        self.rect = self.image.get_rect(midbottom=(randint(10, 390), randint(10, 590)))

class Game:
    def __init__(self):
        pg.init()
        self.tela = pg.display.set_mode((400, 600))
        self.relogio = pg.time.Clock()
        self.player = Macaco()
        self.bananas = pg.sprite.Group()
        self.score = 0
        self.font = pg.font.SysFont('font/Pixeltype.ttf', 20)

    def draw_score(self):
        text_surface = self.font.render(f'Score: {self.score}', True, 'white')
        self.tela.blit(text_surface, (5, 10))

    def check_for_collision(self):
        for banana in self.bananas:
            if banana.rect.colliderect(self.player.rect):
                self.score += 1
                banana.kill()

    def run(self):
        temp0_execucao_bananas = 2000
        tempo_comida = pg.USEREVENT + 1
        pg.time.set_timer(tempo_comida, temp0_execucao_bananas)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

                if event.type == tempo_comida:
                    temp0_execucao_bananas *= 0.9
                    self.bananas.add(Banana())

            self.check_for_collision()

            self.tela.fill('black')

            self.player.update()
            self.tela.blit(self.player.image, self.player.rect)

            for banana in self.bananas:
                self.tela.blit(banana.image, banana.rect)

            self.draw_score()

            pg.display.update()
            self.relogio.tick(30)

if __name__ == '__main__':
    game = Game()
    game.run()
