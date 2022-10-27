###########IMPORTING##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
import pygame
import time
import random
pygame.init()
###########WINDOW CREATION############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
screenWidth=800
screenHeight=600
window=pygame.display.set_mode([screenWidth,screenHeight])
pygame.display.set_caption("ENDLESS")
black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)
red=(255,0,0)
###########SPRITE IMAGES##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
runRight=[pygame.image.load('sonic run 1 flip.gif'),pygame.image.load('sonic run 2 flip.gif'),pygame.image.load('sonic run 3 flip.gif'),pygame.image.load('sonic run 4 flip.gif'),pygame.image.load('sonic run 5 flip.gif'),pygame.image.load('sonic run 6 flip.gif')]
Jump=[pygame.image.load('Spin1.gif'),pygame.image.load('Spin2.gif'),pygame.image.load('Spin3.gif'),pygame.image.load('Spin4.gif')]
Fireball=[pygame.image.load('fireball1.png'),pygame.image.load('fireball2.png'),pygame.image.load('fireball3.png'),pygame.image.load('fireball4.png'),pygame.image.load('fireball5.png')]
saw=[pygame.image.load('saw1.png'),pygame.image.load('saw2.png'),pygame.image.load('saw3.png'),pygame.image.load('saw4.png'),pygame.image.load('saw5.png'),pygame.image.load('saw6.png'),pygame.image.load('saw7.png')]
Axe=[pygame.image.load('axe1.png'),pygame.image.load('axe2 s.png'),pygame.image.load('axe2.png'),pygame.image.load('axe3 s.png'),pygame.image.load('axe3.png'),pygame.image.load('axe4 s.png'),pygame.image.load('axe4.png'),pygame.image.load('axe5 s.png'),pygame.image.load('axe5.png'),pygame.image.load('axe5 s.png'),pygame.image.load('axe4.png'),pygame.image.load('axe4 s.png'),pygame.image.load('axe3.png'),pygame.image.load('axe3 s.png'),pygame.image.load('axe2.png'),pygame.image.load('axe2 s.png')]
target=[pygame.image.load('Target1.png'),pygame.image.load('Target2.png'),pygame.image.load('Target3.png'),pygame.image.load('Target4.png')]
Meteor=[pygame.image.load('Meteor1.png'),pygame.image.load('Meteor2.png'),pygame.image.load('Meteor3.png'),pygame.image.load('Meteor4.png'),pygame.image.load('Meteor5.png'),pygame.image.load('Meteor6.png'),pygame.image.load('Meteor7.png')]#,pygame.image.load('Meteor8.png')]
Boom=[pygame.image.load('Explosion1.gif'),pygame.image.load('Explosion2.gif'),pygame.image.load('Explosion3.gif'),pygame.image.load('Explosion4.gif'),pygame.image.load('Explosion5.gif'),pygame.image.load('Explosion6.gif'),pygame.image.load('Explosion7.gif'),pygame.image.load('Explosion8.gif'),pygame.image.load('Explosion9.gif'),pygame.image.load('Explosion10.gif'),pygame.image.load('Explosion11.gif'),pygame.image.load('Explosion12.gif'),pygame.image.load('Explosion13.gif'),pygame.image.load('Explosion14.gif')]
bg1=pygame.image.load('Green_Hill_Zone2.png')
#Waterfall=[pygame.image.load('Waterfall1.png'),pygame.image.load('Waterfall2.png')]
Keys=pygame.image.load('Key.png')
bg3=[pygame.image.load('snow1.png'),pygame.image.load('snow2.png'),pygame.image.load('snow3.png'),pygame.image.load('snow4.png'),pygame.image.load('snow5.png')]
bg1=pygame.transform.scale(bg1,(screenWidth+screenWidth+screenWidth+screenWidth+screenWidth-48,screenHeight))
###########LOADING AND SETTING STATISTICS#############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
CurrentScore=0
Stats=open("TEST obstacle.txt","r")
lines=Stats.readlines()
TimesPlayed=lines[1][24]
TimesPlayed=int(TimesPlayed)
if TimesPlayed>=1:
    TimesPlayed=str(TimesPlayed)
    Stats=open("TEST obstacle.txt","r")
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
else:
    HighScore=0
    KeysCollected=0
