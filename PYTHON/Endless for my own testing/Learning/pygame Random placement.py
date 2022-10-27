import pygame
import time
import random
pygame.init()


blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)

width=800
height=600

GameDisplay=pygame.display.set_mode((800,600))


pygame.display.set_caption('ENDLESS')


blocksize= 10
FPS=15

font=pygame.font.SysFont(None,25)#25 is the size of the font

def text(msg,color):#msg is short for message and is quicker than defining
    #each piece of text is a message
    screen_text=font.render(msg,True,color)
    GameDisplay.blit(screen_text,[width/2 -180,height/2])

clock=pygame.time.Clock()


def gameLoop():
    
    gameExit= False
    gameOver=False
    lead_x=width/2
    lead_y=height/2
    lead_x_change=0
    lead_y_change=0
    randX= random.randrange(0,width-blocksize)
    randY=random.randrange(0,height-blocksize)


    isJump=False
    jumpCount=10



    
    while not gameExit:

        while gameOver==True:
            GameDisplay.fill(black)
            text("Game over, press c to play again or q to quit",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False

                    if event.key==pygame.K_c:
                        gameLoop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    lead_x_change = -blocksize
                    lead_y_change = 0
                if event.key==pygame.K_RIGHT:
                    lead_x_change = blocksize
                    lead_y_change = 0
                if not(isJump):
                    if event.key==pygame.K_UP:
                        lead_y_change = -blocksize
                        lead_x_change=0
                    if event.key==pygame.K_DOWN:
                        lead_y_change = blocksize
                        lead_x_change=0
                    if event.key==pygame.K_SPACE:
                        isJump=True
                else:
                    if jumpCount>=-10:
                        neg=1
                        if jumpCount<0:
                            neg=-1
                        lead_y_change -=(jumpCount**2)*0.5*neg
                        jumpCount -=1
                    else:
                        isJump=False
                        jumpCount=10
                

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    lead_x_change=0


        if lead_x>=width-10 or lead_x<=0 or lead_y>=height or lead_y<=10:
            lead_x_change=0
            lead_y_change=0
            gameOver=True

        lead_x += lead_x_change
        lead_y += lead_y_change
        GameDisplay.fill(black)
        pygame.draw.rect(GameDisplay,red,[randX,randY,blocksize,blocksize])
        pygame.draw.rect(GameDisplay,green,[lead_x,lead_y,blocksize,blocksize])
        pygame.display.update()
        
        clock.tick(FPS)


    pygame.quit()
    quit()

gameLoop()
