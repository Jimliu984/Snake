import pygame
import random
import numpy as np
import sys
# Go back in terminal: cd /
# Then: cd Users/jimliu/Documents/Python/Games
# python3 Snake_Better.py
print("Running")
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Snake')
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT+20))
screen.fill((0, 0, 0))
Colour_Green = (0,250,0)
Colour_Red = (250,0,0)
Dim = 20
Direction = 0
Snake_Position = [int(WIDTH/2),int(HEIGHT/2)]
Snake_Positions = [Snake_Position]
Food_Position = [random.randrange(0, WIDTH - Dim, Dim), random.randrange(0, HEIGHT - Dim, Dim)]
pygame.draw.rect(screen, Colour_Green,(Snake_Position[0], Snake_Position[1], Dim, Dim))
pygame.draw.rect(screen, Colour_Red, (Food_Position[0], Food_Position[1], Dim, Dim))
pygame.draw.rect(screen, (50, 50, 50), (0, HEIGHT, WIDTH, 20))
Score = 0
pygame.font.init()
Words = "Score:" + str(Score)
default_font = pygame.font.get_default_font()
font_renderer = pygame.font.Font(default_font, 20)
label = font_renderer.render(Words, 1, (255, 255, 255))
screen.blit(label, (0, HEIGHT))
def Detect_Collision(Snake_Position, Food_Position):
	S_x = Snake_Position[0]
	S_y = Snake_Position[1]
	F_x = Food_Position[0]
	F_y = Food_Position[1]
	if S_x == F_x and S_y == F_y:
		return True
	return False

def Collision_Check(Food_Position):
	if Detect_Collision(Snake_Position, Food_Position):
		return True
	return False

def Self_Eat(Snake_Positions):
    dup = []
    for x in Snake_Positions:
        if x not in dup:
            dup.append(x)
    if np.shape(dup)[0] != np.shape(Snake_Positions)[0]:
        return True

def Snake_Move(Snake_Position,Direction):
    x = Snake_Position[0]
    y = Snake_Position[1]
    if Direction == 3:
        x -= Dim
        x = x % WIDTH
    elif Direction ==1:
        x += Dim
        x = x % WIDTH
    elif Direction == 0:
        y -= Dim
        y = y % HEIGHT
    elif Direction == 2:
        y += Dim
        y = y % HEIGHT
    return [int(x),int(y)]
game_over = False
while not game_over:
    Snake_Position = Snake_Move(Snake_Position, Direction)
    Snake_Positions.append(Snake_Position)
    pygame.draw.rect(screen, Colour_Green, (Snake_Position[0], Snake_Position[1], Dim, Dim))
    pygame.draw.rect(screen, (0, 0, 0), (Snake_Positions[0][0], Snake_Positions[0][1], Dim, Dim))
    Snake1 = Snake_Positions[0].copy()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Direction = 3
            elif event.key == pygame.K_RIGHT:
                Direction = 1
            elif event.key == pygame.K_UP:
                Direction = 0
            elif event.key == pygame.K_DOWN:
                Direction = 2
    if Collision_Check(Food_Position):
        Food_Position = [random.randrange(0, WIDTH - Dim, Dim), random.randrange(0, HEIGHT - Dim, Dim)]
        while Food_Position in Snake_Positions:
            Food_Position = [random.randrange(0, WIDTH - Dim, Dim), random.randrange(0, HEIGHT - Dim, Dim)]
        pygame.draw.rect(screen, Colour_Green, (Snake_Position[0], Snake_Position[1], Dim, Dim))
        Snake_Positions.insert(0, [Snake1[0], Snake1[1]])
        pygame.draw.rect(screen, Colour_Red,
                         (Food_Position[0],Food_Position[1], Dim, Dim))
        pygame.font.init()
        pygame.draw.rect(screen, (50, 50, 50), (0, HEIGHT, WIDTH, 20))
        Score +=1
        Words = "Score:" + str(Score)
        default_font = pygame.font.get_default_font()
        font_renderer = pygame.font.Font(default_font, 20)
        label = font_renderer.render(Words, 1, (255, 255, 255))
        screen.blit(label, (0, HEIGHT))
    elif Self_Eat(Snake_Positions):
        pygame.font.init()
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
        default_font = pygame.font.get_default_font()
        font_renderer = pygame.font.Font(default_font, int(WIDTH/10))
        label = font_renderer.render("Whoops, You Lose!", 1, (255, 255, 255))
        label1 = font_renderer.render("Score: " + str(Score), 1, (255, 255, 255))
        screen.blit(label, (0, int(HEIGHT/2)))
        screen.blit(label1, (0, int(HEIGHT/2)+60))
        Direction = 4
    else:
        pygame.draw.rect(screen, Colour_Green, (Snake_Position[0], Snake_Position[1], Dim, Dim))
        pygame.draw.rect(screen, (0, 0, 0), (Snake_Positions[0][0], Snake_Positions[0][1], Dim, Dim))
    Snake_Positions.pop(0)
    clock.tick(10)
    pygame.display.update()