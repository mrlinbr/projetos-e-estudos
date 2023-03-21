import pygame
from sys import exit
from time import sleep
from random import randint,choice

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_walk_1 = pygame.image.load("UltimatePygameIntro-main/graphics/Player/player_walk_1.png").convert_alpha()
		player_walk_2 = pygame.image.load("UltimatePygameIntro-main/graphics/Player/player_walk_2.png").convert_alpha()
		self.player_walk = [player_walk_1,player_walk_2]
		self.player_jump = pygame.image.load("UltimatePygameIntro-main/graphics/Player/jump.png").convert_alpha()
		
		self.player_index = 0

		self.image = self.player_walk[self.player_index]
		self.rect = self.image.get_rect(midbottom =(200,300))

		self.gravity = 0

		self.jump_sound = pygame.mixer.Sound("UltimatePygameIntro-main/audio/jump.mp3")
		self.jump_sound.set_volume(0.3)

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
			self.gravity = -20
			self.jump_sound.play()

	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 300:
			self.rect.bottom = 300

	def animation_state(self):
		if self.rect.bottom < 300:
			self.image = self.player_jump
		else:
			self.player_index += 0.1
			if self.player_index >= len(self.player_walk): 
				self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]

	def update(self):
		self.player_input()
		self.apply_gravity()
		self.animation_state()

class Obstacle(pygame.sprite.Sprite):
	def __init__(self, type):
		super().__init__()

		if type == 'snail':
			snail_frame_1 = pygame.image.load("UltimatePygameIntro-main/graphics/snail/snail1.png").convert_alpha()
			snail_frame_2 = pygame.image.load("UltimatePygameIntro-main/graphics/snail/snail2.png").convert_alpha()
			self.frames = [snail_frame_1,snail_frame_2]
			y_pos = 300
		else:
			fly_frame_1 = pygame.image.load("UltimatePygameIntro-main/graphics/Fly/Fly1.png")
			fly_frame_2 = pygame.image.load("UltimatePygameIntro-main/graphics/Fly/Fly2.png")
			self.frames = [fly_frame_1,fly_frame_2]
			y_pos = 210

		self.index = 0
		self.image = self.frames[self.index]
		self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))


	def animation_state(self):
		self.index += 0.1
		if self.index >= len(self.frames):
			self.index = 0
		self.image = self.frames[int(self.index)]

	def destroy(self):
		if self.rect.x <= -100:
			self.kill()

	def update(self):
		self.animation_state()
		self.destroy()
		self.rect.x -= 6

def get_time():
	tempo_jogo = (pygame.time.get_ticks()//10)*10- ticks_atual
	time_clock = font.render(f"{tempo_jogo}"[:-3],False, "black")
	time_rect = time_clock.get_rect(midbottom = (400,50))
	tela.blit(time_clock,time_rect)
	return tempo_jogo

def collide_group():
	if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
		obstacle_group.empty()
		return False
	return True

pygame.init()
tela = pygame.display.set_mode((800,400))

pygame.display.set_caption("ligeirinho")

relogio = pygame.time.Clock()

font = pygame.font.Font("UltimatePygameIntro-main/font/Pixeltype.ttf",50)

superfice_de_teste =  pygame.image.load("UltimatePygameIntro-main/graphics/Sky.png").convert()
chao = pygame.image.load("UltimatePygameIntro-main/graphics/ground.png")

pos_x = 80
#intro screen
player_stand = pygame.image.load('UltimatePygameIntro-main/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))
titulo = font.render(f'jump or die',0,'black')
titulo_rect = titulo.get_rect(center = (400,50))

instrucoes = font.render(f'Aperte `espaco` para pular ou morra.',0,'black')
instrucoes_rect = titulo.get_rect(center = (200,350))

best_score = ''
player_gravity = 300
game_run = False
ticks_atual = 0

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1400)

#Grupos de classes
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

back_music = pygame.mixer.Sound("UltimatePygameIntro-main/audio/music.wav")
back_music.set_volume(0.1)
back_music.play(loops= -1)
while True: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()	

		if game_run:
			if event.type == obstacle_timer:
				obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
	
		else:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					game_run = True
					ticks_atual = pygame.time.get_ticks()


	if game_run:			
		tela.blit(superfice_de_teste,(0,0))
		tela.blit(chao,(0,300))
		best_score = str(get_time())

		actual_score = int(pygame.time.get_ticks())
		
		player.draw(tela)
		player.update()

		obstacle_group.draw(tela)
		obstacle_group.update()
		game_run = collide_group()

	else:
		tela.fill((94,129,162))
		tela.blit(player_stand,player_stand_rect)
		tela.blit(titulo,titulo_rect)
		
		ponts = font.render(f'melhor pontuacao: {best_score[:-3]}',0,"black")
		ponts_rect = ponts.get_rect(center = (350, 350))
		if best_score == 0:
			tela.blit(instrucoes,instrucoes_rect)
		else: tela.blit(ponts, ponts_rect)	
	pygame.display.update()
	relogio.tick(60)