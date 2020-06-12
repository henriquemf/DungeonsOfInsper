import pygame

class Flecha(pygame.sprite.Sprite):
    '''Classe da flecha do arqueiro e definição de suas movimentações.'''
    def __init__(self, assets, centerx, centery):
        '''
        Params:
        - assets: dicionário de assets com a flecha do arqueiro.
        - funções: movimentação da flecha.
        '''
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['flecha']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.speedx = -10  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.right < 0:
            self.kill()
