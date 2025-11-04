"""
game_objects.py
Классы игровых объектов: GameObject, Snake, Apple.
"""

import random
import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE, GREEN, RED


class GameObject:
    """Базовый класс для игровых объектов."""

    def __init__(self, position, body_color):
        """
        Инициализация объекта.
        :param position: (x, y) координаты верхнего левого угла
        :param body_color: цвет объекта
        """
        self.position = position
        self.body_color = body_color

    def draw(self, surface):
        """Отрисовка объекта на поверхности. Переопределяется в дочерних классах."""
        pass


class Apple(GameObject):
    """Класс яблока."""

    def __init__(self):
        """Создание яблока с случайной позицией."""
        super().__init__((0, 0), RED)
        self.randomize_position()

    def randomize_position(self):
        """Задаёт случайное положение яблока на игровом поле."""
        max_x = WINDOW_WIDTH // CELL_SIZE - 1
        max_y = WINDOW_HEIGHT // CELL_SIZE - 1
        self.position = (random.randint(0, max_x) * CELL_SIZE,
                         random.randint(0, max_y) * CELL_SIZE)

    def draw(self, surface):
        """Отрисовка яблока."""
        pygame.draw.rect(surface, self.body_color,
                         (*self.position, CELL_SIZE, CELL_SIZE))


class Snake(GameObject):
    """Класс змейки."""

    def __init__(self):
        """Создание змейки с начальной длиной 1."""
        start_pos = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        super().__init__(start_pos, GREEN)
        self.length = 1
        self.positions = [start_pos]
        self.direction = (CELL_SIZE, 0)  # движение вправо
        self.next_direction = None

    def update_direction(self):
        """Обновление направления движения."""
        if self.next_direction:
            dx, dy = self.next_direction
            # Запрещаем движение назад
            if (dx, dy) != (-self.direction[0], -self.direction[1]):
                self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Движение змейки: добавление головы и удаление хвоста."""
        head_x, head_y = self.positions[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % WINDOW_WIDTH,
                    (head_y + dy) % WINDOW_HEIGHT)

        # Проверка столкновения с самим собой
        if new_head in self.positions:
            self.reset()
            return

        self.positions.insert(0, new_head)

        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self, surface):
        """Отрисовка змейки."""
        for pos in self.positions:
            pygame.draw.rect(surface, self.body_color,
                             (*pos, CELL_SIZE, CELL_SIZE))

    def get_head_position(self):
        """Возвращает координаты головы змейки."""
        return self.positions[0]

    def reset(self):
        """Сброс змейки при столкновении с собой."""
        start_pos = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.length = 1
        self.positions = [start_pos]
        self.direction = (CELL_SIZE, 0)
        self.next_direction = None
