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
Jump=[pygame.image.load('Spin1.gif'),pygame.image.load('Spin2.gif'),pygame.image.load('Spin3.gif'),pygame.image.load('Spin4.gif')]
Fireball=[pygame.image.load('fireball1.png'),pygame.image.load('fireball2.png'),pygame.image.load('fireball3.png'),pygame.image.load('fireball4.png'),pygame.image.load('fireball5.png')]
saw=[pygame.image.load('saw1.png'),pygame.image.load('saw2.png'),pygame.image.load('saw3.png'),pygame.image.load('saw4.png'),pygame.image.load('saw5.png'),pygame.image.load('saw6.png'),pygame.image.load('saw7.png')]
bg1=pygame.image.load('Green_Hill_Zone2.png')
bg3=[pygame.image.load('snow1.png'),pygame.image.load('snow2.png'),pygame.image.load('snow3.png'),pygame.image.load('snow4.png'),pygame.image.load('snow5.png')]
bg1=pygame.transform.scale(bg1,(screenWidth+screenWidth+screenWidth+screenWidth+screenWidth-48,screenHeight))

CurrentScore=0
HighScore=0
TimesPlayed=1
KeysCollected=0

if TimesPlayed<1:
    lines=Stats.readlines()
    HighScore=lines[1]
    TimesPlayed=lines[2]
    KeysColleceted=lines[3]

Stats=open("TEST SCORE.txt","w+")
Stats.write("Score: "+str(CurrentScore)+"\n")
Stats.write("HighScore: "+str(HighScore)+"\n")
Stats.write("Number of times played: "+str(TimesPlayed)+"\n")
Stats.write("Number of Keys collected: "+str(KeysCollected)+"\n")
Stats.close()
#file.write("Time Spent on the game: "+PlayTime+"\n")





X=300
Y=380
playerposX=300
clock=pygame.time.Clock()

isJump=False
jumpCount=10
Run=True
slide=True
FireBall=True
Snow=True
spin=True
collisions=False
walkCount=0
snowCount=0
spinCount=0
slideCount=0
fbCount=0
TCount=0
i=0
n=0
obstaclemove=-500
obstaclemovefb=-500
obstaclemoveT=-500
t=0
    
def retry():
    global obstaclemove
    global obstaclemovefb
    global X
    global Y
    global Run
    global isJump
    global jumpCount
    global playerposX
    global KeysCollected
    global CurrentScore
    global HighScore
    global TimesPlayed
    global PlayTime

            
    isJump=False
    Run=False
    X=300
    Y=380
    playerposX=0
    obstaclemove=-500
    obstaclemovefb=-500
    pygame.font.init()
    header=pygame.font.SysFont(None,140)
    font=pygame.font.SysFont(None,55)#25 is the size of the font
    header_text=header.render('GAME OVER',False,(255,0,0))
    screen_textRT=font.render('PRESS c TO PLAY AGAIN OR q TO QUIT',False,(255,0,0))
    gameOver=True
    while gameOver:
        window.fill(black)
        window.blit(header_text,(100,screenHeight/4))
        window.blit(screen_textRT,(40,screenHeight/2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                while event.key==pygame.K_c:
                    Run=True
                    gameStart=True
                    jumpCount=10
                    gameLoop()

def gameLoop():
    global isJump
    global Run
    global Y
    global X
    global jumpCount
    global i
    global n
    global t
    global obstaclemove
    global obstaclemovefb
    global playerposX
    global CurrentScore
    global HighScore


    def obstacle():
        global obstaclemove
        global obstaclemovefb
        global spinCount
        global fbCount
        global collisions
        global HighScore
        if spinCount +1>=7:
            spinCount=0
        if spin:
            Saw=window.blit(saw[spinCount//2],(obstaclemove,400))
            spinCount +=1
        if fbCount +1>=4:
            fbCount=0
        if FireBall:
            fireball=window.blit(Fireball[fbCount//2],(obstaclemovefb,200))
            fbCount +=1

        obstaclemove=obstaclemove-10
        obstaclemovefb=obstaclemovefb-100
        
        if screenWidth+obstaclemove<=0:
            obstacleplacement=random.randint(screenWidth,screenWidth+screenWidth)
            obstaclemove=obstacleplacement

        if obstaclemovefb<=320 and obstaclemovefb>=220 and Y<=233 or obstaclemove<=330 and obstaclemove>=220 and Y<=400 and Y>=380:
            print("TEST collision")
            if CurrentScore>HighScore:
                HighScore=CurrentScore
            retry()
        
        obstaclemove=obstaclemove-50
        while screenWidth+obstaclemove<=0 and screenWidth+obstaclemovefb<=0:
            obstacleplacement=random.randint(screenWidth,screenWidth+screenWidth)
            obstaclemove=obstacleplacement
            obstacleplacementfb=random.randint(screenWidth,screenWidth+screenWidth)
            obstaclemovefb=obstacleplacementfb
    

    def BackgroundChange0():
        global n
        window.blit(bg1,[n,0])
        n=n-15
        window.blit(bg1,[screenWidth+screenWidth+screenWidth+screenWidth+screenWidth+n,0])
        n=n-50
            
        if screenWidth+screenWidth+screenWidth+screenWidth+screenWidth+n<=0:
            n=0

    def redrawGameWindow():
        global walkCount
        global jumpCount
        global i
        global Slide
        global playerposX
        
        if walkCount +1>=12:
            walkCount=0

        if Run:
            window.blit(runRight[walkCount//2],(playerposX,380))
            walkCount +=1
            
        else:
            window.blit(Jump[i],(X,Y))
            
        pygame.display.update()

    gameStart=True
    gameRun=False

    while gameStart:
        playerposX=0
        while playerposX<300:
            playerposX=playerposX+5
            redrawGameWindow()
            BackgroundChange0()
            clock.tick(15)
        else:
            gameStart=False
            gameRun=True
            while gameRun:
                #PlayTime=    
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        gameRun=False
                        if event.key==pygame.K_c:
                            gameLoop()

                keys= pygame.key.get_pressed()
                if not (isJump):    
                    if keys[pygame.K_SPACE]:
                        isJump=True
                        Run=False
                        Slide=False
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
                        Slide=False
                        jumpCount=10
                        i=0
                #print(obstaclemovefb)
                clock.tick(15)
                redrawGameWindow()
                BackgroundChange0()
                obstacle()

                HighScore=int(HighScore)
                print(HighScore)


                if n==0:
                    CurrentScore=CurrentScore+1
                    if CurrentScore>HighScore:
                        HighScore=CurrentScore
                    print(CurrentScore)
                Stats=open("TEST SCORE.txt","w+")
                Stats.write("Score: "+str(CurrentScore)+"\n")
                Stats.write("HighScore: "+str(HighScore)+"\n")
                Stats.write("Number of times played: "+str(TimesPlayed)+"\n")
                Stats.write("Number of Keys collected: "+str(KeysCollected)+"\n")
                Stats.close()
                                      
                    
            pygame.quit()
            quit()

gameLoop()
