import pygame
from pygame.math import Vector2
import sys
import random

ROWS = 36
COLUMS = 36
PIXELS = 20

WINDOW_WIDTH = COLUMS * PIXELS
WINDOW_HEIGHT = ROWS * PIXELS

COLOR_OPTIONS = ['White', 'Green', 'Red', 'Blue']

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

frog_image = pygame.image.load('frog.png').convert_alpha()
mouse_image = pygame.image.load('mouse.png').convert_alpha()
insect_image = pygame.image.load('insect.png').convert_alpha()
food_choices = [frog_image, mouse_image, insect_image]


class Snake:
    global COLOR_OPTIONS

    def __init__(self, head="Green", body="Red"):
        self.headColor = head
        self.bodyColor = body
        self.Body = [Vector2(7, 11), Vector2(5, 11), Vector2(6, 11)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for parts in self.Body:
            x_pos = int(parts.x * PIXELS)
            y_pos = int(parts.y * PIXELS)
            snake_rect = pygame.Rect(x_pos, y_pos , PIXELS, PIXELS)
            pygame.draw.rect(screen, (125, 255, 120), snake_rect)

    def move_snake(self):
        body_copy = self.Body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.Body = body_copy

    def add_body(self):
        self.Body.append(self.Body[-1])

    # @property
    # def headColor(self):
    #     return self._headColor

    # @headColor.setter
    # def head(self, head):
    #     if head not in COLOR_OPTIONS:
    #         print("Invalid color for snake head")
    #         sys.exit(1)
    #     self._headColor = head

    # @property
    # def bodyColor(self):
    #     return self._bodyColor
    
    # @bodyColor.setter
    # def body(self, body):
    #     if body not in COLOR_OPTIONS:
    #         print("Invalid color for snake body")
    #         sys.exit(1)
    #     self._bodyColor = body

class Food:
    global food_choices
    def __init__(self):
        self.x = random.randint(0, COLUMS - 1)
        self.y = random.randint(0, ROWS - 1)
        self.pos = Vector2(self.x, self.y)
        self.food = random.choice(food_choices)

    def draw_food(self):
        food_rect = pygame.Rect(int(self.pos.x * PIXELS), int(self.pos.y * PIXELS), PIXELS, PIXELS)
        screen.blit(self.food, food_rect)
        # pygame.draw.rect(screen, (126, 166, 114), food_rect)

class Main:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.come_out_of_wall()
        
    def draw_elements(self):
        self.snake.draw_snake()
        self.food.draw_food()

    def check_collision(self):
        if self.food.pos == self.snake.Body[0]:
            self.food = Food()
            self.snake.add_body()

    def check_fail(self):
        for body in self.snake.Body[1:]:
            if body == self.snake.Body[0]:
                self.game_over()

    def come_out_of_wall(self):
        if self.snake.Body[0].x >= COLUMS:
            self.snake.Body[0].x = 0
        if self.snake.Body[0].x < 0:
            self.snake.Body[0].x = COLUMS - 1
        if self.snake.Body[0].y >= ROWS:
            self.snake.Body[0].y = 0
        if self.snake.Body[0].y < 0:
            self.snake.Body[0].y = ROWS - 1

    def game_over(self):
        pygame.quit()
        sys.exit(1)

food = Food()
snake = Snake()



# Screen Update
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)

main_game = Main()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(1)
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1, 0)
        



    screen.fill((255, 0, 0))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)