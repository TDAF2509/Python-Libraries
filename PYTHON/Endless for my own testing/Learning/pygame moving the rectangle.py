import pygame
pygame.init()


blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)

GameDisplay=pygame.display.set_mode((800,600))


pygame.display.set_caption('ENDLESS')

gameExit= False

lead_x=300
lead_y=300
lead_x_change=0
lead_y_change=0

clock=pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
            if event.key==pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0
            if event.key==pygame.K_UP:
                lead_y_change = -10
                lead_x_change=0
            if event.key==pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change=0

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                lead_x_change=0


    if lead_x>=750 or lead_x<=0 or lead_y>=580 or lead_y<=10:
        gameExit=True

    lead_x += lead_x_change
    lead_y += lead_y_change
    GameDisplay.fill(black)
    pygame.draw.rect(GameDisplay,green,[lead_x,lead_y,40,40])
    pygame.display.update()
    
    clock.tick(15)


pygame.quit()
quit()
