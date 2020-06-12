import pygame
import random 
from parametros import HEIGHT, WIDTH, CHAR_WIDTH, GRAVITY, STILL, GROUND, ATTACK_char 
from classe_flecha import Flecha

class Arqueiro(pygame.sprite.Sprite):
    '''Classe do primeiro inimigo e definição de suas movimentações.'''
    def __init__(self, assets, groups):
        '''
        Params:
        - groups: dicionário de grupos de sprites do arqueiro.
        - assets: dicionário de assets com o arqueiro com arco e flecha.
        - funções: tiro do arqueiro para ataque.
        '''
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets
        self.groups = groups
        self.image = assets["arqueiro"]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT*5//6 - 10
        self.rect.x = random.randint(WIDTH // 2, WIDTH-CHAR_WIDTH)
        self.speedx = 1
        self.last_attack2 = pygame.time.get_ticks()
        self.atacou2 = False
        self.state = STILL
        self.lives = 1

    #tiro de flecha do arqueiro. 
    def shoot(self):
        new_flecha = Flecha(self.assets, self.rect.centerx, self.rect.centery)
        self.groups['all_sprites'].add(new_flecha)
        self.groups['all_flechas'].add(new_flecha)
    
    #ataque do arqueiro. 
    def update(self):
        self.rect.x += self.speedx
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speedx = -self.speedx
        now = pygame.time.get_ticks()
        if now - self.last_attack2 > 3000:
            if not self.atacou2:
                self.atacou2 = True
                self.image = self.assets["arqueiro"]
                self.state = ATTACK_char
                self.shoot()
            elif now - self.last_attack2 > 3500:
                self.atacou2 = False
                self.last_attack2 = now
                self.image = self.assets["arqueiro"]