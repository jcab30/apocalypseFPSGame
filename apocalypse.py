# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates

#https://www.flaticon.com/free-icon/zombie_742863?term=zombie via @theflaticon
#https://www.flaticon.com/free-icon/cool_599447?term=emoji&page=1&position=5 
#https://www.flaticon.com/free-icon/basketball-ball_889442?term=ball&page=1&position=8
# and open the template in the editor.

import pygame
import random
import math
from pygame import mixer

#Initialize the pygame
pygame.init()
    
#create the screen
(width,height) =(800,600)
screen = pygame.display.set_mode((width,height))

#background colour
background_colour = (0,0,0)
screen.fill(background_colour)


#set title caption and icon
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Apocalypse')


#object
class player:
    x = 370
    y = 480
    dx = 0
    dy = 0

class bullet:
    def __init__(playerX,playerY):
        bulletX = playerX
        bulletY = playerY
        state = "ready"
        bulletdX = 0
        bulletdY = 0

class walker:
    pass 

class runner:
    pass

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY= 480
playerdX = 0
playerdY = 0

#Bullet 
bulletImg = pygame.image.load('bullet.png')
bulletX = playerX
bulletY= playerY
bulletdX = 0
bulletdY = 0
bulletState = "ready"
lastDirection = 0

#functions
def player(x,y):
    screen.blit(playerImg,(x,y))

def fire_bullet(x,y):
    screen.blit(bulletImg,(x,y))


running = True
while running:
    screen.fill(background_colour)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerdX = -1
                lastDirection = 0
            if event.key == pygame.K_RIGHT:
                playerdX = 1
                lastDirection = 1
            if event.key == pygame.K_UP:
                playerdY = -1
                lastDirection = 2
            if event.key == pygame.K_DOWN:
               playerdY = 1
               lastDirection = 3
            if bulletState is "ready":
                if event.key == pygame.K_w:
                    bulletState = "fired"
                    bulletdY = -2
                if event.key == pygame.K_s:
                    bulletState = "fired"
                    bulletdY = 2
                if event.key == pygame.K_d:
                    bulletState = "fired"
                    bulletdX = 2
                if event.key == pygame.K_a:
                    bulletState = "fired"
                    bulletdX = -2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerdX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerdY = 0

    playerX += playerdX
    playerY += playerdY
    bulletX += bulletdX
    bulletY += bulletdY
    # Player Movement
    if playerX < 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if playerY < 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    # Bullet Movement
    if bulletState is "fired":
        if bulletX < 0 or bulletX > 780 or bulletY < 0 or bulletY > 580:
            bulletState = "ready"
            bulletdX = 0
            bulletdY = 0
    elif bulletState is "ready":
        bulletX = playerX 
        bulletY = playerY


    fire_bullet(bulletX,bulletY)
    player(playerX,playerY)
    pygame.display.update()


