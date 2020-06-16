#Código baseado no Handout da Aula 13 de Design de Software
#e baseado nos exemplos passados pelo professor do curso. 
# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import sys
from assets import load_assets
from sprites import Character
from classe_mob import Mob
from classe_mob2 import Mob2
from classe_arqueiro import Arqueiro
from classe_flecha import Flecha
from classe_boss import Boss
from classe_boladefogo import Bullet
from def_pretelas import *
from telas_principais import *

pygame.init()
pygame.mixer.init()

estado = TELA_1
while estado != SAIR:
    if estado == TELA_1:
        estado = tela_1(window)
    elif estado == TELA0:
        estado = tela0(window)
    elif estado == TELA_ANTE1:
        estado = tela_ante1(window)    
    elif estado == TELA1:
        estado = tela1(window)
    elif estado == TELA2:
        estado = tela2(window)
    elif estado == TELA3:
        estado = tela3(window)
    elif estado == TELA4:
        estado = tela4(window)
    elif estado == TELA_GAMEOVER:
        estado = tela_gameover(window)    
    elif estado == TELA_WIN:
        estado = tela_win(window)
    elif estado == TELA_PRE_2:
        estado = tela_pre_2(window)
    elif estado == TELA_PRE_3:
        estado = tela_pre_3(window)
    elif estado == TELA_PRE_BOSS:
        estado = tela_pre_boss(window)
pygame.quit()
sys.exit()

#DE TODOS NÓS DO GRUPO 1, MUITO OBRIGADA PROFESSOR PELO CURSO E PELO PROJETO! 
