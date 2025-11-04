# main.py
# === 贪吃蛇主程序 / Основной файл игры "Змейка" ===

import pygame
import sys
from config import *
from game_objects import Snake, Apple

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Змейка / 贪吃蛇")
clock = pygame.time.Clock()

snake = Snake()
apple = Apple()

def check_collision(pos1, pos2):
    """检测碰撞 / Проверка столкновений"""
    return pos1[0] == pos2[0] and pos1[1] == pos2[1]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"

    snake.move()

    # 吃到苹果 / Если съела яблоко
    if check_collision(snake.body[0], apple.position):
        snake.grow()
        apple = Apple()

    # 撞到自己或墙壁 / Столкновение со стенами или с собой
    head_x, head_y = snake.body[0]
    if (head_x < 0 or head_x >= WINDOW_WIDTH or
        head_y < 0 or head_y >= WINDOW_HEIGHT or
        len(snake.body) != len(set(snake.body))):
        pygame.quit()
        sys.exit()

    screen.fill(BLACK)
    snake.draw(screen)
    apple.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
