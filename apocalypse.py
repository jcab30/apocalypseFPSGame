# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates

#https://www.flaticon.com/free-icon/zombie_742863?term=zombie via @theflaticon
#https://www.flaticon.com/free-icon/cool_599447?term=emoji&page=1&position=5 
#https://www.flaticon.com/free-icon/basketball-ball_889442?term=ball&page=1&position=8
#and open the template in the editor.
#https://www.flaticon.com/free-icon/zombie_1680409?term=zombie&page=2&position=49

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

#background
background = pygame.image.load('wasteland.png')

#set title caption and icon
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Apocalypse')

#Score 
score = 0
font = pygame.font.Font('freesansbold.ttf',32)

#gameover screen
gameOver = pygame.image.load('gameover.png')


#Player Class // not used yet
class player:
    def __init__(self,playerX,playerY):
        self.playerImg = pygame.image.load('player.png')
        self.playerX = playerX
        self.playerY = playerY
        self.playerdX = 0
        self.playerdY = 0

#Bullet Class
class bullet:
    def __init__(self,xcor,ycor):
        self.bulletImg = pygame.image.load('bullet.png')
        self.bulletX = xcor 
        self.bulletY = ycor 
        self.bulletdX = 0
        self.bulletdY = 0
        self.bulletState = "ready"
        self.num = 0
    def fireUp(self):
        if self.bulletState is "ready":
            self.bulletState = "fired"  
            self.bulletdY = -4
            return True
        else:
            return False
    def fireDown(self):
        if self.bulletState is "ready":
            self.bulletState = "fired"  
            self.bulletdY = 4
            return True
        else:
            return False
    def fireRight(self):
        if self.bulletState is "ready":
            self.bulletState = "fired"  
            self.bulletdX = 4
            return True
        else:
            return False
    def fireLeft(self):
        if self.bulletState is "ready":
            self.bulletState = "fired"  
            self.bulletdX = -4
            return True
        else:
            return False
    def updateBulletMovement(self,playerX,playerY):
        if self.bulletState is "fired":
            if self.bulletX < 0 or self.bulletX > 780 or self.bulletY < 0 or self.bulletY > 580:
                self.bulletState = "ready"
                self.bulletdX = 0
                self.bulletdY = 0
        elif self.bulletState is "ready":
            self.bulletX = playerX 
            self.bulletY = playerY
            self.bulletdX = 0
            self.bulletdY = 0

class walker:
    def __init__(self):
        self.img = pygame.image.load("walker.png")
        self.xcor= (random.choice([random.randint(-100,0),random.randint(800,900)]))
        self.ycor = (random.choice([random.randint(-100,0),random.randint(600,700)]))
        self.dx = 0
        self.dy = 0
        self.speed = random.uniform(0.1,0.5)
    def updateWalkerMovement(self,playerX,playerY):
        if playerX > self.xcor:
            self.dx = self.speed
        elif playerX < self.xcor:
            self.dx = -self.speed
        else:
            self.dx = 0

        if playerY > self.ycor:
            self.dy = self.speed
        elif playerY < self.ycor:
            self.dy = -self.speed
        else:
            self.dy= 0
       
        self.xcor += self.dx
        self.ycor += self.dy

class creeper(walker):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load("creeper.png")
        self.xcor= (random.choice([random.randint(-100,0),random.randint(800,900)]))
        self.ycor = (random.choice([random.randint(-100,0),random.randint(600,700)]))
     
    #THIS DOESNT WORK FOR SOME REASON, ONLY WORKS WHEN GETTING COORDINATES FROM WALKER LIST
#    def explode(self,playerX,playerY):
#        distance = math.sqrt( (math.pow(self.xcor-playerX,2)) + (math.pow(self.ycor-playerY,2)))
#        if distance < 100:
#            explosionImage = pygame.image.load("explosion.png")
#            screen.blit(explosionImage,(200,200))
#            pygame.time.wait(1000)


# Player Initialization
playerImg = pygame.image.load('player.png')
playerX = 370
playerY= 480
playerdX = 0
playerdY = 0

player1 = player(370,480)


