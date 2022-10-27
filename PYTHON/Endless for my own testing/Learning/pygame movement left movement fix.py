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


runLeft=[pygame.image.load('sonic run 1.gif'),pygame.image.load('sonic run 2.gif'),pygame.image.load('sonic run 3.gif'),pygame.image.load('sonic run 4.gif'),pygame.image.load('sonic run 5.gif'),pygame.image.load('sonic run 6.gif')]
runRight=[pygame.image.load('sonic run 1 flip.gif'),pygame.image.load('sonic run 2 flip.gif'),pygame.image.load('sonic run 3 flip.gif'),pygame.image.load('sonic run 4 flip.gif'),pygame.image.load('sonic run 5 flip.gif'),pygame.image.load('sonic run 6 flip.gif')]
idleChar=pygame.image.load('sonic idle.gif')
bg=pygame.image.load('green hill zone.gif')
bg=pygame.transform.scale(bg,(screenWidth,screenHeight))

X=300
Y=400
width=64
height=64
speed=10


clock=pygame.time.Clock()

isJump=False
jumpCount=10


Right=True
walkCount=0
walkCountLeft=0



def redrawGameWindowRight():
    global walkCount
    global walkCountLeft
    global Right
    window.blit(bg,[0,0])

    if walkCount +1>=12:
        walkCount=0

    if Right:
        window.blit(runRight[walkCount//2],(X,Y))
        walkCount +=1
        Right=True
    else:
        window.blit(idleChar,(X,Y))
        
    pygame.display.update()


gameRun=True
while gameRun:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameRun=False

    keys= pygame.key.get_pressed()

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
            Right=True
            jumpCount=10

    #bg_size = bg.get_size()
    bg_rect = bg.get_rect()
    screen = pygame.display.set_mode((screenWidth,screenHeight))#bg_size)
    #w,h = bg_size
    x = 0
    y = 0

    y1 = 0
    x1 = -screenWidth

    running = True

    while running:
        screen.blit(bg,bg_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        x1 += 5
        x += 5
        screen.blit(bg,(x,y))
        screen.blit(bg,(x1,y1))
        if x > screenWidth:
            x = -screenWidth
        if x1 > screenWidth:
            x1 = -screenWidth
        pygame.display.flip()
        redrawGameWindowRight()
        pygame.display.update()
        clock.tick(15)




pygame.quit()
