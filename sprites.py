import pygame
from parametros import *

class Character(pygame.sprite.Sprite):
    '''Classe do personagem principal e definição de suas movimentações.'''
    def __init__(self, groups, assets):
        '''
        Params:
        - groups: dicionário de grupos de sprites
        - assets: dicionário de assets
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = assets["char_img"]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT//6 - 10
        self.speedx = 0
        self.groups = groups
        self.assets = assets
        self.rect.top = 0
        self.speedy = 0
        self.state = STILL
        # self.lives = 3
        self.attacking = False
        

    def update(self):
        self.rect.x += self.speedx
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        self.speedy += GRAVITY
        self.rect.y += self.speedy
        # Atualiza o estado para caindo (pulo)
        if self.speedy > 0:
            self.state = FALLING
        # Se bater no chão, para de cair
        if self.rect.bottom > GROUND:
            # Reposiciona para a posição do chão
            self.rect.bottom = GROUND
            # Para de cair
            self.speedy = 0
            self.state = STILL
        now = pygame.time.get_ticks() #imagem normal quando não está atacando.
        if self.attacking and now - self.last_attack > self.time_to_attack:
            self.attacking = False
            self.image = self.assets["char_img"]
    #definição do pulo do presonagem.
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING
    #definição do ataque do personagem.
    def attack(self):
        if not self.attacking:
            self.attacking = True
            self.image = self.assets["char_atacc"]
            self.last_attack = pygame.time.get_ticks()
            self.time_to_attack = 300
