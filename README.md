# Snake Game

Este projeto é um jogo de cobra clássico desenvolvido em Python utilizando a biblioteca Pygame. Siga as instruções abaixo para configurar o ambiente e rodar o jogo.

## Requisitos

- Python 3.6+
- Pygame

## Instalação

### Windows

1. **Clone o repositório**

   ```sh
   git clone https://github.com/oondels/snake_game.git
   cd snake_game
   ```

2. **Crie um ambiente virtual**

   - Windows

   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências**

   ```sh
   pip install -r requirements.txt
   ```

4. **Execute o jogo**
   ```sh
   python snake_game.py
   ```

### Linux

1. **Clone o repositório**

   ```sh
   git clone https://github.com/oondels/snake_game.git
   cd snake_game
   ```

2. **Crie um ambiente virtual**

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências**

   ```sh
   pip install -r requirements.txt
   ```

4. **Execute o jogo**
   ```sh
   python3 snake_game.py
   ```

## Controles do Jogo

- **Seta para cima**: Move a cobra para cima
- **Seta para baixo**: Move a cobra para baixo
- **Seta para esquerda**: Move a cobra para a esquerda
- **Seta para direita**: Move a cobra para a direita

## Objetivo

O objetivo do jogo é coletar as maçãs espalhadas pelo mapa para aumentar o tamanho da cobra. Evite colidir com as paredes ou com o próprio corpo!

## Sons

O jogo possui sons de notificação quando a cobra come uma maçã ou colide. Certifique-se de ter um alto-falante ligado para uma melhor experiência.

## Problemas Comuns

- Caso encontre erros de dependência, certifique-se de ter instalado o Pygame corretamente.
- Caso a velocidade da cobra esteja muito alta, ajuste a configuração do FPS (frames por segundo) no código para um valor menor.
