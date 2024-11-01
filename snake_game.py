import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Definir as configurações da tela
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Meu Primeiro Jogo em Python")

# Definir cores
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

snake_element_size = [15, 15]


def random_position():
    pass


snake = {
    "speed": 2,
    "size": snake_element_size,
    "head": {"position": [50, 50]},
    "body": [{"position": [34, 50], "size": 1}],
}

apple = {"position": [100, 100], "size": [13, 13]}


# Loop principal do jogo
running = True
while running:
    # Capturar eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimento do "personagem"
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if snake["head"]["position"][0] > 0:
            snake["head"]["position"][0] -= snake["speed"]

            if snake["head"]["position"][0] - snake["body"][0]["position"][0] == -18:
                snake["body"][0]["position"][0] -= snake["speed"]

    if keys[pygame.K_RIGHT]:
        if snake["head"]["position"][0] < 586:
            snake["head"]["position"][0] += snake["speed"]
            if snake["head"]["position"][0] - snake["body"][0]["position"][0] == 18:
                snake["body"][0]["position"][0] += snake["speed"]

    if keys[pygame.K_UP]:
        if snake["head"]["position"][1] > 0:
            snake["head"]["position"][1] -= snake["speed"]

            if snake["body"][0]["position"][0] < snake["head"]["position"][0]:
                snake["body"][0]["position"][0] += snake["speed"]
            if snake["head"]["position"][1] - snake["body"][0]["position"][1] == -18:
                snake["body"][0]["position"][1] -= snake["speed"]

    if keys[pygame.K_DOWN]:
        if snake["head"]["position"][1] < 586:
            snake["head"]["position"][1] += snake["speed"]

            # Ajusta Posição do corpo em relação a cabeça
            if snake["body"][0]["position"][0] < snake["head"]["position"][0]:
                snake["body"][0]["position"][0] += snake["speed"]
            # Acompanha cabeça
            if snake["head"]["position"][1] - snake["body"][0]["position"][1] == 18:
                snake["body"][0]["position"][1] += snake["speed"]

    # Desenhar a tela
    screen.fill(black)

    # Snake Head
    pygame.draw.rect(
        screen,
        green,
        (
            snake["head"]["position"][0],
            snake["head"]["position"][1],
            snake["size"][0],
            snake["size"][1],
        ),
    )

    # Snake Body

    pygame.draw.rect(
        screen,
        green,
        (
            snake["body"][0]["position"][0],
            snake["body"][0]["position"][1],
            snake["size"][0],
            snake["size"][1],
        ),
    )

    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (
            apple["position"][0],
            apple["position"][1],
            apple["size"][0],
            apple["size"][1],
        ),
    )

    # Atualizar a tela
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Controlar FPS (frames por segundo)
