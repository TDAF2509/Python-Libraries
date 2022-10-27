import pygame
pygame.init()

screenWidth=1200
screenHeight=1000
window=pygame.display.set_mode([screenWidth,screenHeight])
pygame.display.set_caption("ENDLESS")
bg=pygame.image.load('Green_Hill_Zone.png')
bg=pygame.transform.scale(bg,(1200,800))


sprite=pygame.image.load('sonic run.png').convert()
cells=[]
for n in range(8):
    Swidth,Sheight=(70,85)
    rect=pygame.Rect(n*Swidth,0,Swidth,Sheight)
    image=pygame.Surface(rect.size).convert()
    image.blit(sprite,(0,0),rect)
    cells.append(image)

playerImg=cells[0]
player=playerImg.get_rect()
player.center=(300,400)
idle=pygame.image.load('sonic idle.png')


Run=False

black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)
red=(255,0,0)

X=50
Y=425
width=50
height=50
speed=10

isJump=False
jumpCount=10

gameRun=True
while gameRun:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameRun=False
    if Run:
        playerImg=cells[frame]
        frame+=1
        if frame>= len(cells):
            Run=False
    else:
        playerImg=cells[0]
        keys= pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and X >speed:
            X -=speed
        if keys[pygame.K_RIGHT] and X< screenWidth - width - speed:
            X +=speed
            Run=True
            frame=0
        if not (isJump):    
            if keys[pygame.K_UP] and Y> speed:
                Y -=speed
            if keys[pygame.K_DOWN] and Y<screenHeight - height - speed:
                Y +=speed
            if keys[pygame.K_SPACE]:
                isJump=True
               
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

    window.blit(bg,(0,0))

    window.blit(playerImg,(X,Y))

    #window.blit(idle,(X,Y))
    
    #pygame.draw.rect(window,green,(X,Y,width,height))
    pygame.display.update()

pygame.quit()
