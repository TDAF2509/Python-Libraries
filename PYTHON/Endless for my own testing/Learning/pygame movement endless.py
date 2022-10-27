import pygame
import time
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
Spin=[pygame.image.load('Spin1.gif'),pygame.image.load('Spin2.gif'),pygame.image.load('Spin3.gif'),pygame.image.load('Spin4.gif')]
idleChar=pygame.image.load('sonic idle.gif')
bg1=pygame.image.load('Green_Hill_Zone2.png')
bg2=pygame.image.load('Ice_Zone.png')
bg3=[pygame.image.load('snow1.png'),pygame.image.load('snow2.png'),pygame.image.load('snow3.png'),pygame.image.load('snow4.png'),pygame.image.load('snow5.png')]
bg1=pygame.transform.scale(bg1,(screenWidth+screenWidth+screenWidth+screenWidth+screenWidth-48,screenHeight))
bg2=pygame.transform.scale(bg2,(screenWidth,screenHeight+200))

X=300
Y=380
width=64
height=64
speed=10

clock=pygame.time.Clock()

isJump=False
jumpCount=10

Right=True
Snow=True
walkCount=0
snowCount=0
i=0
n=0
bgchange=0

font=pygame.font.SysFont(None,25)#25 is the size of the font

def text(msg,color):
    screen_text=font.render(msg,True,color)
    window.blit(screen_text,[width/2 -180,height/2])

def gameMenu():
    window.fill(black)
    text("WELCOME TO ENDLESS RUNNER",green)
    time.sleep(4)
    
#gameMenu()

def BackgroundChange0():
    global n
    window.blit(bg1,[n,0])
    n=n-15
    window.blit(bg1,[screenWidth+screenWidth+screenWidth+screenWidth+screenWidth+n,0])
    n=n-15
        
    if screenWidth+screenWidth+screenWidth+screenWidth+screenWidth+n<=0:
        n=0

def redrawGameWindow():
    global walkCount
    global jumpCount
    global snowCount
    global i
    global n
    global bgchange
    global gameRun
    
    if walkCount +1>=12:
        walkCount=0

    if Right:
        window.blit(runRight[walkCount//2],(300,380))
        walkCount +=1    
    else:
        window.blit(Spin[i],(X,Y))
        
    pygame.display.update()

gameRun=True
while gameRun:
    gameMenu()
    clock.tick(12)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameRun=False

    keys= pygame.key.get_pressed()

    if not (isJump):    
        if keys[pygame.K_SPACE]:
            isJump=True
            Right=False
            walkCount=0
   
    else:
        if jumpCount>=-10:
            neg=1
            if jumpCount<0:
                neg=-1
            Y -=(jumpCount**2)*0.5*neg
            i=i+1
            if i>=4:
                i=0
            jumpCount -=1
        else:
            isJump=False
            Right=True
            jumpCount=10
            i=0
    redrawGameWindow()
    BackgroundChange0()
pygame.quit()
