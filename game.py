import pygame
import os
import sys
import random


pygame.init()

screen_width = 1200
screen_height = 900
player_x_pos = 400
player_y_pos = 800

player = [player_x_pos, player_y_pos]

block_size = 50

enemy_x_pos = random.randint(0,screen_width-block_size)
enemy_y_pos = 200

enemy_pos = [enemy_x_pos, enemy_y_pos]

enemy_list = [enemy_pos]

myFont = pygame.font.SysFont("monospace", 35)
enemy_block_speed = 20
screen_size = (screen_width, screen_height)
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)
YELLOW = (255, 255,0)

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
game_over = False
score = 0


def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) <15 and delay < 0.1:
        x_pos = random.randint(0, screen_width - block_size)
        y_pos = 1
        enemy_list.append([x_pos,y_pos])
    print(enemy_list)

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, RED, (enemy_pos[0],enemy_pos[1],block_size,block_size))

def update_enemy_positions(enemy_list, score):
    for index, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] > 0 and enemy_pos[1] < screen_height:
            enemy_pos[1] += enemy_block_speed
        else:
            enemy_list.pop(index)
            score +=1
    return score


def collision_check(enemy_list ,player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False


def detect_collision(player_position, enemy_position):
    p_x = player_position[0]
    p_y = player_position[1]

    e_x = enemy_position[0]
    e_y = enemy_position[1]

    if (e_x >= p_x and e_x < (p_x + block_size)) or (p_x >= e_x and p_x < (e_x+block_size)):
        if (e_y >= p_y and e_y < (p_y + block_size)) or (p_y >= e_y and p_y < (e_y+block_size)):
            return True
    return False


def set_level(score, speed):
    if score < 20:
        speed = 5
    elif score < 40:
        speed = 8
    elif score < 60:
        speed = 12
    else: speed = 15

    return speed


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
            player = [player_x_pos, player_y_pos]

    screen.fill(BLACK)

    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list,score)
    enemy_block_speed = set_level(score, enemy_block_speed)

    text = "Score:" + str(score)
    label = myFont.render(text, 1, YELLOW)
    screen.blit(label, (screen_width-200, screen_height-40))

    if collision_check(enemy_list, player):
        print("game over")
        game_over = True
        break

    draw_enemies(enemy_list)
    pygame.draw.rect(screen, BLUE, (player[0],player[1],block_size,block_size))

    clock.tick(20)
    pygame.display.update()
