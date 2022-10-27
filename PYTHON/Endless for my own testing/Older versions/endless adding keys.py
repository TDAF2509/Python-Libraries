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
Axe=[pygame.image.load('axe1.png'),pygame.image.load('axe2 s.png'),pygame.image.load('axe2.png'),pygame.image.load('axe3 s.png'),pygame.image.load('axe3.png'),pygame.image.load('axe4 s.png'),pygame.image.load('axe4.png'),pygame.image.load('axe5 s.png'),pygame.image.load('axe5.png'),pygame.image.load('axe5 s.png'),pygame.image.load('axe4.png'),pygame.image.load('axe4 s.png'),pygame.image.load('axe3.png'),pygame.image.load('axe3 s.png'),pygame.image.load('axe2.png'),pygame.image.load('axe2 s.png')]
target=[pygame.image.load('Meteor explosion1.png'),pygame.image.load('Meteor explosion2.png'),pygame.image.load('Meteor explosion3.png'),pygame.image.load('Meteor explosion4.png'),pygame.image.load('Meteor explosion5.png'),pygame.image.load('Meteor explosion6.png'),pygame.image.load('Meteor explosion7.png'),pygame.image.load('Meteor explosion8.png'),pygame.image.load('Meteor explosion9.png'),pygame.image.load('Meteor explosion10.png'),pygame.image.load('Meteor explosion11.png'),pygame.image.load('Meteor explosion12.png'),pygame.image.load('Meteor explosion13.png'),pygame.image.load('Meteor explosion14.png'),pygame.image.load('Meteor explosion15.png'),pygame.image.load('Meteor explosion16.png'),pygame.image.load('Meteor explosion17.png')]
Meteor=[pygame.image.load('Meteor1.png'),pygame.image.load('Meteor2.png'),pygame.image.load('Meteor3.png'),pygame.image.load('Meteor4.png'),pygame.image.load('Meteor5.png'),pygame.image.load('Meteor6.png'),pygame.image.load('Meteor7.png')]#,pygame.image.load('Meteor8.png')]
Spikes=[pygame.image.load('spikes.png')]
bg1=pygame.image.load('Green_Hill_Zone2.png')
Keys=pygame.image.load('Key.png')
bg3=[pygame.image.load('snow1.png'),pygame.image.load('snow2.png'),pygame.image.load('snow3.png'),pygame.image.load('snow4.png'),pygame.image.load('snow5.png')]
bg1=pygame.transform.scale(bg1,(screenWidth+screenWidth+screenWidth+screenWidth+screenWidth-48,screenHeight))

CurrentScore=0
Stats=open("TEST SCORE.txt","r")
lines=Stats.readlines()
TimesPlayed=lines[1][24]
TimesPlayed=int(TimesPlayed)

if TimesPlayed>=1:
    TimesPlayed=str(TimesPlayed)
    Stats=open("TEST SCORE.txt","r")
    lines=Stats.readlines()
    HighScore=lines[0][11]
    if lines[0][12] !=  " ":
        HighScore=HighScore+lines[0][12]
    if lines[1][25] !=" ":
        TimesPlayed=TimesPlayed+lines[1][25]
        if lines[1][26] !=" ":
            TimesPlayed=TimesPlayed+lines[1][26]
    KeysCollected=lines[2][26]
    if lines[2][27] !=" ":
        KeysCollected=KeysCollected+lines[2][27]
    PlayTime=lines[3][17]
    if lines[3][18]!=" " and lines[3][18]!=".":
        PlayTime=PlayTime+lines[3][18]
        if lines[3][19]!=" " and lines[3][19]!=".":
            PlayTime=PlayTime+lines[3][19]
    print(TimesPlayed,"TIMES PLAYED TEST 2")
else:
    HighScore=0
    KeysCollected=0

HighScore=int(HighScore)
KeysCollected=int(KeysCollected)
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
AXE=True
METEOR=True
walkCount=0
snowCount=0
spinCount=0
slideCount=0
fbCount=0
axeCount=0
meteorCount=0
targetCount=0
explosionCount=0
i=0
n=0
obstaclemove=-500
obstaclemovefb=-500
axemove=-500
keymove=-500
meteormoveX= 800
meteormoveY= 0

def retry():
    global obstaclemove,obstaclemovefb,axemove,meteormoveY,meteormoveX,meteorCount,X,Y,Run,isJump,jumpCount,playerposX,KeysCollected,CurrentScore,HighScore,TimesPlayed,PlayTime,keymove
    isJump=False
    Run=False
    X=300
    Y=380
    playerposX=0
    meteormoveY=-500
    meteormoveX=-500
    obstaclemove=-500
    obstaclemovefb=-500
    keymove=-500
    axemove=-500
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
        Stats=open("TEST SCORE.txt","w+")
        Stats.write("HighScore: "+str(HighScore)+"           "+"\n")
        Stats.write("Number of times played: "+str(TimesPlayed)+"          "+"\n")
        Stats.write("Number of Keys collected: "+str(KeysCollected)+"           "+"\n")
        Stats.write("Total Play Time: "+str(PlayTime/15)+"           "+"\n")
        Stats.close()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                while event.key==pygame.K_c:
                    CurrentScore=0
                    Run=True
                    gameStart=True
                    jumpCount=10
                    gameLoop()

