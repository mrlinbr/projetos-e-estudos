import pygame, csv
from random import choice,randint,random
from sys import exit

# Configurações do jogo
canvas_width = 480
canvas_height = 640
collector_size = 50
shape_speed = 1

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Inicialização do Pygame
pygame.init()

# Configuração da janela do jogo
canvas = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("Teste do Jogo dos Presidentes")

clock = pygame.time.Clock()

# Classe do coletor
class Collector(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((collector_size, collector_size))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = canvas_width/2 - collector_size/2
        self.rect.y = canvas_height - collector_size - 10

    def update(self):
        self.rect.x = pygame.mouse.get_pos()[0] - collector_size // 2

# Classe das formas
class Shape(pygame.sprite.Sprite):
    def __init__(self, shape_type, x, y):
        super().__init__()
        self.type = shape_type
        self.size = randint(20, 50)
        self.image = pygame.Surface((self.size, self.size))
        self.castelo = pygame.image.load('catch_despotas/images/castelo.png').convert_alpha()
        self.geisel = pygame.image.load('catch_despotas/images/geisel.png').convert_alpha()
        if self.type == "circle":
            self.image.blit(self.castelo,(0,0))
        elif self.type == "square":
            self.image.blit(self.geisel,(0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += shape_speed


class Quadro(pygame.sprite.Sprite):
    def __init__(self,width,height,pos,text):
        super().__init__()
        self.text = text
        self.width = width
        self.altura = pos[1]
        self.height = height
        self.pos = pos

        self.quadro = pygame.surface.Surface((width,height))
        self.quadro_rect = self.quadro.get_rect()
        self.quadro_rect.topleft = pos
        
        self.quadro.blit(canvas,(pos[0],-30))
        self.quadro_rect.y = -100

    def draw(self,text):
        self.quadro.blit(canvas,(self.pos[0],-30))
        pygame.draw.rect(canvas,'#475F77',self.quadro_rect)
        #self.animation()

        #TODO animação para o retangulo
        self.txt = font.render(self.text,True,'#32a852')
        
        self.blit_text(text,(self.quadro.get_width()*0.1,self.quadro.get_height()*0.2))
    
    def blit_text(self, text, pos, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = self.quadro.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    #TODO aumentar o quadro por y
                    y += word_height  # Start on new row.
                canvas.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
            if (self.quadro_rect.bottom <= y):
                self.quadro_rect.height += word_height
            
    def animation(self):
        if self.quadro_rect.y < self.altura:
            self.quadro_rect.y += 2

# Grupo de sprites
all_sprites = pygame.sprite.Group()
shapes_group = pygame.sprite.Group()

# Criação do coletor
collector = Collector()
all_sprites.add(collector)

#criação do quadro
quadro = Quadro(canvas.get_width()*0.9, 300, (30,50), "testando isso aqui")


# Função para criar novas formas
def create_shape():
    shape_type = choice(["circle", "square"])
    x = randint(0, canvas_width - 50)
    y = -50
    shape = Shape(shape_type, x, y)
    all_sprites.add(shape)
    shapes_group.add(shape)

# Função para exibir curiosidade

def get_curiosity(nome,pontos):
    global max_pts
    with open('catch_despotas/curiosidades.csv','r') as curios:
        read_curios = csv.DictReader(curios)

        for line in read_curios:
            if line['pontos'] == f'{pontos}':
                print('curiosidade')
                print(line[nome])
                #agr é só botar pra retornar 'line[nome]'
        if int(line['pontos']) > max_pts:
            max_pts = int(line['pontos'])

def display_curiosity(shape_type,presi_dict):
    for presidente in presi_dict:
        if presi_dict[presidente] > int(max_pts):
            presi_dict[presidente] = 0
    if shape_type == "circle":
        presi_dict['circulo'] += 1
        get_curiosity('castelo branco',presi_dict['circulo'])

    if shape_type == "square":
        presi_dict['quadrado'] += 1
        get_curiosity('geisel',presi_dict['quadrado'])
        
# Loop principal do jogo
running = True
score = 0
clock.tick(60)

max_pts = 0

paused = False

presi_dict = {'circulo':0,'quadrado':0}
font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                paused = not paused
    
    if paused == True:
        continue

    # Atualização do jogo
    all_sprites.update()

    # Verificação de colisão com o coletor
    shape_collisions = pygame.sprite.spritecollide(collector, shapes_group, True)
    for shape in shape_collisions:
        score += 1
        display_curiosity(shape.type,presi_dict)

    # Criação de novas formas
    if random() < 0.02:
        create_shape()

    # Limpeza do canvas
    canvas.fill(WHITE)

    # Desenho dos sprites
    all_sprites.draw(canvas)

    #desenhando o quadro de infromações
    #quadro.draw('olá meus amigos, sejam bem vindos a esta demonstração do jogo dos presidentes, onde o seu objetivo é conseguir o maximo de pontos ao coletar personagens da ditadura militar brasileira. divirta-se jogando e aprendendo fatos sobre o aspecto economico deste periodo tão conturbado da historia brasileirira. Agora preiso testar se esta função realmete funciona, quero dizer, se ela realmente ajusta o tamanho do quaddro dinamicamente.')
    

    # Exibição da pontuação
    text = font.render("Pontuação: " + str(score), True, BLACK)
    canvas.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
