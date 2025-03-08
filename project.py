"""
Hello! This file contains the code to our attempt at the final project of CS50P.
The creators of this project are me(Eishal Keshwani) and a CS50P classmate and friend
Omer Rauf Khan. 
"""

import sys
import pygame
from pygame.math import Vector2
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

username = str()
difficulty = str()
difficulty_levels = {"Easy": 150, "Medium": 125, "Hard": 70}
open_window_flag = True

# cap = cv2.VideoCapture("bg_video.mp4")

ROWS = 20
COLUMS = 20
PIXELS = 40

WINDOW_WIDTH = COLUMS * PIXELS
WINDOW_HEIGHT = ROWS * PIXELS

COLOR_OPTIONS = ['White', 'Green', 'Red', 'Blue']

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# load background image
background_image = pygame.image.load("bg_image.jpg")
clock = pygame.time.Clock()
font = pygame.font.Font("font/GallaeciaForte.ttf", 30)
name_font = pygame.font.Font("font/GallaeciaForte.ttf", 15)
game_over_font = pygame.font.Font("font/GallaeciaForte.ttf", 50)

frog_image = pygame.image.load('frog.png').convert_alpha()
mouse_image = pygame.image.load('mouse.png').convert_alpha()
insect_image = pygame.image.load('insect.png').convert_alpha()
bird_image = pygame.image.load('bird.png').convert_alpha()
food_choices = [frog_image, mouse_image, insect_image, bird_image]



