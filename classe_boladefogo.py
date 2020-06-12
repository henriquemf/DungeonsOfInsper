import pygame

class Bullet(pygame.sprite.Sprite):
    ''' Classe da bola de fogo e definição de sua movimentação'''
    # Construtor da classe.
    def __init__(self, assets, centerx, centery):
        ''' Params:
        -groups : dicionario do grupo de sprites.
        -assets : carregar imagem da bola de fogo
        - funções: a movimentação da bola de fogo'''
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['bola_de_fogo']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.rect.centerx = centerx
        self.rect.centery = centery
        self.speedx = -10  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.right < 0:
            self.kill()
