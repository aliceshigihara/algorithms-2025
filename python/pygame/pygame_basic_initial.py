import pygame

# inicialização do pygame
pygame.init()

# configuração da tela
screen = pygame.display.set_mode((1280,720))

# variável de relógio
clock = pygame.time.Clock()

# repetição contínua
while True:

    # tratamento de finalização do programa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # pintar a tela de azul
    screen.fill("blue")

    # atualizar a tela
    pygame.display.flip()
