# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()
pygame.mixer.init()
# ----- Gera tela principal
WIDTH = 700
HEIGHT = 380
CHAR_WIDTH = 200
CHAR_HEIGHT = 180
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dungeons of Insper')

# ---- Fundo
assets={}
assets["background"] = pygame.image.load('Dungeons/fundonormal.png').convert()
assets["char_img"]= pygame.image.load ('Dungeons/manuelcerto.png').convert_alpha()
assets["char_img"] = pygame.transform.scale(assets["char_img"], (CHAR_WIDTH, CHAR_HEIGHT))
pygame.mixer.music.load('Dungeons/videoplayback.ogg')
pygame.mixer.music.set_volume(0.4)
game=True

class Character(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets["char_img"]
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

clock = pygame.time.Clock()
FPS = 15

all_sprites = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
player = Character(groups, assets)
all_sprites.add(player)

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

pygame.quit()  