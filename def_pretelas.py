import pygame
from assets import load_assets
from parametros import SAIR, TELA0, TELA1, TELA2, TELA3, TELA4
''' Telas de imagens para avisar o jogador sobre a mudança de nível e dificuldade'''

def tela_gameover(window):
    ''' definição da tela gameover com musica'''
    clock = pygame.time.Clock()
    assets = load_assets()
    FPS = 15

    pygame.mixer.music.stop()
    pygame.mixer.music.load('Dungeons/musicagameover.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()

    all_sprites = pygame.sprite.Group()
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

        window.fill((0, 0, 0))  # Preenche com a cor preta
        window.blit(assets['gameover'], (0, 0))
        all_sprites.draw(window)   
        pygame.display.update()

def tela_win(window):
    ''' definição da tela da vitória com música''' 
    clock = pygame.time.Clock()
    assets = load_assets()
    FPS = 15

    pygame.mixer.music.stop()
    pygame.mixer.music.load('Dungeons/musicawin.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()

    all_sprites = pygame.sprite.Group()
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
                if event.key == pygame.K_SPACE:
                    return SAIR
    
        window.fill((0, 0, 0))  # Preenche com a cor preta
        window.blit(assets['tela_win'], (0, 0))
        all_sprites.draw(window)   
        pygame.display.update()

def tela_1(window):
    '''definição da tela -1, que é a primeira do jogo com instruções, bem-vindo e música'''
    pygame.mixer.music.load('Dungeons/musicatela_1.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()


    clock = pygame.time.Clock()
    assets = load_assets()
    FPS = 15

    all_sprites = pygame.sprite.Group()
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
                if event.key == pygame.K_SPACE:
                    return TELA0
    
        window.fill((0, 0, 0))  # Preenche com a cor preta
        window.blit(assets['Tela_introducao'], (0, 0))
        all_sprites.draw(window)   
        pygame.display.update()

def tela_ante1(window):
    ''' tela antes da 1, com suspense'''
    clock = pygame.time.Clock()
    assets = load_assets()
    FPS = 15

    all_sprites = pygame.sprite.Group()
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
                if event.key == pygame.K_SPACE:
                    return TELA1
    
        window.fill((0, 0, 0))  # Preenche com a cor preta
        window.blit(assets['antes_fase_1'], (0, 0))
        all_sprites.draw(window)   
        pygame.display.update()

def tela_pre_2(window):
    ''' definição da tela antes da 2 que prepara o jogador para enfrentar o mob do machado'''
    
    clock = pygame.time.Clock()
    assets = load_assets()
    FPS = 15

    all_sprites = pygame.sprite.Group()
    DONE = 0
    PLAYING = 3
    state = PLAYING
    keys_down = {}

    
    while state != DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
                return SAIR   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return TELA2
    
        window.fill((0, 0, 0))  # Preenche com a cor preta
        window.blit(assets['tela_pre_2'], (0, 0))
        all_sprites.draw(window)   
        pygame.display.update()

def tela_pre_3(window):
    ''' tela antes da 3 que avisa o jogador que está mudando para a tela 3 do arqueiro'''
    
    clock = pygame.time.Clock()
    assets = load_assets()
    FPS = 15

    all_sprites = pygame.sprite.Group()
    DONE = 0
    PLAYING = 3
    state = PLAYING
    keys_down = {}

    
    while state != DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
                return SAIR   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return TELA3
    
        window.fill((0, 0, 0))  # Preenche com a cor preta
        window.blit(assets['tela_pre_3'], (0, 0))
        all_sprites.draw(window)   
        pygame.display.update()

def tela_pre_boss(window):
    ''' tela antes do boss que avisa o jogador para o último nível'''
    clock = pygame.time.Clock()
    assets = load_assets()
    FPS = 15

    all_sprites = pygame.sprite.Group()
    DONE = 0
    PLAYING = 3
    state = PLAYING
    keys_down = {}

    
    while state != DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
                return SAIR   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return TELA4
    
        window.fill((0, 0, 0))  # Preenche com a cor preta
        window.blit(assets['tela_pre_boss'], (0, 0))
        all_sprites.draw(window)   
        pygame.display.update()
