import pygame
import random
import math
from pygame import mixer
# def main1():
# Making screen
pygame.init()
screen = pygame.display.set_mode((800, 600))  # x,y

# Changing caption and image
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)
# play music
mixer.music.load('background.wav')
mixer.music.play(-1)

# Background
back = pygame.image.load('background.png')

# Add player
player = pygame.image.load('player.png')
pos_x = 370
pos_y = 460
pos_change = 0
# Add enemy
enemy = []
enemy_x = []
enemy_y = []
enemy_change = []
n_of_e = 5
for i in range(n_of_e):
    enemy.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0, 750))
    enemy_y.append(random.randint(0, 150))
    enemy_change.append(11)
# bullets
# Fire can see
# Ready cannot sea
bullet = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bullet_change = 11
bullet_state = "ready"
# Score
score = 0
font = pygame.font.Font("Hokjesgeest-PDGB.ttf", 50)


# Methods
def show(x, y):
    font1 = font.render("Score :" + str(score), True, (255, 255, 200))
    screen.blit(font1, (x, y))


def player_m(x, y):
    screen.blit(player, (x, y))


def enemy_m(x, y, i):
    screen.blit(enemy[i], (x, y))


def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 20))


def oncollision(enemy_x, enemy_y, bulletx, bullet_y):
    pow1 = pow(enemy_x - bulletx, 2)
    pow2 = pow(enemy_y - bullet_y, 2)
    distance = math.sqrt(pow1 + pow2)
    if distance < 26:
        return True


def gameover():
    font2 = pygame.font.Font("Hokjesgeest-PDGB.ttf", 85)
    over = font2.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over, (0, 250))


# Infinite Loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(back, (0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    # Checking input

    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_LEFT:
            pos_x += -11
        if e.key == pygame.K_RIGHT:
            pos_x += 11
        if bullet_state == "ready":
            if e.key == pygame.K_SPACE:
                laser = mixer.Sound('laser.wav').play()
                bullet_x = pos_x
                fire(bullet_x, bullet_y)

    if bullet_y < 0:
        bullet_state = "ready"
        bullet_y = 480
    if bullet_state == "fire":
        fire(bullet_x, bullet_y)
        bullet_y -= 30

    if e.type == pygame.KEYUP:
        if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
            pos_x += 0
    for i in range(n_of_e):
        if enemy_y[i] > 460:
            for j in range(n_of_e):
                enemy_y[j] = 2000
                gameover()
                mixer.music.stop()
                mixer.Sound('over.wav').play()



        enemy_x[i] += enemy_change[i]
        # Moving enemy
        if enemy_x[i] > 750:
            enemy_change[i] *= -1
            enemy_y[i] += 60
        if enemy_x[i] <= 4:
            enemy_change[i] *= -1
            enemy_y[i] += 60
        if oncollision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            explosion = mixer.Sound('explosion.wav').play()
            bullet_y = 480
            bullet_state = "ready"
            enemy_x[i] = random.randint(0, 750)
            enemy_y[i] = random.randint(0, 150)
            score += 1
        enemy_m(enemy_x[i], enemy_y[i], i)
    # Checking collision

    # Boundry checking

    if pos_x > 740:
        pos_x = 740
    if pos_x < 0:
        pos_x = 0

    # Applying players

    player_m(pos_x, pos_y)
    show(10, 10)
        pygame.display.update()
# main1()