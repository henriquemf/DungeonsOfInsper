#Código baseado no Handout da Aula 13 de Design de Software
# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import sys

pygame.init()
pygame.mixer.init()
# ----- Gera tela principal
WIDTH = 1200
HEIGHT = 600
CHAR_WIDTH = 200
CHAR_HEIGHT = 180
GRAVITY = 2
JUMP_SIZE = 30
GROUND = HEIGHT * 5 //6
# Define estados possíveis do jogador
STILL = 4
JUMPING = 5
FALLING = 6
ATTACK_char = 7
score = 0
lives = 3

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dungeons of Insper')

# ---- Assets
def load_assets():
    assets={}
    assets["background"] = pygame.image.load('Dungeons/fundonormal.png').convert()
    assets["background"] = pygame.transform.scale(assets["background"], (WIDTH, HEIGHT))
    assets["telainicio1"] = pygame.image.load('Dungeons/telainicio1.png').convert()
    assets["telainicio1"] = pygame.transform.scale(assets["telainicio1"], (WIDTH, HEIGHT))
    assets["char_img"]= pygame.image.load('Dungeons/teste_heroi_2.png').convert_alpha()
    assets["char_img"] = pygame.transform.scale(assets["char_img"], (CHAR_WIDTH, CHAR_HEIGHT))
    assets["char_atacc"] = pygame.image.load('Dungeons/teste_heroi.png').convert_alpha()
    assets["char_atacc"] = pygame.transform.scale(assets["char_atacc"], (CHAR_WIDTH, CHAR_HEIGHT))
    assets["mob_atacc"] = pygame.image.load('Dungeons/mob_certo.png').convert_alpha()
    assets["mob_atacc"] = pygame.transform.scale(assets["mob_atacc"], (CHAR_WIDTH - 25, CHAR_HEIGHT-40))
    assets["mob_normal"] = pygame.image.load('Dungeons/sprite_2_mob.png').convert_alpha()
    assets["mob_normal"] = pygame.transform.scale(assets["mob_normal"], (CHAR_WIDTH - 25, CHAR_HEIGHT-40))
    assets["mob_atacc2"] = pygame.image.load('Dungeons/sprite_2_mob_vermelho (1).png').convert_alpha()
    assets["mob_atacc2"] = pygame.transform.scale(assets["mob_atacc2"], (CHAR_WIDTH - 25, CHAR_HEIGHT-40))
    assets["mob_normal2"] = pygame.image.load('Dungeons/sprite_2_mob_vermelho.png').convert_alpha()
    assets["mob_normal2"] = pygame.transform.scale(assets["mob_normal2"], (CHAR_WIDTH - 25, CHAR_HEIGHT-40))
    assets["boss"] = pygame.image.load('Dungeons/boss_bola_de_fogo.png').convert_alpha()
    assets["boss"] = pygame.transform.scale(assets["boss"], (CHAR_WIDTH+10, CHAR_HEIGHT+20))
    assets["fundo_boss"] = pygame.image.load('Dungeons/fundo_boss.png'). convert_alpha()
    assets["fundo_boss"] = pygame.transform.scale(assets["fundo_boss"], (WIDTH, HEIGHT))
    assets["fundo2"] = pygame.image.load('Dungeons/fundo2.png').convert_alpha()
    assets["fundo2"] = pygame.transform.scale(assets["fundo2"], (WIDTH, HEIGHT))
    assets["bola_de_fogo"] = pygame.image.load('Dungeons/bola_de_fogo.png').convert_alpha()
    assets["bola_de_fogo"] = pygame.transform.scale(assets["bola_de_fogo"], (100,50))
    assets["score_font"] = pygame.font.Font('Dungeons/OldLondon.ttf', 28)
    assets["score_font2"] = pygame.font.Font('Dungeons/PressStart2P.ttf', 28)
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
        # self.lives = 3
        self.attacking = False
        

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
        # if self.attacking:
        #     self.image = self.assets["char_atacc"]
        # else:
        #     self.image = self.assets["char_img"]
        
        now = pygame.time.get_ticks()
        if self.attacking and now - self.last_attack > self.time_to_attack:
            self.attacking = False
            self.image = self.assets["char_img"]

    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING
    
    def attack(self):
        if not self.attacking:
            self.attacking = True
            self.image = self.assets["char_atacc"]
            self.last_attack = pygame.time.get_ticks()
            self.time_to_attack = 2000

