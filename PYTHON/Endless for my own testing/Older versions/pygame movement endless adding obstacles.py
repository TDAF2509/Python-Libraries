import pygame
import time
import random
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
tailsRun=[pygame.image.load('tails run1.png'),pygame.image.load('tails run2.png'),pygame.image.load('tails run3.png')]
Jump=[pygame.image.load('Spin1.gif'),pygame.image.load('Spin2.gif'),pygame.image.load('Spin3.gif'),pygame.image.load('Spin4.gif')]
saw=[pygame.image.load('saw1.png'),pygame.image.load('saw2.png'),pygame.image.load('saw3.png'),pygame.image.load('saw4.png'),pygame.image.load('saw5.png'),pygame.image.load('saw6.png'),pygame.image.load('saw7.png')]
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
isSlide=False
slideCount=0
jumpCount=10

Run=True
Snow=True
spin=True
walkCount=0
snowCount=0
spinCount=0
i=0
n=0
S=0
obstaclemove=-500
bgchange=0



font=pygame.font.SysFont(None,25)#25 is the size of the font

def text(msg,color):
    screen_text=font.render(msg,True,color)
    window.blit(screen_text,[screenWidth/2 -180,screenHeight/2])

def obstacle():
    global obstaclemove
    global spinCount
    if spinCount +1>=7:
        spinCount=0
    if spin:
        window.blit(saw[spinCount//2],(obstaclemove,400))
        spinCount +=1
    obstaclemove=obstaclemove-50
    if screenWidth+obstaclemove<=0:
        obstacleplacement=random.randint(screenWidth,screenWidth+screenWidth)
        obstaclemove=obstacleplacement
    


def BackgroundChange0():
    global n
    window.blit(bg1,[n,0])
    n=n-15
    window.blit(bg1,[screenWidth+screenWidth+screenWidth+screenWidth+screenWidth+n,0])
    n=n-50
        
    if screenWidth+screenWidth+screenWidth+screenWidth+screenWidth+n<=0:
        n=0


def SLIDE():
    global S
    global slideCount
    Jump[S]
    S=S+1
    if S<=3:
        slideCount=slideCount+1
        print(S)
        if slideCount<20:
            S=0
        else:
            slideCount=0
            isSlide=False
            isJump=False
            Run=True



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

    if Run:
        window.blit(runRight[walkCount//2],(300,380))
        walkCount +=1    
    else:
        window.blit(Jump[i],(X,Y))
        
    pygame.display.update()

gameRun=True
while gameRun:
    clock.tick(12)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameRun=False

    keys= pygame.key.get_pressed()

    if not (isSlide):    
        if keys[pygame.K_DOWN]:
            isJump=False
            Run=False
            isSlide=True
            walkCount=0
   
    else:
        SLIDE()
##        if S>=0:
##            Jump[S]
##            S=S+1
##        if S<=3:
##            slideCount=slideCount+1
##            print(S)
##            if slideCount<20:
##                S=0
##            else:
##                slideCount=0
##                isSlide=False
##                isJump=False
##                Run=True
##        else:
##            isJump=False
##            Run=True
##            isSlide=False
##            jumpCount=10
##            spinCount=10
##            S=0

    if not (isJump):    
        if keys[pygame.K_SPACE]:
            isJump=True
            Run=False
            isSlide=False
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
            Run=True
            jumpCount=10
            i=0
    redrawGameWindow()
    BackgroundChange0()
    obstacle()
pygame.quit()
