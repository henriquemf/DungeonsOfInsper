#Código baseado no Handout da Aula 13 de Design de Software
# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import sys

pygame.init()
pygame.mixer.init()
# ----- Gera tela principal
WIDTH = 1000
HEIGHT = 500
CHAR_WIDTH = 200
CHAR_HEIGHT = 180
GRAVITY = 2
JUMP_SIZE = 30
GROUND = HEIGHT * 5 //6
# Define estados possíveis do jogador
STILL = 4
JUMPING = 5
FALLING = 6

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dungeons of Insper')

# ---- Assets
def load_assets():
    assets={}
    assets["background"] = pygame.image.load('Dungeons/fundonormal.png').convert()
    assets["background"] = pygame.transform.scale(assets["background"], (WIDTH, HEIGHT))
    assets["char_img"]= pygame.image.load('Dungeons/teste_heroi_2.png').convert_alpha()
    assets["char_img"] = pygame.transform.scale(assets["char_img"], (CHAR_WIDTH, CHAR_HEIGHT))
    assets["char_atacc"]= pygame.image.load('Dungeons/teste_heroi.png').convert_alpha()
    assets["char_"] = pygame.transform.scale(assets["char_atacc"], (CHAR_WIDTH, CHAR_HEIGHT))
    assets["mob_atacc"] = pygame.image.load('Dungeons/mob_certo.png').convert_alpha()
    assets["mob_atacc"] = pygame.transform.scale(assets["mob_atacc"], (CHAR_WIDTH - 25, CHAR_HEIGHT-40))
    assets["mob_normal"] = pygame.image.load('Dungeons/sprite_2_mob.png').convert_alpha()
    assets["mob_normal"] = pygame.transform.scale(assets["mob_normal"], (CHAR_WIDTH - 25, CHAR_HEIGHT-40))
    
    pygame.mixer.music.load('Dungeons/videoplayback.ogg')
    pygame.mixer.music.set_volume(0.1)
    return assets

class Character(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
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
        self.lives = 2


    def update(self):
        self.rect.x += self.speedx
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        self.speedy += GRAVITY
        self.rect.y += self.speedy
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        # Se bater no chão, para de cair
        if self.rect.bottom > GROUND:
            # Reposiciona para a posição do chão
            self.rect.bottom = GROUND
            # Para de cair
            self.speedy = 0
            self.state = STILL

    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING
            

class Mob(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets
        self.image = assets["mob_normal"]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT*5//6 - 10
        self.rect.x = random.randint(WIDTH // 2, WIDTH-CHAR_WIDTH)
        self.speedx = 1
        self.last_attack = pygame.time.get_ticks()
        self.atacou = False
        # self.state = STILL

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speedx = -self.speedx
        now = pygame.time.get_ticks()
        if now - self.last_attack > 1000:
            if not self.atacou:
                self.atacou = True
                self.image = self.assets["mob_atacc"]
                # self.state = ATTACK
            elif now - self.last_attack > 1500:
                self.atacou = False
                self.last_attack = now
                self.image = self.assets["mob_normal"]

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

    for i in range(1):
        mob = Mob(assets)
        all_sprites.add(mob)
        all_mobs.add(mob)

    DONE = 0
    PLAYING = 3
    state = PLAYING
    keys_down = {}
    #score = 0
    #lives = 3
    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
                return SAIR
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_LEFT:
                    player.speedx -= 2
                if event.key == pygame.K_RIGHT:
                    player.speedx += 2
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.jump()
            if event.type == pygame.KEYUP:
                if event.key in keys_down and keys_down[event.key]:
                    if event.key == pygame.K_LEFT:
                        player.speedx += 2
                    if event.key == pygame.K_RIGHT:
                        player.speedx -= 2
                keys_down[event.key] = False
        #Atualiza Jogo

        all_sprites.update()

        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_mobs, True, pygame.sprite.collide_mask)
            for mob in hits:
                player.lives -= 1
                if player.lives == 0:
                    return SAIR
            
            
            
            if len(all_mobs) == 0:
                return TELA2

            hits = pygame.sprite.spritecollide(player, all_mobs, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                # Toca o som da colisão
                #assets['boom_sound'].play()
                player.kill()
                #lives -= 1
                #explosao = Explosion(player.rect.center, assets)
                #all_sprites.add(explosao)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lives == 0:
                    state = DONE
                else:
                    state = PLAYING
                    player = Ship(groups, assets)
                    all_sprites.add(player)

        window.fill((0, 0, 0))  # Preenche com a cor preta
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
    keys_down = {}
    
    pygame.mixer.music.play(loops=-1)
    
    while state != DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return SAIR
            if state == PLAYING:    
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 2
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 2
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        player.jump()
                if event.type == pygame.KEYUP:
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 2
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 2
                    keys_down[event.key] = False
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
sys.exit()

