import pygame
from sys import exit


class Mascaco(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('graphics\imagens\mamaco.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (250,400))
    
    def movimento(self):
        pressionar_tecla = pygame.key.get_pressed()
        if pressionar_tecla[pygame.K_w,pygame.K_UP]:
            self.rect.y -= 5

        elif pressionar_tecla[pygame.K_s,pygame.K_DOWN]:
            self.rect.y += 5
        
        elif pressionar_tecla[pygame.K_d,pygame.K_RIGHT]:
            self.rect.x += 5

        elif pressionar_tecla[pygame.K_a,pygame.K_LEFT]:
            self.rect.x -= 5

    def update(self):
        self.movimento()

class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((600,700))
        self.relogio = pygame.time.Clock()
        self.player = Mascaco()

    def rodar(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            

            self.tela.fill('black')

           
            self.tela.blit(self.player.image,self.player.rect)

            pygame.display.update()
            self.relogio.tick(30)

if __name__ == '__main__':
    jogo = Game()
    jogo.rodar()