###########INITIALISING##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
HighScore=int(HighScore)
KeysCollected=int(KeysCollected)
PlayTime=int(PlayTime)
TimesPlayed=int(TimesPlayed)
X=300
Y=380
playerposX=300
clock=pygame.time.Clock()
isJump=False
Run=True
Slide=False
Obstacle=True
jumpCount=10
walkCount=0
snowCount=0
spinCount=0
slideCount=0
fbCount=0
axeCount=0
meteorCount=0
targetCount=0
boomCount=0
waterfallCount=0
i=0
n=0
j=0
MeteorX=29
MeteorY=30
AxeX=30
SawX=30
FireballX=30
obstaclemove=800
obstaclemovefb=800
axemove=800
keymove=800
meteormoveX= 800
meteormoveY= 0
SETS=0
SETCHOOSER=random.randint(0,100)
###########GAME OVER SCREEN AND UPDATING THE STATISTICS END GAME AND QUIT OR PLAY-AGAIN##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
def retry():
    global SETCHOOSER,obstaclemove,obstaclemovefb,axemove,meteormoveY,meteormoveX,meteorCount,X,Y,Run,isJump,jumpCount,playerposX,KeysCollected,CurrentScore,HighScore,TimesPlayed,PlayTime,keymove
    isJump=False
    Run=False
    X=300
    Y=380
    playerposX=0
    meteormoveY=0
    meteormoveX=800
    obstaclemove=800
    obstaclemovefb=800
    keymove=800
    axemove=800
    AxeX=0
    SawX=0
    MeteorX=0
    MeteorY=0
    FireballX=0
    SETCHOOSER=random.randint(0,100)
    pygame.font.init()
    header=pygame.font.SysFont(None,140)
    font=pygame.font.SysFont(None,55)#55 is the size of the font
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
        Stats=open("TEST obstacle.txt","w+")
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
###########GAMEPLAY LOOP######################################################################################################################################################################################
def gameLoop():
    global isJump,Run,Y,X,jumpCount,i,n,j,obstaclemove,obstaclemovefb,axemove,meteorY,meteorX,playerposX,CurrentScore,HighScore,KeysCollected,PlayTime,TimesPlayed,Slide,slideCount,slideRepeat
