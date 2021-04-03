import pygame
import random 
from ClasseInimigo import Inimigo
from parametros import HEIGHT, WIDTH, CHAR_WIDTH, GRAVITY, STILL, GROUND, ATTACK_char 

class Mob(Inimigo):
    '''Classe do primeiro inimigo e definição de suas movimentações.'''
    def __init__(self, assets, groups):
        super().__init__(assets, groups, 1, "mob_normal")
        self.speedy = 0
        self.last_jump = pygame.time.get_ticks()
        self.time_to_jump = random.randint(2000, 5000) #pula aleatoriamente


    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_attack > 1000:
            if not self.atacou:
                self.atacou = True
                self.image = self.assets["mob_atacc"]
                self.state = ATTACK_char
            elif now - self.last_attack > 1500:
                self.atacou = False
                self.last_attack = now
                self.image = self.assets["mob_normal"]
        if now - self.last_jump > self.time_to_jump:
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
