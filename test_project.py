import pytest
import pygame
from pygame.math import Vector2
from project import Snake, Food, Main, ROWS, COLUMS, PIXELS

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((COLUMS * PIXELS, ROWS * PIXELS))

def test_snake_initialization():
    snake = Snake()
    assert len(snake.Body) == 3
    assert snake.direction == Vector2(1, 0)
    assert snake.Body[0] == Vector2(7, 11)
    assert snake.Body[1] == Vector2(5, 11)
    assert snake.Body[2] == Vector2(6, 11)

def test_food_initialization():
    snake = Snake()
    food = Food(snake.Body)
    assert food.pos not in snake.Body

def test_move_snake():
    snake = Snake()
    initial_head_position = snake.Body[0]
    snake.move_snake()
    new_head_position = snake.Body[0]
    assert new_head_position == initial_head_position + snake.direction
    assert len(snake.Body) == 3 

def test_check_collision():
    main_game = Main()
    initial_length = len(main_game.snake.Body)
    main_game.food.pos = main_game.snake.Body[0]  
    main_game.check_collision()
    assert len(main_game.snake.Body) == initial_length + 1  
    assert main_game.food.pos != main_game.snake.Body[0]  