#Create bullets
bullet1 = bullet(playerX,playerY)
bullet2 = bullet(playerX,playerY)

#bullet magazine : unlimited supply
bulletList = []
bulletList.append(bullet1)
bulletList.append(bullet2)

#Create Enemies
walkers = []
creepers = []
i = 0
while i <= 3:
    walkers.append(walker())
    i+=1

walkers.append(creeper())
creepers.append(creeper())


#Screen drawings
def player(x,y):
    screen.blit(playerImg,(x,y))

def fire_bullet(bullet):
    screen.blit(bullet.bulletImg,(bullet.bulletX+50,bullet.bulletY+50))

def walkerUpdate(enemy):
    screen.blit(enemy.img,(enemy.xcor,enemy.ycor))

def show_score(x,y):
    global score
    score_text = font.render("Score :" +str(score),True,(255,255,255))
    screen.blit(score_text,(x,y))

#Walker attack algorithim - get hit once  you lose
def checkGameOver(enemy):
    distance = math.sqrt( (math.pow(enemy.xcor-playerX,2)) + (math.pow(enemy.ycor-playerY,2)))
    if distance < 27:
        return False
    else:
        return True


#Score algorithim        
def checkCollision(bullet,enemy):
    global score 
    if bullet.bulletState is "fired":
        distance = math.sqrt( (math.pow(enemy.xcor-bullet.bulletX,2)) + (math.pow(enemy.ycor-bullet.bulletY,2)))
        if distance < 27:
            bullet.bulletState = "ready"
            score +=1
            enemy.xcor = (random.choice([random.randint(-100,0),random.randint(800,900)]))
            enemy.ycor = (random.choice([random.randint(-100,0),random.randint(600,700)]))

#Main while loop
running = True
while running:

    #background
    screen.fill(background_colour)
    #background image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerdX = -2
            if event.key == pygame.K_RIGHT:
                playerdX = 2
            if event.key == pygame.K_UP:
                playerdY = -2
            if event.key == pygame.K_DOWN:
               playerdY = 2
        
            if event.key == pygame.K_w:
                for bullet in bulletList:
                    if bullet.fireUp():
                        break
            if event.key == pygame.K_s:
                for bullet in bulletList:
                    if bullet.fireDown():
                        break
            if event.key == pygame.K_a:
                for bullet in bulletList:
                    if bullet.fireLeft():
                        break
            if event.key == pygame.K_d:
                for bullet in bulletList:
                    if bullet.fireRight():
                        break
            if event.key == pygame.K_LCTRL:
                playerdX *= 1.7
                playerdY *= 1.7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:   
                playerdX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerdY = 0
            if event.key == pygame.K_LCTRL:
                playerdX *= 0.666667
                playerdY *= 0.666667

    playerX += playerdX
    playerY += playerdY

    bullet1.bulletX += bullet1.bulletdX
    bullet1.bulletY += bullet1.bulletdY
    
    bullet2.bulletX += bullet2.bulletdX
    bullet2.bulletY += bullet2.bulletdY

    # Player Movement
    if playerX < 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if playerY < 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    player(playerX,playerY)

    for bullet in bulletList:
        bullet.updateBulletMovement(playerX,playerY)
        fire_bullet(bullet)
        for w in walkers:
            checkCollision(bullet,w)
        
    #Walker movement
    for w in walkers:
        w.updateWalkerMovement(playerX,playerY)
        walkerUpdate(w)
        if not checkGameOver(w):
            running = False
    
     #Creeper movement
    distance = math.sqrt( (math.pow(walkers[4].xcor-playerX,2)) + (math.pow(walkers[4].ycor-playerY,2)))
    if distance < 50:
        explosionImage = pygame.image.load("explosion.png")
        screen.blit(explosionImage,(walkers[4].xcor,walkers[4].ycor))
        pygame.time.wait(1000)
        running = False


    #Dynamic walker creation
    if pygame.time.get_ticks() % 50 == 0:
        walkers.append(walker())

    #Show score
    show_score(10,10)

    pygame.display.update()


#Game Over Screen
running  = True
while running:
    screen.blit(gameOver,(250,200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
