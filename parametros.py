import pygame

''' 
Parâmetros do jogo.
Atribuição de principais tamanhos das telas e personagens.
Atribuição de estados para os personagens. 
Atribuição do nome do jogo. 
Atribuição de variáveis para as telas. 
''' 

WIDTH = 1200
HEIGHT = 600
CHAR_WIDTH = 200
CHAR_HEIGHT = 180
GRAVITY = 2
JUMP_SIZE = 30
GROUND = HEIGHT * 5 //6
STILL = 4
JUMPING = 5
FALLING = 6
ATTACK_char = 7
score = 0
lives = 3
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dungeons of Insper')


#-Estados das telas do jogo
SAIR = -1
TELA_GAMEOVER = -7
TELA_WIN = 10000
TELA_1 = -10
TELA0 = -2
TELA_ANTE1 = -20
TELA_PRE_3 = -17
TELA_PRE_2 = -18
TELA1 = 1
TELA2 = 2
TELA3 = 9
TELA4 = 4
TELA_PRE_BOSS = -27 
