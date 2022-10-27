import pygame
pygame.init()

screenWidth=800
screenHeight=600
window=pygame.display.set_mode([screenWidth,screenHeight])
pygame.display.set_caption("ENDLESS")

black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)
red=(255,0,0)



runRight=[pygame.image.load('sonic run 1 flip.gif'),pygame.image.load('sonic run 2 flip.gif'),pygame.image.load('sonic run 3 flip.gif'),pygame.image.load('sonic run 4 flip.gif'),pygame.image.load('sonic run 5 flip.gif'),pygame.image.load('sonic run 6 flip.gif')]
bg=pygame.image.load('Green_Hill_Zone2.png')
bg=pygame.transform.scale(bg,(screenWidth,screenHeight))

X=50
Y=425
width=64
height=64
speed=10


clock=pygame.time.Clock()

isJump=False
jumpCount=10

Left=True
Right=False
walkCount=0



def redrawGameWindow():
    global walkCount
    window.blit(bg,[0,0])

    if walkCount +1>=12:
        walkCount=0

    if Left:
        window.blit(runLeft[walkCount//2],(X,Y))
        walkCount += 1
    elif Right:
        window.blit(runRight[walkCount//2],(X,Y))
        walkCount +=1
        
    pygame.display.update()



gameRun=True
while gameRun:
    clock.tick(12)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameRun=False

    keys= pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and X >speed:
        X -=speed
        Left=True
        Right=False
    if keys[pygame.K_RIGHT] and X< screenWidth - width - speed:
        X +=speed
        Right=True
        Left=False

    else:
        Right=False
        Left=False
        walkCount=0
    if not (isJump):    
        if keys[pygame.K_SPACE]:
            isJump=True
            Left=False
            Right=False
            walkCount=0
           
    else:
        if jumpCount>=-10:
            neg=1
            if jumpCount<0:
                neg=-1
            Y -=(jumpCount**2)*0.5*neg
            jumpCount -=1
        else:
            isJump=False
            jumpCount=10
    redrawGameWindow()



pygame.quit()
