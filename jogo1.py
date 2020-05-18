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
    assets["mob_img"] = pygame.transform.scale(assets["mob_img"], (CHAR_WIDTH - 25, CHAR_HEIGHT-40))
    pygame.mixer.music.load('Dungeons/rpgsong.ogg')
    pygame.mixer.music.set_volume(0.1)
    return assets

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
        self.rect.bottom = HEIGHT - 10
        self.rect.x = random.randint(WIDTH // 2, WIDTH-CHAR_WIDTH)
        self.speedx = 1

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speedx = -self.speedx

#-------Tela do jogo
SAIR = -1
TELA1 = 1
TELA2 = 2

#----- Tela 1

def tela1(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    FPS = 15

    all_sprites = pygame.sprite.Group()
    all_mobs = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_mobs'] = all_mobs
    player = Character(groups, assets)
    all_sprites.add(player)

    for i in range(2):
        mob = Mob(assets)
        all_sprites.add(mob)
        all_mobs.add(mob)

    DONE = 0
    PLAYING = 3
    state = PLAYING

    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
                return SAIR
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
        #Atualiza Jogo

        all_sprites.update()

        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_mobs, True, pygame.sprite.collide_mask)
            if len(all_mobs) == 0:
                return TELA2

        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets['background'], (0, 0))
        all_sprites.draw(window)

        pygame.display.update()

#----- Tela 2 

def tela2(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    FPS = 15

    all_sprites = pygame.sprite.Group()
    all_mobs = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_mobs'] = all_mobs
    player = Character(groups, assets)
    all_sprites.add(player)

    for i in range(4):
        mob = Mob(assets)
        all_sprites.add(mob)
        all_mobs.add(mob)

    DONE = 0
    PLAYING = 3
    state = PLAYING

    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
                return SAIR
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
        #Atualiza Jogo

        all_sprites.update()

        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_mobs, True, pygame.sprite.collide_mask)

        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets['background'], (0, 0))
        all_sprites.draw(window)

        pygame.display.update()


estado = TELA1
while estado != SAIR:
    if estado == TELA1:
        estado = tela1(window)
    elif estado == TELA2:
        estado = tela2(window)

pygame.quit()