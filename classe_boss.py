import pygame
import random
from ClasseInimigo import Inimigo
from parametros import HEIGHT, WIDTH, CHAR_WIDTH, GRAVITY, STILL, GROUND, ATTACK_char 
from classe_boladefogo import Bullet

class Boss(Inimigo):
    '''Classe do boss e definição de suas movimentações.'''
    def __init__(self, assets, groups):
        super().__init__(assets, groups, 5, "boss")  
        self.groups = groups
        
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