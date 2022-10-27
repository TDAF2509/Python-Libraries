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
saw1move=800
fireballmove=800
axemove=800
keymove=800
meteormoveX= 800
meteormoveY= 0
jh=0
###########LEVEL SELECTION###################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
level=(input("please select a level"))
level=int(level)
if level==1:
    saw1move=800
    fireballmove=800
if level==2:
    axemove=800
    saw1move=1200
if level==3:
    saw1move=800
    saw2move=1100
    saw3move=1400
    saw4move=1700
###########GAME OVER SCREEN AND UPDATING THE STATISTICS END GAME AND QUIT OR PLAY-AGAIN##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
def retry():
    global saw1move,saw2move,saw3move,saw4move,fireballmove,axemove,meteormoveY,meteormoveX,meteorCount,X,Y,Run,isJump,jumpCount,playerposX,KeysCollected,CurrentScore,HighScore,TimesPlayed,PlayTime,keymove
    isJump=False
    Run=False
    X=300
    Y=380
    playerposX=0
    meteormoveY=0
    meteormoveX=800
    saw1move=800
    fireballmove=800
    keymove=800
    axemove=800
    if level==1:
        saw1move=800
        fireballmove=800
    if level==2:
        axemove=800
        saw1move=1200
    if level==3:
        saw1move=800
        saw2move=1100
        saw3move=1400
        saw4move=1700
    AxeX=0
    SawX=0
    MeteorX=0
    MeteorY=0
    FireballX=0
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
                    if level==1:
                        saw1move=800
                        fireballmove=800
                    if level==2:
                        axemove=800
                        saw1move=1200
                    if level==3:
                        saw1move=800
                        saw2move=1100
                        saw3move=1400
                        saw4move=1700                        
                    gameLoop()
###########GAMEPLAY LOOP######################################################################################################################################################################################
def gameLoop():
    global isJump,Run,Y,X,jumpCount,i,n,j,jh,saw1move,saw2move,saw3move,saw4move,fireballmove,axemove,meteorY,meteorX,playerposX,CurrentScore,HighScore,KeysCollected,PlayTime,TimesPlayed,Slide,slideCount