###########SAW SPRITE ANIMATION###############################################################################################################################################################################    
    def SAW():
        global obstaclemove,spinCount,TimesPlayed,SawX
        if spinCount +1>=7:
            spinCount=0
        if Obstacle:
            Saw=window.blit(saw[spinCount//2],(obstaclemove,400))
            spinCount +=1
            obstaclemove=obstaclemove-SawX
        while screenWidth+obstaclemove<=0:
            obstacleplacement=random.randint(screenWidth,screenWidth+screenWidth)
            obstaclemove=obstacleplacement
###########SAW SPRITE ANIMATION FOR A SPECIFIC SET######################################################################################################################################################################################
    def SAW_SETS():
        global obstaclemove,spinCount,TimesPlayed,SawX
        if spinCount +1>=7:
            spinCount=0
        if Obstacle:
            Saw=window.blit(saw[spinCount//2],(obstaclemove,400))
            spinCount +=1
            obstaclemove=obstaclemove-SawX
        while screenWidth+obstaclemove<=0:
            obstacleplacement=random.randint(screenWidth,screenWidth+10)
            obstaclemove=obstacleplacement
###########AXE SPRITE ANIMATION######################################################################################################################################################################################
    def AXE():
        global axemove,axeCount,TimesPlayed,AxeX
        if axeCount +1>=16:
            axeCount=0
        if Obstacle:
            axe=window.blit(Axe[axeCount//1],(axemove,-15))
            axeCount +=1
        axemove=axemove-AxeX
        while screenWidth+axemove-30<=0:
            axeplacement=random.randint(screenWidth,screenWidth)
            axemove=axeplacement
###########FIREBALL SPRITE ANIMATION######################################################################################################################################################################################
    def FIREBALL():
        global obstaclemovefb,fbCount,TimesPlayed,FireballX
        if fbCount +1>=4:
            fbCount=0
        if Obstacle:
            fireball=window.blit(Fireball[fbCount//2],(obstaclemovefb,200))
            fbCount +=1
        obstaclemovefb=obstaclemovefb-FireballX
        while screenWidth+obstaclemovefb<=0:
            obstacleplacementfb=random.randint(screenWidth,screenWidth+screenWidth)
            obstaclemovefb=obstacleplacementfb
###########FIREBALL SPRITE ANIMATION FOR A SPECIFIC SET######################################################################################################################################################################################
    def FIREBALL_SETS():
        global obstaclemovefb,fbCount,TimesPlayed,FireballX
        if fbCount +1>=4:
            fbCount=0
        if Obstacle:
            fireball=window.blit(Fireball[fbCount//2],(obstaclemovefb,200))
            fbCount +=1
        obstaclemovefb=obstaclemovefb-FireballX
        while screenWidth+obstaclemovefb<=0:
            obstacleplacementfb=random.randint(screenWidth,screenWidth+20)
            obstaclemovefb=obstacleplacementfb
###########METEOR AND EXPLOSION SPRITE ANIMATIONS######################################################################################################################################################################################
    def METEOR():
        global meteormoveY,meteormoveX,meteorCount,targetCount,explosionCount,TimesPlayed,boomCount,MeteorX,MeteorY
        if meteorCount +1>8:
            meteorCount=0
        if targetCount +1>4:
            targetCount=0
        if boomCount +1>14:
            boomCount =0
        if Obstacle:
            meteor=window.blit(Meteor[meteorCount//2],(meteormoveX,meteormoveY))
            Target=window.blit(target[targetCount//1],(300,400))
            targetCount +=1
            meteorCount +=1
            meteormoveX=meteormoveX-MeteorX
            meteormoveY=meteormoveY+MeteorY
            if meteormoveY>=380 and meteormoveX<=300 and boomCount!=14:
                for boomCount in range(13):
                    boom=window.blit(Boom[boomCount//1],(200,340))
                    boomCount=boomCount+1
                    meteormoveY=-50
                    meteormoveX=850
            boomCount=0
###########KEY SPRITE ANIMATION######################################################################################################################################################################################            
    def KEY():
        global Key,keymove,KeysCollected
        if Obstacle:
            window.blit(Keys,(keymove,400))
        keymove=keymove-50
        if keymove<=330 and 290<=keymove and Y>=380:
            KeysCollected=int(KeysCollected)
            KeysCollected=KeysCollected+1
            keymove=-500
        while screenWidth+keymove<=0:
            keyplacement=random.randint(screenWidth,screenWidth+20)
            keymove=keyplacement
###########WATERFALL SPRITE ANIMATION######################################################################################################################################################################################
    def WATERFALL():
        global waterfallCount
        if waterfallCount +1>2:
            waterfallCount=0
        if Obstacle:
            waterfall=window.blit(Waterfall[waterfallCount//2],(500,518))
            waterfallCount +=1
###########OBSTACLE SETS AND RANDOM GENERATION######################################################################################################################################################################################
    def obstacle():
        global SETS
        global SETCHOOSER
        global axemove
        global obstaclemove
        global obstaclemovefb
        global TimesPlayed
        global meteormoveX
        global meteormoveY
        KEY()
        SETS=SETS+1
        if SETS>=100 and SETCHOOSER<25 and obstaclemove<=0 and obstaclemovefb<=0:
            SETCHOOSER=random.randint(0,100)
            SETS=0
        if SETS>=100 and SETCHOOSER>24 and SETCHOOSER<50 and axemove<=-20:
            SETCHOOSER=random.randint(0,100)
            SETS=0
        if SETS>=10 and SETCHOOSER>49 and SETCHOOSER<75 and meteormoveX>=800 and boomCount==0:
            SETCHOOSER=random.randint(0,100)
            SETS=0
        if SETS>=100 and SETCHOOSER>74 and obstaclemove<=0:
            SETCHOOSER=random.randint(0,100)
            SETS=0
        if SETCHOOSER<25:
            SAW_SETS()
            FIREBALL_SETS()
            axemove=800
        if SETCHOOSER>24 and SETCHOOSER<50:
            AXE()
            obstaclemovefb=800
            obstaclemove=800
        if SETCHOOSER>49 and SETCHOOSER<75:
            METEOR()
            axemove=800
            obstaclemovefb=800
            obstaclemove=800
        if SETCHOOSER>74:
            SAW()
            axemove=800
            obstaclemovefb=800
        if obstaclemovefb<=320 and obstaclemovefb>=220 and Y<=233 or obstaclemove<=330 and obstaclemove>=220 and Y<=400 and Y>=380 or axemove<=320 and axemove>=270 and Y<=380 or meteormoveX<=320 and Y>360:
            TimesPlayed=int(TimesPlayed)
            TimesPlayed=TimesPlayed+1
            retry()
###########BACKGROUND ANIMATION AND SETTINGS######################################################################################################################################################################################                    
    def BackgroundChange0():
        global n,MeteorX,MeteorY,SawX,FireballX,AxeX
        window.blit(bg1,[n,0])
        n=n-15
        window.blit(bg1,[screenWidth+screenWidth+screenWidth+screenWidth+screenWidth+n,0])
        n=n-50
        if screenWidth+screenWidth+screenWidth+screenWidth+screenWidth+n<=0:
            n=0
            MeteorX=MeteorX+1
            MeteorY=MeteorY+1
            SawX=SawX+1
            FireballX=FireballX+1
            AxeX=AxeX+1
###########CHARACTER ANIMATION#######################################################################################################################################################################################
    def redrawGameWindow():
        global walkCount,jumpCount,i,Slide,playerposX,slideCount,isJump
        if walkCount +1>=12:
            walkCount=0
        if Run:
            window.blit(runRight[walkCount//2],(playerposX,380))
            walkCount +=1
        if isJump:
            window.blit(Jump[i],(X,Y))
        if Slide:
            window.blit(Jump[j],(X,Y))
        pygame.display.update()
###########GAME BUILD UP######################################################################################################################################################################################
    gameStart=True
    gameRun=False
    Slide=False
    while gameStart:
        playerposX=0
        while playerposX<300:
            playerposX=playerposX+5
            redrawGameWindow()
            BackgroundChange0()
            clock.tick(15)
        else:
###########GAME START######################################################################################################################################################################################            
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
###########SLIDE######################################################################################################################################################################################
                if not (Slide) and Y>=380:    
                    if keys[pygame.K_DOWN]:
                        isJump=False
                        Run=False
                        Slide=True
                        walkCount=0
                        slideCount=0
                else:
                    if Y>=380:                            
                        if slideCount>=-10:
                            neg=1
                            if slideCount<10:
                                neg=-1
                            Y=400
                            j=j+1
                            if j>=4:
                                j=0
                            slideCount -=1
                        else:
                            isJump=False
                            Run=True
                            Slide=False
                            Y=380
                            jumpCount=10
                            j=0
                            playerposY=400
                            slideCount=0
###########JUMP######################################################################################################################################################################################
                if not (isJump):    
                    if keys[pygame.K_SPACE]:
                        isJump=True
                        Run=False
                        Slide=False
                        walkCount=0
                        slideCount=0
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
                        Slide=False
                        Run=True
                        jumpCount=10
                        i=0
############CALLING THE PROCEDURES#####################################################################################################################################################################################                        
                clock.tick(15)
                redrawGameWindow()
                BackgroundChange0()
                obstacle()
                print(Y," Y COORDINATE")
############UPDATING THE STATISTICS MID GAME#####################################################################################################################################################################################
                HighScore=int(HighScore)
                TimesPlayed=int(TimesPlayed)
                if n==0:
                    CurrentScore=CurrentScore+1
                    if CurrentScore>HighScore:
                        HighScore=CurrentScore
                Stats=open("TEST Obstacle.txt","w+")
                Stats.write("HighScore: "+str(HighScore)+"           "+"\n")
                Stats.write("Number of times played: "+str(TimesPlayed)+"          "+"\n")
                Stats.write("Number of Keys collected: "+str(KeysCollected)+"           "+"\n")
                Stats.write("Total Play Time: "+str(PlayTime/15)+"           "+"\n")
                Stats.close()
            pygame.quit()
            quit()
gameLoop()
