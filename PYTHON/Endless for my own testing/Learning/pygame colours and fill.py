import pygame
pygame.init()


blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)

GameDisplay=pygame.display.set_mode((800,600))


pygame.display.set_caption('ENDLESS')

gameExit= False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit=True

    #GameDisplay.fill(blue)#this fills the window with blue
    GameDisplay.fill(black)#this fills the window with black
    pygame.draw.rect(GameDisplay,green,[400,300,40,40])#creates a green square
    pygame.draw.rect(GameDisplay,red,[300,300,40,40])#creates a red square
    #[where top left x coordinate,top left y coordinate, width,height]


    GameDisplay.fill(green, rect=[200,200,50,50])#Another way of making squares
    #This square is the top left one
    pygame.display.update()#this updates the window so it fills


pygame.quit()
quit()
