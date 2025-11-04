# game_objects.py
# === 游戏对象定义 ===
# === Определение игровых объектов ===

import pygame
import random
from config import *

class Snake:
    """蛇类 / Класс змейки"""
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = "RIGHT"

    def move(self):
        """移动蛇 / Движение змейки"""
        x, y = self.body[0]
        if self.direction == "UP":
            y -= CELL_SIZE
        elif self.direction == "DOWN":
            y += CELL_SIZE
        elif self.direction == "LEFT":
            x -= CELL_SIZE
        elif self.direction == "RIGHT":
            x += CELL_SIZE
        new_head = (x, y)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        """蛇增长 / Увеличение длины змейки"""
        tail = self.body[-1]
        self.body.append(tail)

    def draw(self, surface):
        """绘制蛇 / Отрисовка змейки"""
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))


class Apple:
    """苹果类 / Класс яблока"""
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        """随机生成新位置 / Генерация случайной позиции"""
        x = random.randint(0, (WINDOW_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (WINDOW_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        return (x, y)

    def draw(self, surface):
        """绘制苹果 / Отрисовка яблока"""
        pygame.draw.rect(surface, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))
