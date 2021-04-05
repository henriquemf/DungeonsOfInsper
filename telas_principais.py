import pygame
import random
from assets import load_assets
from parametros import * 
from sprites import Character
from classe_mob import Mob
from classe_mob2 import Mob2
from classe_arqueiro import Arqueiro
from classe_flecha import Flecha
from classe_boss import Boss
from classe_boladefogo import Bullet

"Função que determina movimento do personagem"
def movement(player, evento):
    keys_down = {}
    if evento.type == pygame.KEYDOWN:
        keys_down[evento.key] = True
        if evento.key == pygame.K_LEFT:
            player.speedx -= 2
        if evento.key == pygame.K_RIGHT:
            player.speedx += 2
        if evento.key == pygame.K_SPACE or evento.key == pygame.K_UP:
            player.jump()
        if evento.key == pygame.K_k:
            player.attack()
    if evento.type == pygame.KEYUP:
        if evento.key == pygame.K_LEFT:
            player.speedx += 2
        if evento.key == pygame.K_RIGHT:
            player.speedx -= 2
        keys_down[evento.key] = False

''' definição das principais telas de ação do jogo'''

def tela0(window):
    ''' tela de tutorial para o jogador aprender na prática como será o jogo'''
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Dungeons/florestacerto.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()

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

    for i in range(3):
        mob = Mob(assets, groups)
        all_sprites.add(mob)
        all_mobs.add(mob)
    
    global lives
    global score
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
            if state == PLAYING:
                evento = event
                movement(player, evento)
        #Atualiza Jogo

        all_sprites.update()
       
        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_mobs, False, pygame.sprite.collide_mask)
            for mob in hits:
                if player.attacking:
                    mob.kill()
                    score += 100
                    print(score)
                    if score % 1000 == 0:
                        lives += 1
                else:
                    lives -= 1
                    if lives == 0:
                        return TELA_GAMEOVER
                        
            if len(all_mobs) == 0 : 
                return TELA_ANTE1
        
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
    ''' tela 1 que contempla mobs de menor dificuldade para vencer'''
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Dungeons/videoplayback.ogg')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()


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

    for i in range(10):
        mob = Mob(assets, groups)
        all_sprites.add(mob)
        all_mobs.add(mob)
    
    global lives
    global score
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
            if state == PLAYING:
                evento = event
                movement(player, evento)
        #Atualiza Jogo

        all_sprites.update()

        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_mobs, False, pygame.sprite.collide_mask)
            for mob in hits:
                if player.attacking:
                    mob.kill()
                    score += 100
                    print(score)
                    if score % 1000 == 0:
                        lives += 1
                else:
                    for mobs in hits:
                        lives -= 1
                        if lives == 0:
                            return TELA_GAMEOVER
                        
            if len(all_mobs) == 0 : 
                return TELA_PRE_2
            


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

