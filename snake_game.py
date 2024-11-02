import pygame
import sys
import random

# Inicializar o Pygame
pygame.init()
pygame.mixer.init()

# Sons
eat_apple = pygame.mixer.Sound("./utils/sounds/apple_bite.mp3")
game_over = pygame.mixer.Sound("./utils/sounds/game_over.mp3")

# Definir as configurações da tela
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Meu Primeiro Jogo em Python")

clock = pygame.time.Clock()
ultima_chamada = pygame.time.get_ticks()


# Definir cores
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
gold = 0

snake_element_size = [15, 15]

# Inicializar a cobra
snake = {
    "speed": 0.8,
    "size": snake_element_size,
    "head": {"position": [50, 50]},
    "body": [{"position": [34, 50]}, {"position": [18, 50]}],
    "direction": "RIGHT",
}

apple = {"position": [100, 100], "size": [19, 19]}

show_golden_apple_index = False
golden_apple = {"position": [-50, -50], "size": [23, 23]}


# Função para mover a cobra
def move_snake():
    global move
    if move == True:
        # Mover o corpo da cobra
        for i in range(len(snake["body"]) - 1, 0, -1):
            snake["body"][i]["position"] = list(snake["body"][i - 1]["position"])

        for i in range(2, len(snake["body"])):
            head_rect = pygame.Rect(
                snake["head"]["position"][0],
                snake["head"]["position"][1],
                snake["size"][0],
                snake["size"][1],
            )

            body_rect = pygame.Rect(
                snake["body"][i]["position"][0],
                snake["body"][i]["position"][1],
                snake["size"][0],
                snake["size"][1],
            )

            # Verifica se a cabeça está completamente dentro do corpo
            if body_rect.contains(head_rect):
                game_over.play()
                print("Body collision - head is completely within body")
                move = False

        # Mover o primeiro segmento do corpo para a posição atual da cabeça
        if len(snake["body"]) > 0:
            snake["body"][0]["position"] = list(snake["head"]["position"])

        # Mover a cabeça na direção correta
        if snake["direction"] == "UP":
            snake["head"]["position"][1] -= snake["speed"]
        elif snake["direction"] == "DOWN":
            snake["head"]["position"][1] += snake["speed"]
        elif snake["direction"] == "LEFT":
            snake["head"]["position"][0] -= snake["speed"]
        elif snake["direction"] == "RIGHT":
            snake["head"]["position"][0] += snake["speed"]


def show_golden_apple():
    golden_apple["position"] = random.sample(range(580), k=2)


def random_golden_apple():
    golden_apple["position"] = [-50, -50]
    snake["body"].append({"position": [-16, -16]})
    snake["body"].append({"position": [-16, -16]})
    snake["body"].append({"position": [-16, -16]})
    snake["body"].append({"position": [-16, -16]})
    snake["body"].append({"position": [-16, -16]})
    snake["body"].append({"position": [-16, -16]})
    snake["body"].append({"position": [-16, -16]})
    snake["body"].append({"position": [-16, -16]})
    snake["body"].append({"position": [-16, -16]})
    snake["body"].append({"position": [-16, -16]})
    snake["speed"] += 0.06


def random_apple():
    apple["position"] = random.sample(range(580), k=2)
    snake["body"].append({"position": [-32, -32]})
    snake["body"].append({"position": [-16, -16]})
    snake["speed"] += 0.03

    print(f"Velociade = {snake["speed"]}")


# Loop principal do jogo
move = True
running = True
while running:
    # Capturar eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    agora = pygame.time.get_ticks()
    if (
        agora - ultima_chamada >= 5000 and show_golden_apple_index == True
    ):  # 5000 ms = 5 segundos
        show_golden_apple()
        show_golden_apple_index = False
        ultima_chamada = agora

    # Capturar maçã
    if pygame.Rect(
        snake["head"]["position"][0],
        snake["head"]["position"][1],
        snake["size"][0],
        snake["size"][1],
    ).colliderect(
        pygame.Rect(
            apple["position"][0],
            apple["position"][1],
            apple["size"][0],
            apple["size"][1],
        )
    ):
        eat_apple.play()
        show_golden_apple_index = True
        random_apple()

    # Capturar maçã de ouro
    if pygame.Rect(
        snake["head"]["position"][0],
        snake["head"]["position"][1],
        snake["size"][0],
        snake["size"][1],
    ).colliderect(
        pygame.Rect(
            golden_apple["position"][0],
            golden_apple["position"][1],
            golden_apple["size"][0],
            golden_apple["size"][1],
        )
    ):
        eat_apple.play()
        random_golden_apple()

    # Detectar teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake["direction"] != "RIGHT":
        snake["direction"] = "LEFT"
    if keys[pygame.K_RIGHT] and snake["direction"] != "LEFT":
        snake["direction"] = "RIGHT"
    if keys[pygame.K_UP] and snake["direction"] != "DOWN":
        snake["direction"] = "UP"
    if keys[pygame.K_DOWN] and snake["direction"] != "UP":
        snake["direction"] = "DOWN"

    # Mover a cobra
    move_snake()

    # Delimitar paredes do mapa
    if snake["head"]["position"][0] <= 0 or snake["head"]["position"][0] >= 600:
        game_over.play()
        move = False

    if snake["head"]["position"][1] <= 0 or snake["head"]["position"][1] >= 585:
        game_over.play()
        move = False

    # Desenhar a tela
    screen.fill(black)

    # Desenhar a cabeça da cobra
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

    # Desenhar o corpo da cobra
    for segment in snake["body"]:
        pygame.draw.rect(
            screen,
            green,
            (
                segment["position"][0],
                segment["position"][1],
                snake["size"][0],
                snake["size"][1],
            ),
        )

    # Desenhar a maçã
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

    # Maçã de ouro
    pygame.draw.rect(
        screen,
        (255, 255, 0),
        (
            golden_apple["position"][0],
            golden_apple["position"][1],
            golden_apple["size"][0],
            golden_apple["size"][1],
        ),
    )

    # Atualizar a tela
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Controlar FPS (frames por segundo)
