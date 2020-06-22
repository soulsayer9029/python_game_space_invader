import pygame
import random
import math
#initialize the pygame
pygame.init()

#create the screen of size(800x600)
screen=pygame.display.set_mode((800,600))
# setting the icon of the game
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
#setting the background image
background=pygame.image.load('background1.png')

#score
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)

textX=10
textY=10
#game over text
over_font=pygame.font.Font('freesansbold.ttf',50)

def game_over():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))

def show_score(x,y):
    score=font.render("Score :" + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
#player
player_image=pygame.image.load('space-invaders.png')
playerX=370
playerY=480
playerX_change=0
def player(x,y):
    screen.blit(player_image,(x,y))
#enemy
enemy_image=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
no_of_enemies=5
for i in range(no_of_enemies):
    enemy_image.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(64,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(12)
    enemyY_change.append(40)
def enemy(x,y,i):
    screen.blit(enemy_image[i],(x,y))
#bullet
bullet=pygame.image.load('bullet(1).png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=25
bullet_state='ready'
#bullet state=ready means that we cant see the bullet
            #=fire means that bullet is on screen and is moving
def bullet_fire(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bullet,(x+16,y+10))
#collision function
def iscollision(bulletX,bulletY,enemyX,enemyY):
    distance=math.sqrt(((enemyX-bulletX)**2)+((enemyY-bulletY)**2))
    if distance<27:
         return True
    else:
         return False
    
    




running=True
#main loop
while running:
    pygame.time.delay(15)
    screen.fill((0,0,0))
    #background image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #movement of player
    #if key is pressed check whether it is right or left
        if event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_LEFT:
                playerX_change=-5
                
            if event.key==pygame.K_RIGHT:
                playerX_change=5
            if event.key==pygame.K_SPACE:
                if bullet_state == 'ready':
                    #get current position of spaceship for bullet release
                    bulletX=playerX
                    bullet_fire(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                
                playerX_change=0
                 
            
            
        
    #player not going out of bounds
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736


    #player movement

    
    playerX=playerX+playerX_change


    #enemy not going out of bounds and enemy movement
    for i in range(no_of_enemies):
        #GAME OVER
        if enemyY[i]>440:
            for j in range(no_of_enemies):
                enemyY[j]=2000
                game_over()
                break
        enemyX[i]=enemyX[i]+enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]=5
            enemyY[i]=enemyY[i]+enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-5
            enemyY[i]=enemyY[i]+enemyY_change[i]
    #collision
        collision=iscollision(bulletX,bulletY,enemyX[i],enemyY[i])
        if collision:
            bulletY=480
            bullet_state='ready'
            score_value=score_value+1
            enemyX[i]=random.randint(0,736)
            enemyY[i]=random.randint(50,150)
                
        enemy(enemyX[i],enemyY[i],i)
    

    enemyX=enemyX+enemyX_change
    #bullet movement
    if bulletY<=0:
        bulletY=480
        bullet_state='ready'
    if bullet_state == 'fire':
        bullet_fire(bulletX,bulletY)
        bulletY=bulletY-bulletY_change


    
   

    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
    
pygame.quit()
    
    
