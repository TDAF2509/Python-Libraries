import pygame
pygame.init()


GameDisplay=pygame.display.set_mode((800,600))

#creates a title on the window
pygame.display.set_caption('ENDLESS')

gameExit= False

while not gameExit:
    for event in pygame.event.get():
        print(event)#this shows all the actions/events that occurs on the window


pygame.display.update()

pygame.quit()
