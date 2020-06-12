import pygame
import random 
from parametros import HEIGHT, WIDTH, CHAR_WIDTH, GRAVITY, STILL, GROUND, ATTACK_char 
from classe_boladefogo import Bullet

class Boss(pygame.sprite.Sprite):
    '''Classe do boss e definição de suas movimentações.'''
    def __init__(self, assets, groups):
        '''
        Params:
        - groups: dicionário de grupos de sprites.
        - assets: dicionário de assets.
        -funções: definição do ataque do boss.
        '''
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets
        self.groups = groups
        self.image = assets["boss"]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT*5//6 - 10
        self.rect.x = random.randint(WIDTH // 2, WIDTH-CHAR_WIDTH)
        self.speedx = 1
        self.last_attack = pygame.time.get_ticks()
        self.atacou = False
        self.state = STILL
    # definição da arma do boss: bola de fogo. 
    def shoot(self):
        new_bullet = Bullet(self.assets, self.rect.centerx, self.rect.centery)
        self.groups['all_sprites'].add(new_bullet)
        self.groups['all_bullets'].add(new_bullet)
  
    #tempo para atacar.
    def update(self):
        self.rect.x += self.speedx
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speedx = -self.speedx
        now = pygame.time.get_ticks()
        if now - self.last_attack > 2000:
            if not self.atacou:
                self.atacou = True
                self.image = self.assets["boss"]
                self.state = ATTACK_char
                self.shoot()
            elif now - self.last_attack > 2500:
                self.atacou = False
                self.last_attack = now
                self.image = self.assets["boss"]