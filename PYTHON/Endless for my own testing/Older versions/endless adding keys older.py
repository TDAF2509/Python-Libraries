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
Keys=[pygame.image.load('download.png'),pygame.image.load('Key2.png')]
bg3=[pygame.image.load('snow1.png'),pygame.image.load('snow2.png'),pygame.image.load('snow3.png'),pygame.image.load('snow4.png'),pygame.image.load('snow5.png')]
bg1=pygame.transform.scale(bg1,(screenWidth+screenWidth+screenWidth+screenWidth+screenWidth-48,screenHeight))

CurrentScore=0
Stats=open("TEST SCORE.txt","r")
lines=Stats.readlines()
TimesPlayed=lines[1][24]
if lines[1][25] != " ":
    TimesPlayed=TimesPlayed+lines[1][25]
    if lines[1][26]!=" ":
        TimesPlayed=TimesPlayed+lines[1][26]
TimesPlayed=int(TimesPlayed)

if TimesPlayed>=1:
    Stats=open("TEST SCORE.txt","r")
    lines=Stats.readlines()
    HighScore=lines[0][11]
    if lines[0][12] != " ":
        HighScore=HighScore+lines[0][12]
    KeysCollected=lines[2][26]
    if lines[2][27]!=" ":
        KeysCollected=KeysCollected+lines[2][27]
    PlayTime=lines[3][17]
    if lines[3][18]!=" ":
        PlayTime=PlayTime+lines[3][18]
        if lines[3][19]!=" " and lines[3][19]!=".":
            PlayTime=PlayTime+lines[3][19]
            if lines[3][20]!=" " and lines[3][20]!=".":
                PlayTime=PlayTime+lines[3][20]
    
else:
    HighScore=0
    KeysCollected=0

HighScore=int(HighScore)
PlayTime=int(PlayTime)
TimesPlayed=int(TimesPlayed)

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
KEY=True
walkCount=0
snowCount=0
spinCount=0
slideCount=0
fbCount=0
KCount=0
i=0
n=0
obstaclemove=-500
obstaclemovefb=-500
obstaclemoveT=-500
keymove=-500
    
def retry():
    global obstaclemove
    global obstaclemovefb
    global keymove
    global X
    global Y
    global KEY
    global Run
    global isJump
    global jumpCount
    global playerposX
    global KeysCollected
    global CurrentScore
    global HighScore
    global TimesPlayed
    global PlayTime
    global KeysCollected

    isJump=False
    Run=False
    X=300
    Y=380
    playerposX=0
    obstaclemove=-500
    obstaclemovefb=-500
    keymove=-500
    pygame.font.init()
    header=pygame.font.SysFont(None,140)
    font=pygame.font.SysFont(None,55)#25 is the size of the font
    Score=pygame.font.SysFont(None,55)
    header_text=header.render('GAME OVER',False,(255,0,0))
    Score_text=Score.render(('SCORE: '+str(CurrentScore)),False,(255,0,0))
    HScore_text=Score.render(('HIGH SCORE: '+str(HighScore)),False,(255,0,0))
    screen_textRetry=font.render('PRESS c TO PLAY AGAIN OR q TO QUIT',False,(255,0,0))
    gameOver=True
    while gameOver:
        window.fill(black)
        window.blit(header_text,(100,screenHeight/8))
        window.blit(Score_text,(40,screenHeight/3))
        window.blit(HScore_text,(485,screenHeight/3))
        window.blit(screen_textRetry,(40,screenHeight/2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                while event.key==pygame.K_c:
                    CurrentScore=0
                    Run=True
                    gameStart=True
                    KEY=True
                    jumpCount=10
                    gameLoop()

def gameLoop():
    global isJump
    global Run
    global Y
    global X
    global jumpCount
    global KCount
    global i
    global n
    global t
    global obstaclemove
    global obstaclemovefb
    global playerposX
    global CurrentScore
    global HighScore
    global PlayTime
    global KeysCollected
    global TimesPlayed

    def obstacle():
        global obstaclemove
        global obstaclemovefb
        global spinCount
        global fbCount
        global KCount
        global collisions
        global HighScore
        global TimesPlayed
        global KEY
        global keymove
        global KeysCollected
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
        if KCount +1>=2:
            KCount=0
        if KEY:
            window.blit(Keys[KCount//2],(keymove,400))
            KCount +=1

        obstaclemove=obstaclemove-10
        obstaclemovefb=obstaclemovefb-100
        keymove=keymove-100
        
        if screenWidth+obstaclemove<=0:
            obstacleplacement=random.randint(screenWidth,screenWidth+screenWidth)
            obstaclemove=obstacleplacement

        if obstaclemovefb<=320 and obstaclemovefb>=220 and Y<=233 or obstaclemove<=330 and obstaclemove>=220 and Y<=400 and Y>=380:
            TimesPlayed=int(TimesPlayed)
            TimesPlayed=TimesPlayed+1
            print(TimesPlayed,"TIMES PLAYED")
            if CurrentScore>HighScore:
                HighScore=CurrentScore
            retry()
        if keymove<=330 and keymove>=220 and Y>=380:
            KeysCollected=int(KeysCollected)
            KeysCollected=KeysCollected+1
            keymove=-500
            
        
        obstaclemove=obstaclemove-50
        while screenWidth+obstaclemove<=0 and screenWidth+obstaclemovefb<=0 and screenWidth+keymove<=0:
            obstacleplacement=random.randint(screenWidth,screenWidth+screenWidth)
            obstaclemove=obstacleplacement
            obstacleplacementfb=random.randint(screenWidth,screenWidth+screenWidth)
            obstaclemovefb=obstacleplacementfb
            keyplacement=random.randint(screenWidth,screenWidth+10)
            keymove=keyplacement
            
    

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

                redrawGameWindow()
                BackgroundChange0()
                obstacle()
                clock.tick(15)
                KEY=True
                PlayTime=PlayTime+(1)
                HighScore=int(HighScore)
                if n==0:
                    CurrentScore=CurrentScore+1
                    if CurrentScore>HighScore:
                        HighScore=CurrentScore
                Stats=open("TEST SCORE.txt","w+")
                Stats.write("HighScore: "+str(HighScore)+"          "+"\n")
                Stats.write("Number of times played: "+str(TimesPlayed)+"           "+"\n")
                Stats.write("Number of Keys collected: "+str(KeysCollected)+"           "+"\n")
                Stats.write("Total Play time: "+str(PlayTime/15)+"           "+"\n")
                Stats.close()
            pygame.quit()
            quit()

gameLoop()
