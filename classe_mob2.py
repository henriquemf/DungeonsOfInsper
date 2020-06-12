#Classe do segundo inimigo e definição de suas principais movimentações.
import pygame
import random 
from parametros import HEIGHT, WIDTH, CHAR_WIDTH, GRAVITY, STILL, GROUND, ATTACK_char 

class Mob2(pygame.sprite.Sprite):
    '''Classe do primeiro inimigo e definição de suas movimentações.'''
    def __init__(self, assets, groups):
        '''
        Params:
        - groups: dicionário de grupos de sprites do mob 2.
        - assets: dicionário de assets com o mob2 de machado normal e mob atacando.
        - funções: pulo do mob, ataque e definição das duas vidas.
        '''
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets
        self.image = assets["mob_normal2"]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT*5//6 - 10
        self.rect.x = random.randint(WIDTH // 2, WIDTH-CHAR_WIDTH)
        self.speedy = 0
        self.speedx = 1
        self.last_attack = pygame.time.get_ticks()
        self.last_jump = pygame.time.get_ticks()
        self.time_to_jump = random.randint(2000, 5000)
        self.atacou = False
        self.state = STILL
        self.lives = 2
    
    #mudança de imagem se estiver atacando ou se estiver em seu estado normal.
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_attack > 1000:
            if not self.atacou:
                self.atacou = True
                self.image = self.assets["mob_atacc2"]
                self.state = ATTACK_char
            elif now - self.last_attack > 1500:
                self.atacou = False
                self.last_attack = now
                self.image = self.assets["mob_normal2"]
        if now - self.last_jump > self.time_to_jump: #definindo pulo do mob2
            self.time_to_jump = random.randint(1000, 2000)
            self.last_jump = now
            self.speedy -= random.randint( 30, 40)
        self.speedy += GRAVITY
        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.speedy = 0        
        
        self.rect.x += self.speedx
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speedx = -self.speedx
        self.rect.y += self.speedy