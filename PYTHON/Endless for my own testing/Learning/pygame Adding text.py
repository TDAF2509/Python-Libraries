import pygame
import time
pygame.init()


blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)

width=800
height=600

GameDisplay=pygame.display.set_mode((800,600))


pygame.display.set_caption('ENDLESS')

gameExit= False

lead_x=width/2
lead_y=height/2
lead_x_change=0
lead_y_change=0
blocksize= 10
FPS=15

font=pygame.font.SysFont(None,25)#25 is the size of the font

def text(msg,color):#msg is short for message and is quicker than defining
    #each piece of text is a message
    screen_text=font.render(msg,True,color)
    GameDisplay.blit(screen_text,[width/2 -50,height/2])

clock=pygame.time.Clock()

while not gameExit:
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
            if event.key==pygame.K_UP:
                lead_y_change = -blocksize
                lead_x_change=0
            if event.key==pygame.K_DOWN:
                lead_y_change = blocksize
                lead_x_change=0

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                lead_x_change=0


    if lead_x>=width or lead_x<=0 or lead_y>=height or lead_y<=10:
        gameExit=True

    lead_x += lead_x_change
    lead_y += lead_y_change
    GameDisplay.fill(black)
    pygame.draw.rect(GameDisplay,green,[lead_x,lead_y,blocksize,blocksize])
    pygame.display.update()
    
    clock.tick(FPS)

text("YOU LOSE",red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
