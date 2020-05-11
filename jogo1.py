# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()
# ----- Gera tela principal
WIDTH = 700
HEIGHT = 380
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dungeons of Insper')

# ---- Fundo
background = pygame.image.load('Dungeons/fundonormal.png').convert()

game=True

while game:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            game = False
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    pygame.display.update()

pygame.quit()  