###########SAW SPRITE ANIMATION###############################################################################################################################################################################    
    def SAW():
        global saw1move,spinCount,TimesPlayed,SawX
        if spinCount +1>=7:
            spinCount=0
        if Obstacle:
            Saw=window.blit(saw[spinCount//2],(saw1move,400))
            spinCount +=1
            saw1move=saw1move-SawX
        while screenWidth+saw1move<=0:
            obstacleplacement=random.randint(screenWidth,screenWidth+screenWidth)
            saw1move=obstacleplacement
        #if saw1move<=330 and saw1move>=220 and Y<=400 and Y>=380:
        #    TimesPlayed=int(TimesPlayed)
        #    TimesPlayed=TimesPlayed+1
         #   retry()
###########SAW SPRITE ANIMATION FOR A SPECIFIC SET######################################################################################################################################################################################
    def SAW_SETS():
        global saw1move,spinCount,TimesPlayed,SawX
        if spinCount +1>=7:
            spinCount=0
        if Obstacle:
            Saw=window.blit(saw[spinCount//2],(saw1move,400))
            spinCount +=1
            saw1move=saw1move-SawX
        while screenWidth+saw1move<=0:
            saw1move=800
        #if saw1move<=330 and saw1move>=220 and Y<=400 and Y>=380:
        #    TimesPlayed=int(TimesPlayed)
        #    TimesPlayed=TimesPlayed+1
        #    retry()
        #    saw1move=800
###########SAW SPRITE ANIMATION FOR A SPECIFIC SET######################################################################################################################################################################################
    def SAW_SETS2():
        global saw2move,spinCount,TimesPlayed,SawX
        if spinCount +1>=7:
            spinCount=0
        if Obstacle:
            Saw=window.blit(saw[spinCount//2],(saw2move,400))
            spinCount +=1
            saw2move=saw2move-SawX
        while screenWidth+saw2move<=0:
            saw2move=800
        #if saw2move<=330 and saw2move>=220 and Y<=400 and Y>=380:
        #    TimesPlayed=int(TimesPlayed)
        #    TimesPlayed=TimesPlayed+1
        #    retry()
        #    saw2move=1100
###########SAW SPRITE ANIMATION FOR A SPECIFIC SET######################################################################################################################################################################################
    def SAW_SETS3():
        global saw3move,spinCount,TimesPlayed,SawX
        if spinCount +1>=7:
            spinCount=0
        if Obstacle:
            Saw=window.blit(saw[spinCount//2],(saw3move,400))
            spinCount +=1
            saw3move=saw3move-SawX
        while screenWidth+saw3move<=0:
            saw3move=800
        #if saw3move<=330 and saw3move>=220 and Y<=400 and Y>=380:
        #    TimesPlayed=int(TimesPlayed)
        #    TimesPlayed=TimesPlayed+1
        #    retry()
        #    saw3move=1400
###########SAW SPRITE ANIMATION FOR A SPECIFIC SET######################################################################################################################################################################################
    def SAW_SETS4():
        global saw4move,spinCount,TimesPlayed,SawX
        if spinCount +1>=7:
            spinCount=0
        if Obstacle:
            Saw=window.blit(saw[spinCount//2],(saw4move,400))
            spinCount +=1
            saw4move=saw4move-SawX
        while screenWidth+saw4move<=0:
            saw4move=800
        #if saw4move<=330 and saw4move>=220 and Y<=400 and Y>=380:
        #    TimesPlayed=int(TimesPlayed)
        #    TimesPlayed=TimesPlayed+1
        #    retry()
        #    saw4move=1700
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
        #if axemove<=320 and axemove>=270 and Y<=380:
        #    TimesPlayed=int(TimesPlayed)
        #    TimesPlayed=TimesPlayed+1
        #    retry()
###########AXE SPRITE ANIMATION FOR A SPECIFIC SET######################################################################################################################################################################################
    def AXE_SET():
        global axemove,axeCount,TimesPlayed,AxeX
        if axeCount +1>=16:
            axeCount=0
        if Obstacle:
            axe=window.blit(Axe[axeCount//1],(axemove,-15))
            axeCount +=1
        axemove=axemove-AxeX
        while screenWidth+axemove-30<=0:
            axemove=800
        #if axemove<=320 and axemove>=270 and Y<=380:
        #    TimesPlayed=int(TimesPlayed)
        #    TimesPlayed=TimesPlayed+1
        #    retry()
###########FIREBALL SPRITE ANIMATION######################################################################################################################################################################################
    def FIREBALL():
        global fireballmove,fbCount,TimesPlayed,FireballX
        if fbCount +1>=4:
            fbCount=0
        if Obstacle:
            fireball=window.blit(Fireball[fbCount//2],(fireballmove,200))
            fbCount +=1
        fireballmove=fireballmove-FireballX
        while screenWidth+fireballmove<=0:
            fbplacement=random.randint(screenWidth,screenWidth+screenWidth)
            fireballmove=fbplacement
        #if fireballmove<=320 and fireballmove>=220 and Y<=233:
        #    TimesPlayed=int(TimesPlayed)
        #    TimesPlayed=TimesPlayed+1
        #    retry()
###########FIREBALL SPRITE ANIMATION FOR A SPECIFIC SET######################################################################################################################################################################################
    def FIREBALL_SETS():
        global fireballmove,fbCount,TimesPlayed,FireballX
        if fbCount +1>=4:
            fbCount=0
        if Obstacle:
            fireball=window.blit(Fireball[fbCount//2],(fireballmove,200))
            fbCount +=1
        fireballmove=fireballmove-FireballX
        while screenWidth+fireballmove<=0:
            fbplacement=random.randint(screenWidth,screenWidth+20)
            fireballmove=fbplacement
        #if fireballmove<=320 and fireballmove>=220 and Y<=233:
        #    TimesPlayed=int(TimesPlayed)
        #    TimesPlayed=TimesPlayed+1
        #    retry()
        #    fireballmove=800
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
        #if meteormoveX<=320 and Y>360:
        #    TimesPlayed=int(TimesPlayed)
        #    TimesPlayed=TimesPlayed+1
        #    retry()
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
        global axemove,saw1move,fireballmove,meteormoveX,meteormoveY,TimesPlayed,level
        level=int(level)
        KEY()
        if level==1:
            FIREBALL_SETS()
            SAW_SETS()
            axemove=800
        if level==2:
            AXE_SET()
            SAW_SETS()
            fireballmove=800
        if level==3:
            SAW_SETS()
            SAW_SETS2()
            SAW_SETS3()
            SAW_SETS4()
            axemove=800
            fireballmove=800
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
                if event.type==pygame.KEYDOWN:
                    if not (isJump):
                        jh=jh+1
                        if keys[pygame.K_SPACE]:
                            isJump=True
                            Run=False
                            Slide=False
                            walkCount=0
                            slideCount=0
                            print(jh," Jump Height")
                if event.type==pygame.KEYUP and jh<5:
                    if jumpCount>=-10:
                        neg=1
                        if jumpCount<0:
                            neg=-1
                        Y -=(jumpCount**2)*0.25*neg
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
                if event.type==pygame.KEYUP and jh>5:
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
############UPDATING THE STATISTICS MID GAME#####################################################################################################################################################################################
                HighScore=int(HighScore)
                TimesPlayed=int(TimesPlayed)
                if n==0:
                    CurrentScore=CurrentScore+1
                    if CurrentScore>HighScore:
                        HighScore=CurrentScore
            pygame.quit()
            quit()
gameLoop()