def tela2(window):
    ''' tela que contempla o segundo mob que tem duas vidas e um machado'''
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Dungeons/tela2.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()


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
      
    global score
    global lives
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
                evento = event
                movement(player, evento)
        #Atualiza Jogo
        now = pygame.time.get_ticks()
        if available_mobs2 > 0 and now - last_mob2 > 500:
            mob2 = Mob2(assets, groups) 
            all_sprites.add(mob2)
            all_mobs2.add(mob2)
            available_mobs2 -= 1
            last_mob2 = now

        all_sprites.update()
        

        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_mobs2, False, pygame.sprite.collide_mask)
            for mob2 in hits:
                if player.attacking:
                    mob2.lives -=1
                    if mob2.lives == 0:
                        mob2.kill()
                        score += 100
                        print(score)
                        if score % 1000 == 0 :
                            lives += 1
                else:
                    lives -= 1
                    if lives == 0:
                        return TELA_GAMEOVER

            if len(all_mobs2) == 0 and available_mobs2 == 0:
                return TELA_PRE_3
        
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
    ''' tela em que o jogador enfrentará o arqueiro que atira flechas que descontam 2 vidas do jogador'''
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Dungeons/musicatela3.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()

    clock = pygame.time.Clock()
    assets = load_assets()
    FPS = 15

    all_sprites = pygame.sprite.Group()
    all_arqueiros = pygame.sprite.Group()
    all_flechas = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_arqueiros'] = all_arqueiros
    groups['all_flechas'] = all_flechas
    player = Character(groups, assets)
    all_sprites.add(player)

    global score
    global lives
    DONE = 0
    PLAYING = 3
    state = PLAYING
    keys_down = {}
    
    pygame.mixer.music.play(loops=-1)

    available_arqueiros = 8
    last_arqueiro = pygame.time.get_ticks()
    
    while state != DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return SAIR
            if state == PLAYING:    
                evento = event
                movement(player, evento)
        #Atualiza Jogo
        
        now = pygame.time.get_ticks()
        if available_arqueiros > 0 and now - last_arqueiro > 3000:
            arqueiro = Arqueiro(assets, groups) 

            all_sprites.add(arqueiro)
            all_arqueiros.add(arqueiro)
            available_arqueiros -= 1
            last_arqueiro = now

        all_sprites.update()

        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_arqueiros, False, pygame.sprite.collide_mask)
            for arqueiro in hits:
                if player.attacking:
                    arqueiro.kill()
                    score+=100
                else:
                    lives -= 1
                    if lives <= 0:
                        return TELA_GAMEOVER

            hits = pygame.sprite.spritecollide(player, all_flechas, True, pygame.sprite.collide_mask)
            for flechas in hits:
                lives -= 2
                if lives <= 0:
                    return TELA_GAMEOVER
     
    
            if len(all_arqueiros) == 0 and available_arqueiros == 0:
                return TELA_PRE_BOSS
        
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets['fundotela3'], (0, 0))
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

def tela4(window):
    ''' tela do chefão, que contempla todos os outros inimigos e com a maior dificuldade do jogo'''
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Dungeons/musicatelaboss_certo.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()

    clock = pygame.time.Clock()
    assets = load_assets()
    FPS = 15
    
    all_sprites = pygame.sprite.Group()
    all_mobs = pygame.sprite.Group()
    all_bosses = pygame.sprite.Group()
    all_flechas = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_mobs'] = all_mobs
    groups['all_bosses'] = all_bosses
    groups['all_flechas'] = all_flechas
    groups['all_bullets'] = all_bullets
    player = Character(groups, assets)
    all_sprites.add(player)

    for i in range(1):
        boss = Boss(assets, groups) 
        all_sprites.add(boss)
        all_bosses.add(boss)
    
    global score
    global lives
    
    lives_boss = 5  
    DONE = 0
    PLAYING = 3
    state = PLAYING
    keys_down = {}
    
    pygame.mixer.music.play(loops=-1)
    last_mob = pygame.time.get_ticks()

    while state != DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return SAIR
            if state == PLAYING:    
                evento = event
                movement(player, evento)
        
        #Atualiza Jogo
        now = pygame.time.get_ticks()
        if boss.alive() and now - last_mob > 500:
            classe_mob = random.choice([Mob, Mob2, Arqueiro])
            mob = classe_mob(assets, groups)
            all_sprites.add(mob)
            all_mobs.add(mob)
            last_mob = now

        all_sprites.update()

        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, all_bosses, False, pygame.sprite.collide_mask)
            for boss in hits:
                if player.attacking:
                    lives_boss-=1
                    if lives_boss == 0:
                        boss.kill()
                else:
                    lives -= 1
                    if lives == 0:
                        return TELA_GAMEOVER

            hits = pygame.sprite.spritecollide(player, all_bullets, False, pygame.sprite.collide_mask)
            for bullet in hits:
                lives -= 3
                if lives <= 0:
                    return TELA_GAMEOVER

            hits = pygame.sprite.spritecollide(player, all_flechas, False, pygame.sprite.collide_mask)
            for flechas in hits:
                lives -= 2
                if lives <= 0:
                    return TELA_GAMEOVER
            
            hits = pygame.sprite.spritecollide(player, all_mobs, False, pygame.sprite.collide_mask)
            for mob in hits:
                if player.attacking:
                    mob.lives -= 1
                    if mob.lives <= 0:
                        mob.kill()
                        score+=100
                    if score % 1000 == 0 :
                        lives += 1
                else:
                    lives -= 1
                    if lives == 0:
                        return TELA_GAMEOVER

            if len(all_bosses) == 0 and len(all_mobs) == 0:
                return TELA_WIN
        
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
