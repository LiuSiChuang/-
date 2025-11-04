import random
import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE, GRID_WIDTH, GRID_HEIGHT, GREEN, RED


class GameObject:
    """Базовый класс игрового объекта."""

    def __init__(self, position, body_color):
        """Инициализация объекта с позицией и цветом."""
        self.position = position
        self.body_color = body_color

    def draw(self, surface):
        """Метод отрисовки объекта. Переопределяется в наследниках."""
        pass


class Apple(GameObject):
    """Класс яблока."""

    def __init__(self):
        super().__init__((0, 0), RED)
        self.randomize_position()

    def randomize_position(self):
        """Случайное размещение яблока."""
        x = random.randint(0, GRID_WIDTH - 1) * CELL_SIZE
        y = random.randint(0, GRID_HEIGHT - 1) * CELL_SIZE
        self.position = (x, y)

    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, self.body_color, rect)


class Snake(GameObject):
    """Класс змейки."""

    def __init__(self):
        start_x = WINDOW_WIDTH // 2 // CELL_SIZE * CELL_SIZE
        start_y = WINDOW_HEIGHT // 2 // CELL_SIZE * CELL_SIZE
        super().__init__((start_x, start_y), GREEN)
        self.length = 1
        self.positions = [self.position]
        self.direction = (CELL_SIZE, 0)
        self.next_direction = None

    def get_head_position(self):
        return self.positions[0]

    def update_direction(self):
        if self.next_direction:
            dx, dy = self.direction
            ndx, ndy = self.next_direction
            if (dx + ndx, dy + ndy) != (0, 0):
                self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        cur_x, cur_y = self.get_head_position()
        dx, dy = self.direction
        new_head = ((cur_x + dx) % WINDOW_WIDTH, (cur_y + dy) % WINDOW_HEIGHT)

        if new_head in self.positions:
            self.reset()
            return

        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()
        self.position = new_head

    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, self.body_color, rect)

    def reset(self):
        start_x = WINDOW_WIDTH // 2 // CELL_SIZE * CELL_SIZE
        start_y = WINDOW_HEIGHT // 2 // CELL_SIZE * CELL_SIZE
        self.length = 1
        self.positions = [(start_x, start_y)]
        self.direction = (CELL_SIZE, 0)
        self.next_direction = None
