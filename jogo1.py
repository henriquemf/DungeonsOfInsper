#Código baseado no Handout da Aula 13 de Design de Software
# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init() 
pygame.mixer.init()
# ----- Gera tela principal
WIDTH = 1000
HEIGHT = 500
CHAR_WIDTH = 200
CHAR_HEIGHT = 180
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dungeons of Insper')

# ---- Assets
def load_assets():    
    assets={}
    assets["background"] = pygame.image.load('Dungeons/fundonormal.png').convert()
    assets["background"] = pygame.transform.scale(assets["background"], (WIDTH, HEIGHT))
    assets["char_img"]= pygame.image.load ('Dungeons/manuelcerto.png').convert_alpha()
    assets["char_img"] = pygame.transform.scale(assets["char_img"], (CHAR_WIDTH, CHAR_HEIGHT))
    assets["mob_img"] = pygame.image.load('Dungeons/soldadinho.png').convert_alpha()
    assets["mob_img"] = pygame.transform.scale(assets["mob_img"], (CHAR_WIDTH - 10, CHAR_HEIGHT-10))
    pygame.mixer.music.load('Dungeons/rpgsong.ogg')
    pygame.mixer.music.set_volume(0.1)
    return assets
game=True

class Character(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets["char_img"]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.groups = groups
        self.assets = assets
    
    def update(self): 
        self.rect.x += self.speedx
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Mob(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets["mob_img"]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.rect.x = random.randint(100, WIDTH-CHAR_WIDTH)
        self.speedx = 1
    
    def update(self): 
        self.rect.x += self.speedx
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speedx = -self.speedx

def game_screen(window):
    clock = pygame.time.Clock()
    game=True
    assets = load_assets()
    FPS = 15

    all_sprites = pygame.sprite.Group()
    all_mobs = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_mobs'] = all_mobs
    player = Character(groups, assets)
    mob = Mob(assets)
    all_sprites.add(player)
    all_sprites.add(mob)

    pygame.mixer.music.play(loops=-1)
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 2
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 2
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.speedx += 2
                    if event.key == pygame.K_RIGHT:
                        player.speedx -= 2
                        
        all_sprites.update()

        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets['background'], (0, 0))
        all_sprites.draw(window)

        pygame.display.update()
game_screen(window)

pygame.quit()  