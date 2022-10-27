import pygame
pygame.init()

#The GameDisplay is the canvas/background that will be updated
GameDisplay=pygame.display.set_mode((800,600))


#this updates the game display, pygame.display.flip() is also a valid option
#pygame.display.flip() updates everything at once
#pygame.display.update() updates individual sections
pygame.display.update()

#this uninitialises everything
pygame.quit()