class Snake: # Donot Touch
    global COLOR_OPTIONS

    def __init__(self):
        self.Body = [Vector2(7, 11), Vector2(5, 11), Vector2(6, 11)]
        self.direction = Vector2(1, 0)
        
        self.head = pygame.image.load('snake/head_right.png').convert_alpha()
        self.tail = pygame.image.load('snake/tail_left.png').convert_alpha()

        self.head_up = pygame.image.load('snake/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('snake/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('snake/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('snake/head_left.png').convert_alpha()
        
        self.tail_up = pygame.image.load('snake/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('snake/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('snake/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('snake/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('snake/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('snake/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('snake/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('snake/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('snake/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('snake/body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('crunch.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, parts in enumerate(self.Body):
            x_pos = int(parts.x * PIXELS)
            y_pos = int(parts.y * PIXELS)
            snake_rect = pygame.Rect(x_pos, y_pos , PIXELS, PIXELS)
            
            if index == 0:
                screen.blit(self.head, snake_rect)
            elif index == len(self.Body) - 1:
                screen.blit(self.tail, snake_rect)
            else:
                previous_part = self.Body[index + 1] - parts
                next_part = self.Body[index - 1] - parts
                if previous_part.x == next_part.x:
                    screen.blit(self.body_vertical, snake_rect)
                elif previous_part.y == next_part.y:
                    screen.blit(self.body_horizontal, snake_rect)
                else:
                    if previous_part.x == -1 and next_part.y == -1 or previous_part.y == -1 and next_part.x == -1:
                        screen.blit(self.body_tl, snake_rect)
                    elif previous_part.x == -1 and next_part.y == 1 or previous_part.y == 1 and next_part.x == -1:
                        screen.blit(self.body_bl, snake_rect)
                    elif previous_part.x == 1 and next_part.y == -1 or previous_part.y == -1 and next_part.x == 1:
                        screen.blit(self.body_tr, snake_rect)
                    elif previous_part.x == 1 and next_part.y == 1 or previous_part.y == 1 and next_part.x == 1:
                        screen.blit(self.body_br, snake_rect)
            

    def update_head_graphics(self):
        head_direction = self.Body[1] - self.Body[0]
        if head_direction == Vector2(1, 0):
            self.head = self.head_left
        elif head_direction == Vector2(-1, 0):
            self.head = self.head_right
        elif head_direction == Vector2(0, 1):
            self.head = self.head_up
        elif head_direction == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_direction = self.Body[-2] - self.Body[-1]
        if tail_direction == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_direction == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_direction == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_direction == Vector2(0, -1):
            self.tail = self.tail_down

    
        ... 

    def move_snake(self):
        body_copy = self.Body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.Body = body_copy

    def add_body(self):
        self.Body.append(self.Body[-1])

class Food: # Donot Touch
    global food_choices
    def __init__(self, snake_body):
        self.x = random.randint(0, COLUMS - 1)
        self.y = random.randint(0, ROWS - 1)
        self.pos = Vector2(self.x, self.y)
        self.food = random.choice(food_choices)
        self.snake_body = snake_body

    def randomize_position(self):
        while True:
            self.x = random.randint(0, COLUMS - 1)
            self.y = random.randint(0, ROWS - 1)
            self.pos = Vector2(self.x, self.y)
            if self.pos not in self.snake_body:
                break

    def draw_food(self):
        food_rect = pygame.Rect(int(self.pos.x * PIXELS), int(self.pos.y * PIXELS), PIXELS, PIXELS)
        screen.blit(self.food, food_rect)
        # pygame.draw.rect(screen, (126, 166, 114), food_rect)
        
class Main: # Donot Touch
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.Body)
        self.game_over_flag = False
        self.game_music = pygame.mixer.Sound('game music.mp3')
        self.game_over_music = pygame.mixer.Sound('game over music.wav')
        self.game_music.play(loops=-1).set_volume(0.5)
    
    def update(self):
        if not self.game_over_flag:
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()
            self.come_out_of_wall()
        
    def draw_elements(self):
        if not self.game_over_flag:
            self.snake.draw_snake()
            self.food.draw_food()
            self.score()
            self.display_username()
        else:
            self.display_game_over()

    def check_collision(self):
        if self.food.pos == self.snake.Body[0]:
            self.snake.crunch_sound.play()
            self.food = Food(self.snake.Body)
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

    def display_username(self):
        name = username
        name_text = name_font.render(name, True, (255, 255, 255))
        name_x = int(self.snake.Body[0].x * PIXELS + PIXELS / 2)
        if self.snake.Body[0].y != 0:
            name_y = int((self.snake.Body[0].y - 1) * PIXELS + PIXELS / 2)
        else:
            name_y = int((self.snake.Body[0].y + 1) * PIXELS + PIXELS / 2)
        name_rect = name_text.get_rect(center=(name_x, name_y))
        screen.blit(name_text, name_rect)
    
    def score(self):
        score = str(len(self.snake.Body) - 3)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        score_x = int(WINDOW_WIDTH - 100)
        score_y = int(WINDOW_HEIGHT - 50)
        score_rect = score_text.get_rect(center=(score_x, score_y))
        screen.blit(score_text, score_rect)

    def game_over(self):
        self.game_over_flag = True
    
    def display_game_over(self):
        self.game_over_music.play()
        game_over_screen_overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        game_over_screen_overlay.set_alpha(200)
        game_over_screen_overlay.fill((20, 20, 20, 0.5))
        screen.blit(game_over_screen_overlay, (0, 0))
        score = str(len(self.snake.Body) - 3)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
        pos_x = int(WINDOW_WIDTH / 2)
        pos_y = int(WINDOW_HEIGHT / 2)
        score_rect = score_text.get_rect(center=(pos_x, pos_y + 80))
        game_over_rect = game_over_text.get_rect(center=(pos_x, pos_y - 80))
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)



def main(): # Donot Touch --> Main Function
    openStartWindow()
    openGameWindow()

def openStartWindow():
    def data_retrieve():
        global username, difficulty, open_window_flag
        # retrieving data
        username = username_form.get()   
        difficulty = difficulty_dropdown.get()
        # Validation checks
        if username == "" and difficulty=="":
            messagebox.showwarning(title="Error",message="Please enter name and select level")
        elif difficulty == "":
            messagebox.showwarning(title="Error",message="Please select level")
        elif username == "":
            messagebox.showwarning(title="Error",message="Please enter name")
        else:
            window.destroy()
            open_window_flag = False


    #Creating a window
    window = tk.Tk()
    window.geometry("800x450")
    window.title("CS50P Final Project")
    window.config(bg="#1E1E1E")
    window.resizable(width=False,height=False)

    # Changing the logo of window
    # icon = ImageTk.PhotoImage(Image.open("favicon.png"))   
    # window.iconphoto(True,icon)


    # creating widgets 
    welcome_label = tk.Label(window,text="Welcome to snake game",bg="#1E1E1E",fg="#c20003",font=("Bevan",35))
    username_label = tk.Label(window,text="User Name",bg="#1E1E1E",fg="#0003c2",font=("fantasy",30))
    username_form = tk.Entry(window,font=(100))
    difficulty_label = tk.Label(window,text="Difficulty Level",bg="#1E1E1E",fg="#75038f",font=("fantasy",30))
    difficulty_dropdown = ttk.Combobox(window,values=["Easy","Medium","Hard"],font=(15))
    submit = tk.Button(window,text="START",command=data_retrieve,font=("Arial",50),fg="#000000",bg="#e8e800")


    # placing widgets
    welcome_label.place(x=200,y=30)
    username_label.place(x=10,y=130)
    username_form.place(x=230,y=138,height=35,width=250)
    difficulty_label.place(x=10,y=220)
    difficulty_dropdown.place(x=280,y=230,height=30,width=100)
    submit.place(width=800,height=100,y=350)
    window.mainloop()

def openGameWindow(): # Donot Touch
    global difficulty, difficulty_levels

    # Screen Update
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, difficulty_levels[difficulty])

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
            

        # Draw background image
        screen.blit(background_image, (0, 0))
                
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()