class Mob(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets
        self.image = assets["mob_normal"]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT*5//6 - 10
        self.rect.x = random.randint(WIDTH // 2, WIDTH-CHAR_WIDTH)
        self.speedy = 0
        self.speedx = 1
        self.last_attack = pygame.time.get_ticks()
        self.last_jump = pygame.time.get_ticks()
        self.time_to_jump = random.randint(2000, 5000)
        self.atacou = False
        self.state = STILL

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

class Mob2(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets
        self.image = assets["mob_normal2"]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT*5//6 - 10
        self.rect.x = random.randint(WIDTH // 2, WIDTH-CHAR_WIDTH)
        self.speedy = 0
        self.speedx = 1
        self.last_attack = pygame.time.get_ticks()
        self.last_jump = pygame.time.get_ticks()
        self.time_to_jump = random.randint(2000, 5000)
        self.atacou = False
        self.state = STILL

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_attack > 1000:
            if not self.atacou:
                self.atacou = True
                self.image = self.assets["mob_atacc2"]
                self.state = ATTACK_char
            elif now - self.last_attack > 1500:
                self.atacou = False
                self.last_attack = now
                self.image = self.assets["mob_normal2"]
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

class Boss(pygame.sprite.Sprite):
    def __init__(self, assets, groups):
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
     
    def shoot(self):
        new_bullet = Bullet(self.assets, self.rect.centerx, self.rect.centery)
        self.groups['all_sprites'].add(new_bullet)
        self.groups['all_bullets'].add(new_bullet)
        #self.assets['pew_sound'].play()

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

class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets, centerx, centery):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['bola_de_fogo']
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



#-------Tela do jogo
SAIR = -1
TELA0 = -2
TELA1 = 1
TELA2 = 2
TELA3 = 9
#----- Tela 1

def tela0(window):
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
                if event.key == pygame.K_k:
                    player.attack()
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
        
        global lives
        global score
        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_mobs, False, pygame.sprite.collide_mask)
            if player.attacking:
                for mob in hits:
                    mob.kill()
                    score += 100
                    print(score)
                if score % 1000 == 0:
                    lives += 1              
            else:
                for mob in hits:
                    lives -= 1
                    if lives == 0:
                        return SAIR
                        
            if len(all_mobs) == 0 : 
                return TELA1
        
        window.fill((0, 0, 0))  # Preenche com a cor preta
        window.blit(assets['telainicio1'], (0, 0))
        all_sprites.draw(window)

        text_surface = assets['score_font'].render("{:08d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)
        
        text_surface = assets['score_font2'].render(chr(9829) * lives, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)
    
        pygame.display.update()    

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

    for i in range(5):
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
                state = DONE
                return SAIR
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_LEFT:
                    player.speedx -= 2
                if event.key == pygame.K_RIGHT:
                    player.speedx += 2
                if event.key == pygame.K_k:
                    player.attack()
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.jump()
            if event.type == pygame.KEYUP:
                if event.key in keys_down and keys_down[event.key]:
                    if event.key == pygame.K_LEFT:
                        player.speedx += 2
                    if event.key == pygame.K_RIGHT:
                        player.speedx -= 2
                    # if event.key == pygame.K_k:
                    #     player.attack()
                keys_down[event.key] = False
        #Atualiza Jogo

        all_sprites.update()
        
        global lives
        global score
        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_mobs, False, pygame.sprite.collide_mask)
            if player.attacking:
                for mob in hits:
                    mob.kill()
                    score += 100
                    print(score)
                if score % 1000 == 0:
                    lives += 1
            else:
                for mobs in hits:
                    lives -= 1
                    if lives == 0:
                        return SAIR
                        
            if len(all_mobs) == 0 : 
                return TELA2
            


        window.fill((0, 0, 0))  # Preenche com a cor preta
        window.blit(assets['background'], (0, 0))
        all_sprites.draw(window)

        text_surface = assets['score_font'].render("{:08d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)
        
        text_surface = assets['score_font2'].render(chr(9829) * lives, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)
    
        pygame.display.update()

#----- Tela 2 

def tela2(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    FPS = 15

    all_sprites = pygame.sprite.Group()
    all_mobs2 = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_mobs2'] = all_mobs2
    player = Character(groups, assets)
    all_sprites.add(player)



    DONE = 0
    PLAYING = 3
    state = PLAYING
    keys_down = {}
    
    pygame.mixer.music.play(loops=-1)

    available_mobs2 = 12
    last_mob2 = pygame.time.get_ticks()
    
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
                    if event.key == pygame.K_k:
                        player.attack()
                if event.type == pygame.KEYUP:
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 2
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 2
                        if event.key == pygame.K_k:
                            player.attack()
                    keys_down[event.key] = False
        #Atualiza Jogo
        now = pygame.time.get_ticks()
        if available_mobs2 > 0 and now - last_mob2 > 500:
            mob2 = Mob2(assets) 
            all_sprites.add(mob2)
            all_mobs2.add(mob2)
            available_mobs2 -= 1
            last_mob2 = now

        all_sprites.update()
       
        global score
        global lives
        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_mobs2, False, pygame.sprite.collide_mask)
            if player.attacking:
                for mob2 in hits:
                    mob2.kill()
                    score += 100
                    print(score)
                if score % 1000 :
                    lives += 1
            else:
                for mob2 in hits:
                    lives -= 1
                    if lives == 0:
                        return SAIR

            if len(all_mobs2) == 0 and available_mobs2 == 0:
                return TELA3
        
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets['fundo2'], (0, 0))
        all_sprites.draw(window)

        text_surface = assets['score_font'].render("{:08d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        text_surface = assets['score_font2'].render(chr(9829) * lives, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador
  

def tela3(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    FPS = 15

    all_sprites = pygame.sprite.Group()
    all_bosses = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_bosses'] = all_bosses
    groups['all_bullets'] = all_bullets
    player = Character(groups, assets)
    all_sprites.add(player)

    
    for i in range(1):
        boss = Boss(assets, groups) 
        all_sprites.add(boss)
        all_bosses.add(boss)
    

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
                    if event.key == pygame.K_k:
                        player.attack()
                if event.type == pygame.KEYUP:
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 2
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 2
                        if event.key == pygame.K_k:
                            player.attack()
                    keys_down[event.key] = False
        #Atualiza Jogo
        #available_mobs= 3
        #now = pygame.time.get_ticks()
        #if available_mobs > 0 and now - last_mob > 500:
        #    mob = Mob(assets) 
        #    all_sprites.add(mob)
        #    all_mobs.add(mob)
        #    available_mobs -= 1
        #    last_mob = now

        all_sprites.update()
        global score
        global lives
        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_bosses, False, pygame.sprite.collide_mask)
            if player.attacking:
                for boss in hits:
                    boss.kill()
                    score+=100
            else:
                for boss in hits:
                    lives -= 1
                    if lives == 0:
                        return SAIR
        
        
            hits = pygame.sprite.spritecollide(player, all_bullets, True, pygame.sprite.collide_mask)
            for bullet in hits:
                # player.lives -= 3
                lives -= 3
                # if player.lives == 0:
                if lives == 0:
                    return SAIR
     
    
            if len(all_bosses) == 0:
                return SAIR
        
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets['fundo_boss'], (0, 0))
        all_sprites.draw(window)
        
        text_surface = assets['score_font'].render("{:08d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        text_surface = assets['score_font2'].render(chr(9829) * lives, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()

estado = TELA1
while estado != SAIR:
    if estado == TELA0:
        estado = tela0(window)
    elif estado == TELA1:
        estado = tela1(window)
    elif estado == TELA2:
        estado = tela2(window)
    elif estado == TELA3:
        estado= tela3(window)    

pygame.quit()
sys.exit()