def gameLoop():
    global isJump,Run,Y,X,jumpCount,i,n,obstaclemove,obstaclemovefb,axemove,meteorY,meteorX,playerposX,CurrentScore,HighScore,KeysCollected,PlayTime,TimesPlayed
    
    def obstacle():
        global obstaclemove,obstaclemovefb,meteormoveY,meteormoveX,meteorCount,axemove,spinCount,fbCount,axeCount,targetCount,explosionCount,HighScore,TimesPlayed,KEY,keymove,KeysCollected
        
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
        if KEY:
            window.blit(Keys,(keymove,400))
        if axeCount +1>=16:
            axeCount=0
        if AXE:
            axe=window.blit(Axe[axeCount//1],(axemove,-15))
            axeCount +=1
        if meteorCount +1>8:
            meteorCount=0
        if targetCount +1>16:
            targetCount=0
        if METEOR:
            window.blit(Spikes,(obstaclemove,400))
            meteor=window.blit(Meteor[meteorCount//2],(meteormoveX,meteormoveY))
            Target=window.blit(target[targetCount//1],(210,400))
            targetCount +=1
            meteorCount +=1
            if meteormoveY>=380 and meteormoveX<=300:
                meteorCount=8
                if meteorCount +1>10:
                    meteorCount +=1
                    if meteorCount==10:
                        meteormoveY=0
                        meteormoveX=800
            
        obstaclemove=obstaclemove-1
        obstaclemovefb=obstaclemovefb-100
        keymove=keymove-50
        axemove=axemove-20
        meteormoveX=meteormoveX-59
        meteormoveY=meteormoveY+60
        
        if screenWidth+obstaclemove<=0:
            obstacleplacement=random.randint(screenWidth,screenWidth+screenWidth)
            obstaclemove=obstacleplacement

        if obstaclemovefb<=320 and obstaclemovefb>=220 and Y<=233 or obstaclemove<=330 and obstaclemove>=220 and Y<=400 and Y>=380:
            TimesPlayed=int(TimesPlayed)
            TimesPlayed=TimesPlayed+1
            print(TimesPlayed)
            if CurrentScore>HighScore:
                HighScore=CurrentScore
            retry()
        if keymove<=330 and 290<=keymove and Y>=380:
            KeysCollected=int(KeysCollected)
            KeysCollected=KeysCollected+1
            keymove=-500
        
        obstaclemove=obstaclemove-50
        while screenWidth+obstaclemove<=0 and screenWidth+obstaclemovefb<=0 and screenWidth+keymove<=0 and screenWidth+axemove<=0:
            obstacleplacement=random.randint(screenWidth,screenWidth+screenWidth)
            obstaclemove=obstacleplacement
            obstacleplacementfb=random.randint(screenWidth,screenWidth+screenWidth)
            obstaclemovefb=obstacleplacementfb
            keyplacement=random.randint(screenWidth,screenWidth+500)
            keymove=keyplacement
            axeplacement=random.randint(screenWidth,screenWidth)
            axemove=axeplacement
            meteorplacementX=800
            meteorplacementY=0
            meteormoveX=meteorplacementX
            meteormoveY=meteorplacementY

    def BackgroundChange0():
        global n
        window.blit(bg1,[n,0])
        n=n-15
        window.blit(bg1,[screenWidth+screenWidth+screenWidth+screenWidth+screenWidth+n,0])
        n=n-50
            
        if screenWidth+screenWidth+screenWidth+screenWidth+screenWidth+n<=0:
            n=0

    def redrawGameWindow():
        global walkCount,jumpCount,i,Slide,playerposX
        
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
                PlayTime=PlayTime+1
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
                clock.tick(15)
                redrawGameWindow()
                BackgroundChange0()
                obstacle()
                HighScore=int(HighScore)
                TimesPlayed=int(TimesPlayed)
                print(TimesPlayed,"TIMES PLAYED TEST 9")
                if n==0:
                    CurrentScore=CurrentScore+1
                    if CurrentScore>HighScore:
                        HighScore=CurrentScore
                Stats=open("TEST SCORE.txt","w+")
                Stats.write("HighScore: "+str(HighScore)+"           "+"\n")
                Stats.write("Number of times played: "+str(TimesPlayed)+"          "+"\n")
                Stats.write("Number of Keys collected: "+str(KeysCollected)+"           "+"\n")
                Stats.write("Total Play Time: "+str(PlayTime/15)+"           "+"\n")
                Stats.close()
            pygame.quit()
            quit()

gameLoop()
