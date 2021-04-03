import pygame
import random 
from parametros import HEIGHT, WIDTH, CHAR_WIDTH, GRAVITY, STILL, GROUND, ATTACK_char 

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, assets, groups, lives, assetName):
        '''
        Params:
        - groups: dicionário de grupos de sprites do mob 1.
        - assets: dicionário de assets com o mob normal e mob atacando.
        - funções: pulo do mob e ataque.
        '''
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets
        self.image = assets[assetName]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT*5//6 - 10
        self.rect.x = random.randint(WIDTH // 2, WIDTH-CHAR_WIDTH)
        self.speedx = 1
        self.last_attack = pygame.time.get_ticks()
        self.atacou = False
        self.state = STILL
        self.lives = lives