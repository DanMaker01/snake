import pygame
import random

# Configurações do jogo
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Função para desenhar a grade
def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (40, 40, 40), rect, 1)

# Função para desenhar a cobra
def draw_snake(snake):
    for segment in snake:
        rect = pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (0, 255, 0), rect)

# Função para desenhar a comida
def draw_food(food):
    rect = pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, (255, 0, 0), rect)

# Função para desenhar a pontuação
def draw_score(score):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def morrer():
    print("fim de jogo, aperte s para continuar")
    a = input()
    if a == "s":
        main()
    else:
        pygame.quit()
# Função principal do jogo
def main():
    running = True
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = pygame.K_RIGHT
    food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                morrer()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    direction = event.key

        # Movimentação da cobra
        head_x, head_y = snake[0]
        if direction == pygame.K_UP:
            head_y -= CELL_SIZE
        elif direction == pygame.K_DOWN:
            head_y += CELL_SIZE
        elif direction == pygame.K_LEFT:
            head_x -= CELL_SIZE
        elif direction == pygame.K_RIGHT:
            head_x += CELL_SIZE

        # Verificação de colisão com as bordas
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            running = False

        # Verificação de colisão com o próprio corpo
        if (head_x, head_y) in snake:
            running = False

        # Verificação de colisão com a comida
        if (head_x, head_y) == food:
            food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                    random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
            score += 1
        else:
            snake.pop()

        # Atualização da posição da cabeça da cobra
        snake.insert(0, (head_x, head_y))

        # Desenho dos elementos do jogo
        screen.fill((0, 0, 0))
        draw_grid()
        draw_snake(snake)
        draw_food(food)
        draw_score(score)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
