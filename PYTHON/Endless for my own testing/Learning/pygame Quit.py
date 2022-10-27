import pygame
pygame.init()



GameDisplay=pygame.display.set_mode((800,600))

#creates a title on the window
pygame.display.set_caption('ENDLESS')

gameExit= False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit=True
        


pygame.quit()
quit()
