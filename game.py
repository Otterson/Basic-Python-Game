import pygame
import os
import sys
import random


pygame.init()

screen_width = 1200
screen_height = 900
player_x_pos = 400
player_y_pos = 800
enemy_x_pos = 400
enemy_y_pos = 200
enemy_x_pos = random.randint(0,screen_width-50)

screen_size = (screen_width, screen_height)
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_pos -= 40
            elif event.key == pygame.K_RIGHT:
                player_x_pos += 40
            elif event.key == pygame.K_UP:
                player_y_pos -= 40
            elif event.key == pygame.K_DOWN:
                player_y_pos += 40

    screen.fill(BLACK)

    if enemy_y_pos > 0 and enemy_y_pos < screen_height:
        enemy_y_pos += 20
    else:
        enemy_x_pos = random.randint(0,screen_width - 50)
        enemy_y_pos = 1

    pygame.draw.rect(screen, RED, (enemy_x_pos,enemy_y_pos,50,50))
    pygame.draw.rect(screen, BLUE, (player_x_pos,player_y_pos,50,50))

    clock.tick(20)
    pygame.display.update()
