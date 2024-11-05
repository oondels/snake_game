import pygame
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

menu = True


def run_game():
    global move
    move = True
    running = True
    # Inicializar o Pygame
    pygame.init()
    pygame.mixer.init()

    # Sons
    eat_tadala = pygame.mixer.Sound("./utils/sounds/apple_bite.mp3")
    # eat_comida_surpresa = pygame.mixer.Sound("./utils/sounds/val_sound.mp3")
    game_over = pygame.mixer.Sound("./utils/sounds/game_over.mp3")

    # Definir as configurações da tela
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()
    ultima_chamada = pygame.time.get_ticks()

    # Definir cores
    global color
    black = (0, 0, 0)
    color = (0, 255, 0)

    snake_element_size = [15, 15]

    # Inicializar a cobra
    snake = {
        "speed": 0.8,
        "size": snake_element_size,
        "head": {"position": [50, 50]},
        "body": [{"position": [34, 50]}, {"position": [18, 50]}],
        "direction": "RIGHT",
    }

    tadala = {"position": [100, 100], "size": [23, 23]}
    tadalinha_image = pygame.image.load("./utils/imgs/tadalinha.png")
    tadalinha_image = pygame.transform.scale(tadalinha_image, (30, 30))

    show_golden_apple_index = False
    caixa_tadala_image = pygame.image.load("./utils/imgs/tadala.png")
    caixa_tadala_image = pygame.transform.scale(caixa_tadala_image, (35, 35))
    caixa_tadala = {"position": [-50, -50], "size": [23, 30]}

    comida_surpresa_image = pygame.image.load("./utils/imgs/comida_surpresa.png")
    comida_surpresa_image = pygame.transform.scale(comida_surpresa_image, (55, 55))
    comida_surpresa = {
        "comidas": [
            {"position": [-100, -100]},
            {"position": [-100, -100]},
            {"position": [-100, -100]},
        ],
        "size": [30, 40],
    }

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
        caixa_tadala["position"] = random.sample(range(580), k=2)

    def random_golden_apple():
        caixa_tadala["position"] = [-50, -50]
        for _ in range(10):
            snake["body"].append({"position": [-16, -16]})
        snake["speed"] += 0.06
        print(f"Velociade = {snake["speed"]}")

    def random_comida_surpresa(part):
        part["position"] = [-50, -50]
        for _ in range(60):
            snake["body"].append({"position": [-16, -16]})
        snake["speed"] += 0.1

    def random_apple():
        tadala["position"] = random.sample(range(580), k=2)
        for _ in range(2):
            snake["body"].append({"position": [-16, -16]})
        snake["speed"] += 0.03

        print(f"Velociade = {snake["speed"]}")

    def check_cheat():
        global typed_cheat
        if typed_cheat == cheat_code_2:
            global color
            color = (255, 0, 0)
            for _ in range(100):
                snake["body"].append({"position": [-16, -16]})
            snake["speed"] += 0.5
            typed_cheat = ""

        if typed_cheat == cheat_code_1:
            for food in comida_surpresa["comidas"]:
                food["position"] = random.sample(range(580), k=2)
            typed_cheat = ""

    cheat_code_2 = "hendrius"
    cheat_code_1 = "adevaldo"
    global typed_cheat
    typed_cheat = ""
    key_map = {
        pygame.K_h: "h",
        pygame.K_e: "e",
        pygame.K_n: "n",
        pygame.K_d: "d",
        pygame.K_r: "r",
        pygame.K_i: "i",
        pygame.K_u: "u",
        pygame.K_s: "s",
        pygame.K_a: "a",
        pygame.K_v: "v",
        pygame.K_l: "l",
        pygame.K_o: "o",
    }

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key in key_map:
                    typed_cheat += key_map[event.key]
                    check_cheat()

        agora = pygame.time.get_ticks()
        if agora - ultima_chamada >= 5000 and show_golden_apple_index == True:
            show_golden_apple()
            show_golden_apple_index = False
            ultima_chamada = agora

        # Capturar Tadala
        if pygame.Rect(
            snake["head"]["position"][0],
            snake["head"]["position"][1],
            snake["size"][0],
            snake["size"][1],
        ).colliderect(
            pygame.Rect(
                tadala["position"][0],
                tadala["position"][1],
                tadala["size"][0],
                tadala["size"][1],
            )
        ):
            eat_tadala.play()
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
                caixa_tadala["position"][0],
                caixa_tadala["position"][1],
                caixa_tadala["size"][0],
                caixa_tadala["size"][1],
            )
        ):
            eat_tadala.play()
            random_golden_apple()

        # Capturar comida surpresa
        for food in comida_surpresa["comidas"]:
            if pygame.Rect(
                snake["head"]["position"][0],
                snake["head"]["position"][1],
                snake["size"][0],
                snake["size"][1],
            ).colliderect(
                pygame.Rect(
                    food["position"][0],
                    food["position"][1],
                    comida_surpresa["size"][0],
                    comida_surpresa["size"][1],
                )
            ):
                # eat_comida_surpresa.play()
                random_comida_surpresa(food)

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
            color,
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
                color,
                (
                    segment["position"][0],
                    segment["position"][1],
                    snake["size"][0],
                    snake["size"][1],
                ),
            )

        # Tadala comprimido
        screen.blit(
            tadalinha_image,
            (
                tadala["position"][0],
                tadala["position"][1],
            ),
        )

        # Caixa Tadala
        screen.blit(
            caixa_tadala_image,
            (
                caixa_tadala["position"][0],
                caixa_tadala["position"][1],
            ),
        )

        # Comida Surpresa
        for food in comida_surpresa["comidas"]:
            screen.blit(
                comida_surpresa_image,
                (
                    food["position"][0],
                    food["position"][1],
                ),
            )

        # Atualizar a tela
        pygame.display.flip()
        pygame.time.Clock().tick(60)  # Controlar FPS (frames por segundo)

    pygame.display.quit()


def pause():
    global move
    move = not move


def interface_menu():
    # Inicializar o QApplication
    app = QApplication(sys.argv)

    # Cria a janela principal
    window = QWidget()
    window.setWindowTitle("Tadala Game")
    window.setGeometry(100, 100, 300, 400)

    # Cria um layout vertical
    layout = QVBoxLayout()

    # Cria um título para o menu
    titulo = QLabel("Bem-vindo ao ######!")
    titulo.setAlignment(Qt.AlignCenter)
    titulo.setStyleSheet("font-size: 24px; font-weight: bold;")

    # Adiciona descrição
    description = QLabel("Desenvolvido por Hendrius Félix")
    description.setAlignment(Qt.AlignCenter)
    description.setStyleSheet("font-size: 12px;")

    # Adiciona título e descrição ao layout
    layout.addWidget(titulo)
    layout.addWidget(description)

    # Cria os botões do menu
    botao_novo_jogo = QPushButton("Novo Jogo")
    botao_novo_jogo.clicked.connect(run_game)

    botao_pause = QPushButton("Pause")
    botao_pause.clicked.connect(pause)

    # Adiciona os botões ao layout
    layout.addWidget(botao_novo_jogo)
    layout.addWidget(botao_pause)

    # Define o layout na janela
    window.setLayout(layout)

    # Exibe a janela
    window.show()

    # Executa o loop da aplicação
    sys.exit(app.exec_())


if __name__ == "__main__":
    interface_menu()
