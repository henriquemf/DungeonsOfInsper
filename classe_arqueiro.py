import pygame
import random 
from ClasseInimigo import Inimigo
from parametros import HEIGHT, WIDTH, CHAR_WIDTH, GRAVITY, STILL, GROUND, ATTACK_char 
from classe_flecha import Flecha

class Arqueiro(Inimigo):
    '''Classe do primeiro inimigo e definição de suas movimentações.'''
    def __init__(self, assets, groups):
        super().__init__(assets, groups, 1, "arqueiro")
        self.groups = groups

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
        if now - self.last_attack > 3000:
            if not self.atacou:
                self.atacou = True
                self.image = self.assets["arqueiro"]
                self.state = ATTACK_char
                self.shoot()
            elif now - self.last_attack > 3500:
                self.atacou = False
                self.last_attack = now
                self.image = self.assets["arqueiro"]