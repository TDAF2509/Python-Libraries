###########IMPORTING##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
import pygame
import time
import random
pygame.init()
file1=open("Usernames.txt","a+")
file1.write("\n")
file1.close()
file1=open("Usernames.txt","r")
AccountNames=file1.readlines()
file1.close()
file=open("Password.txt","a+")
file.write("\n")
file.close()
file=open("Password.txt","r")
AccountPasswords=file.readlines()
file.close()
###########WINDOW CREATION############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
screenWidth=800
screenHeight=600
pygame.display.set_caption("ENDLESS")
black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)
red=(255,0,0)
gold=(255,212,0)
grey=(100,100,100)
Lblue=(70,255,245)
Lgold=(255,230,107)
Lred=(252,45,45)
Lgreen=(125,255,90)
###########SPRITE IMAGES##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
runRight=[pygame.image.load('sonic run 1 flip.gif'),pygame.image.load('sonic run 2 flip.gif'),pygame.image.load('sonic run 3 flip.gif'),pygame.image.load('sonic run 4 flip.gif'),pygame.image.load('sonic run 5 flip.gif'),pygame.image.load('sonic run 6 flip.gif')]
Jump=[pygame.image.load('Spin1.gif'),pygame.image.load('Spin2.gif'),pygame.image.load('Spin3.gif'),pygame.image.load('Spin4.gif')]
Fireball=[pygame.image.load('fireball1.png'),pygame.image.load('fireball2.png'),pygame.image.load('fireball3.png'),pygame.image.load('fireball4.png'),pygame.image.load('fireball5.png')]
saw=[pygame.image.load('saw1.png'),pygame.image.load('saw2.png'),pygame.image.load('saw3.png'),pygame.image.load('saw4.png'),pygame.image.load('saw5.png'),pygame.image.load('saw6.png'),pygame.image.load('saw7.png')]
Axe=[pygame.image.load('axe1.png'),pygame.image.load('axe2 s.png'),pygame.image.load('axe2.png'),pygame.image.load('axe3 s.png'),pygame.image.load('axe3.png'),pygame.image.load('axe4 s.png'),pygame.image.load('axe4.png'),pygame.image.load('axe5 s.png'),pygame.image.load('axe5.png'),pygame.image.load('axe5 s.png'),pygame.image.load('axe4.png'),pygame.image.load('axe4 s.png'),pygame.image.load('axe3.png'),pygame.image.load('axe3 s.png'),pygame.image.load('axe2.png'),pygame.image.load('axe2 s.png')]
target=[pygame.image.load('Target1.png'),pygame.image.load('Target2.png'),pygame.image.load('Target3.png'),pygame.image.load('Target4.png')]
Meteor=[pygame.image.load('Meteor1.png'),pygame.image.load('Meteor2.png'),pygame.image.load('Meteor3.png'),pygame.image.load('Meteor4.png'),pygame.image.load('Meteor5.png'),pygame.image.load('Meteor6.png'),pygame.image.load('Meteor7.png')]#,pygame.image.load('Meteor8.png')]
Boom=[pygame.image.load('Explosion1.gif'),pygame.image.load('Explosion2.gif'),pygame.image.load('Explosion3.gif'),pygame.image.load('Explosion4.gif'),pygame.image.load('Explosion5.gif'),pygame.image.load('Explosion6.gif'),pygame.image.load('Explosion7.gif'),pygame.image.load('Explosion8.gif'),pygame.image.load('Explosion9.gif'),pygame.image.load('Explosion10.gif'),pygame.image.load('Explosion11.gif'),pygame.image.load('Explosion12.gif'),pygame.image.load('Explosion13.gif'),pygame.image.load('Explosion14.gif')]
#bg1=pygame.image.load('bg4now.png')
#bg2=pygame.image.load('Beachbg.png')
bg3=pygame.image.load('canyonbg.png')
#bg4=pygame.image.load('Sandbg.png')
bg5=pygame.image.load('Green_Hill_Zone2.png')
#bg6=pygame.image.load('040.png')
EndlessTXT=pygame.image.load('Endless text.png')
LevelsTXT=pygame.image.load('Levels text.png')
ShopTXT=pygame.image.load('Shop text.png')
BackTXT=pygame.image.load('Back text.png')
StatsTXT=pygame.image.load('Statistics text.png')
oneTXT=pygame.image.load('1TEXT.png')
twoTXT=pygame.image.load('2TEXT.png')
threeTXT=pygame.image.load('3TEXT.png')
fourTXT=pygame.image.load('4TEXT.png')
fiveTXT=pygame.image.load('5TEXT.png')
sixTXT=pygame.image.load('6TEXT.png')
sevenTXT=pygame.image.load('7TEXT.png')
eightTXT=pygame.image.load('8TEXT.png')
nineTXT=pygame.image.load('9TEXT.png')
#Waterfall=[pygame.image.load('Waterfall1.png'),pygame.image.load('Waterfall2.png')]
Keys=pygame.image.load('Key.png')
#bg3=[pygame.image.load('snow1.png'),pygame.image.load('snow2.png'),pygame.image.load('snow3.png'),pygame.image.load('snow4.png'),pygame.image.load('snow5.png')]
#bg1=pygame.transform.scale(bg1,(screenWidth+screenWidth+screenWidth+screenWidth+screenWidth-48,screenHeight))
#bg2=pygame.transform.scale(bg2,(screenWidth+screenWidth+screenWidth+screenWidth+screenWidth-48,screenHeight))
bg3=pygame.transform.scale(bg3,(screenWidth+screenWidth+screenWidth+screenWidth+screenWidth-48,screenHeight))
#bg4=pygame.transform.scale(bg4,(screenWidth+screenWidth+screenWidth+screenWidth+screenWidth-48,screenHeight))
bg5=pygame.transform.scale(bg5,(screenWidth+screenWidth+screenWidth+screenWidth+screenWidth-48,screenHeight))
#bg6=pygame.transform.scale(bg6,(screenWidth+screenWidth+screenWidth+screenWidth+screenWidth-48,screenHeight))
###########INITIALISING##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
gameX=300
gameY=380
playerposX=300
clock=pygame.time.Clock()
isJump=False
Run=True
Slide=False
Obstacle=True
endless=False
levels=False
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
sawmove=800
fireballmove=800
axemove=800
keymove=800
meteormoveX= 800
meteormoveY= 0
SETS=0
SETCHOOSER=random.randint(0,100)
###########GAME OVER SCREEN AND UPDATING THE STATISTICS END GAME AND QUIT OR PLAY-AGAIN##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
def retry():
    global SETCHOOSER,window,sawmove,fireballmove,axemove,meteormoveY,meteormoveX,meteorCount,gameX,gameY,Run,isJump,jumpCount,playerposX,KeysCollected,CurrentScore,HighScore,TimesPlayed,PlayTime,keymove,levels,saw1move,saw2move,saw3move,saw4move
    isJump=False
    Run=False
    if levels: 
        if level==1:
            saw1move=800
            fireballmove=800
        if level==2:
            axemove=800
            saw1move=1200
        if level==3:
            saw1move=800
            saw2move=1200
            saw3move=1600
            saw4move=2000
        if level==4:
            saw1move=800
            axemove=1300
            saw2move=1800
            fireballmove=2200
            meteormoveX=1800
            meteormoveY=-900
    gameX=300
    gameY=380
    playerposX=0
    meteormoveY=0
    meteormoveX=800
    sawmove=800
    fireballmove=800
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
        Stats=open(Username+".txt","w+")
        Stats.write("HighScore: "+str(HighScore)+"           "+"\n")
        Stats.write("Number of times played: "+str(TimesPlayed)+"          "+"\n")
        Stats.write("Number of Keys collected: "+str(KeysCollected)+"           "+"\n")
        Stats.write("Total Play Time: "+str(PlayTime/15)+"           "+"\n")
        Stats.close()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.display.quit()
                    Run=True
                    gamestart=True
                    jumpCount=10
                    GUIMainMenu()
                    window=pygame.display.set_mode([1,1])
                while event.key==pygame.K_c:
                    CurrentScore=0
                    axemove=800
                    AxeX=0
                    SawX=0
                    MeteorX=0
                    MeteorY=0
                    FireballX=0
                    Run=True
                    gameStart=True
                    jumpCount=10
                    if levels: 
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
                        if level==4:
                            saw1move=800
                            axemove=1300
                            saw2move=1800
                            fireballmove=2200
                            meteormoveX=1800
                            meteormoveY=-900
                    gameLoop()
###########GAME OVER SCREEN AND UPDATING THE STATISTICS END GAME AND QUIT OR PLAY-AGAIN##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
def complete():
    global SETCHOOSER,window,sawmove,fireballmove,axemove,meteormoveY,meteormoveX,meteorCount,gameX,gameY,Run,isJump,jumpCount,playerposX,KeysCollected,CurrentScore,HighScore,TimesPlayed,PlayTime,keymove,levels,saw1move,saw2move,saw3move,saw4move
    isJump=False
    Run=False
    if levels: 
        if level==1:
            saw1move=800
            fireballmove=800
        if level==2:
            axemove=800
            saw1move=1200
        if level==3:
            saw1move=800
            saw2move=1200
            saw3move=1600
            saw4move=2000
        if level==4:
            saw1move=800
            axemove=1300
            saw2move=1800
            fireballmove=2200
            meteormoveX=1800
            meteormoveY=-900
    gameX=300
    gameY=380
    playerposX=0
    meteormoveY=0
    meteormoveX=800
    sawmove=800
    fireballmove=800
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
    header_text=header.render('LEVEL COMPLETE',False,(240,0,0))
    screen_textRetry=font.render('PRESS c TO PLAY AGAIN OR q TO QUIT',False,(255,0,0))
    gameOver=True
    while gameOver:
        window.fill(black)
        window.blit(header_text,(10,screenHeight/8))
        window.blit(screen_textRetry,(40,screenHeight/2))
        pygame.display.update()
        Stats=open(Username+".txt","w+")
        Stats.write("HighScore: "+str(HighScore)+"           "+"\n")
        Stats.write("Number of times played: "+str(TimesPlayed)+"          "+"\n")
        Stats.write("Number of Keys collected: "+str(KeysCollected)+"           "+"\n")
        Stats.write("Total Play Time: "+str(PlayTime/15)+"           "+"\n")
        Stats.close()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.display.quit()
                    Run=True
                    gamestart=True
                    jumpCount=10
                    GUIMainMenu()
                    window=pygame.display.set_mode([1,1])
                while event.key==pygame.K_c:
                    CurrentScore=0
                    axemove=800
                    AxeX=0
                    SawX=0
                    MeteorX=0
                    MeteorY=0
                    FireballX=0
                    Run=True
                    gameStart=True
                    jumpCount=10
                    if levels: 
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
                        if level==4:
                            saw1move=800
                            axemove=1300
                            saw2move=1800
                            fireballmove=2200
                            meteormoveX=1800
                            meteormoveY=-900
                    gameLoop()                    
###########GAMEPLAY LOOP#################################################################################################################################################################################################################
def gameLoop():
    global isJump,Run,window,gameY,gameX,jumpCount,i,n,j,keymove,sawmove,fireballmove,axemove,meteorY,meteorX,playerposX,CurrentScore,HighScore,KeysCollected,PlayTime,TimesPlayed,Slide,slideCount,slideRepeat,CurrentScore,endless,levels,level,saw2move,saw1move,saw3move,saw4move,meteormoveX,meteormoveY
###########LEVEL SELECTION###################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
    if levels:
        level=int(level)
        if level==1:
            saw1move=800
            fireballmove=800
        if level==2:
            axemove=800
            saw1move=1200
        if level==3:
            saw1move=800
            saw2move=1200
            saw3move=1600
            saw4move=2000
        if level==4:
            saw1move=800
            axemove=1400
            saw2move=1900
            fireballmove=2270
            meteormoveX=2400
            meteormoveY=-1600
###########SAW SPRITE ANIMATION#########################################################################################################################################################################################################
    def SAW():
        global sawmove,spinCount,TimesPlayed,SawX
        if spinCount +1>=7:
            spinCount=0
        if Obstacle:
            Saw=window.blit(saw[spinCount//2],(sawmove,400))
            spinCount +=1
            sawmove=sawmove-SawX
        while screenWidth+sawmove<=0:
            sawplacement=random.randint(screenWidth,screenWidth+screenWidth)
            sawmove=sawplacement
        if sawmove<=330 and sawmove>=220 and gameY<=400 and gameY>=380:
            TimesPlayed=int(TimesPlayed)
            TimesPlayed=TimesPlayed+1
            retry()
###########SAW SPRITE ANIMATION FOR A SPECIFIC SET######################################################################################################################################################################################
    def SAW_SETS():
        global sawmove,spinCount,TimesPlayed,SawX
        if spinCount +1>=7:
            spinCount=0
        if Obstacle:
            Saw=window.blit(saw[spinCount//2],(sawmove,400))
            spinCount +=1
            sawmove=sawmove-SawX
        while screenWidth+sawmove<=0:
            sawplacement=random.randint(screenWidth,screenWidth+10)
            sawmove=sawplacement
        if sawmove<=330 and sawmove>=220 and gameY<=400 and gameY>=380:
            TimesPlayed=int(TimesPlayed)
            TimesPlayed=TimesPlayed+1
            retry()
###########SAW SPRITE ANIMATION FOR A SPECIFIC SET######################################################################################################################################################################################
    def SAW_SETS1():
        global saw1move,spinCount,TimesPlayed,SawX
        if spinCount +1>=7:
            spinCount=0
        if Obstacle:
            Saw=window.blit(saw[spinCount//2],(saw1move,400))
            spinCount +=1
            saw1move=saw1move-SawX
        while screenWidth+saw1move<=0:
            if screenWidth+saw1move<=0 and level==4:
                saw1move=-100
            else:
                saw1move=800
        if saw1move<=330 and saw1move>=220 and gameY<=400 and gameY>=380:
            TimesPlayed=int(TimesPlayed)
            TimesPlayed=TimesPlayed+1
            retry()
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
            if screenWidth+saw2move<=0 and level==4:
                saw2move=-100
            else:
                saw2move=800
        if level==4 and saw2move<=330 and saw2move>=220 and gameY<=400 and gameY>=380:
            TimesPlayed=int(TimesPlayed)
            TimesPlayed=TimesPlayed+1
            retry()
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
        if saw3move<=330 and saw3move>=220 and gameY<=400 and gameY>=380:
            TimesPlayed=int(TimesPlayed)
            TimesPlayed=TimesPlayed+1
            retry()
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
        if saw4move<=330 and saw4move>=220 and gameY<=400 and gameY>=380:
            TimesPlayed=int(TimesPlayed)
            TimesPlayed=TimesPlayed+1
            retry()
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
        if axemove<=320 and axemove>=270 and gameY<=380:
            TimesPlayed=int(TimesPlayed)
            TimesPlayed=TimesPlayed+1
            retry()
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
            if screenWidth+axemove-30<=0 and level==4:
                axemove=-1000
            else:
                axemove=800
        if axemove<=320 and axemove>=270 and gameY<=380:
            TimesPlayed=int(TimesPlayed)
            TimesPlayed=TimesPlayed+1
            retry()
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
            fireballplacement=random.randint(screenWidth,screenWidth+screenWidth)
            fireballmove=fireballplacement
        if fireballmove<=320 and fireballmove>=220 and gameY<=233:
            TimesPlayed=int(TimesPlayed)
            TimesPlayed=TimesPlayed+1
            retry()
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
            fireballplacement=random.randint(screenWidth,screenWidth+20)
            fireballmove=fireballplacement
        if fireballmove<=320 and fireballmove>=220 and gameY<=233:
            TimesPlayed=int(TimesPlayed)
            TimesPlayed=TimesPlayed+1
            retry()
###########FIREBALL SPRITE ANIMATION FOR A SPECIFIC SET######################################################################################################################################################################################
    def FIREBALL_SETS1():
        global fireballmove,fbCount,TimesPlayed,FireballX
        if fbCount +1>=4:
            fbCount=0
        if Obstacle:
            fireball=window.blit(Fireball[fbCount//2],(fireballmove,200))
            fbCount +=1
        fireballmove=fireballmove-FireballX
        while screenWidth+fireballmove<=0:
            if screenWidth+fireballmove<=0 and level==4:
                fireballmove=-100
            else:
                fireballmove=800
        if fireballmove<=320 and fireballmove>=220 and gameY<=233:
            TimesPlayed=int(TimesPlayed)
            TimesPlayed=TimesPlayed+1
            retry()
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
                if meteormoveX<=320 and meteormoveY>=380 and gameY>360:
                    TimesPlayed=int(TimesPlayed)
                    TimesPlayed=TimesPlayed+1
                    retry()
                meteormoveY=-50
                meteormoveX=850
            boomCount=0
            
###########METEOR AND EXPLOSION SPRITE FOR SPECIFIC ANIMATION SETS######################################################################################################################################################################################
    def METEOR_SET():
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
                if meteormoveX<=290 and level==4:
                        meteormoveY=-300
                        meteormoveX=-999
                else:
                    if meteormoveX<=320 and meteormoveY>=380 and gameY>360:
                        TimesPlayed=int(TimesPlayed)
                        TimesPlayed=TimesPlayed+1
                        retry()
                    for boomCount in range(13):
                        boom=window.blit(Boom[boomCount//1],(200,340))
                        boomCount=boomCount+1
                    meteormoveY=-300
                    meteormoveX=-999
            boomCount=0
###########KEY SPRITE ANIMATION######################################################################################################################################################################################            
    def KEY():
        global Key,keymove,KeysCollected
        if Obstacle:
            window.blit(Keys,(keymove,400))
        keymove=keymove-50
        if keymove<=330 and 290<=keymove and gameY>=380:
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
        global SETS,SETCHOOSER,axemove,sawmove,fireballmove,TimesPlayed,meteormoveX,meteormoveY,endless,levels,level,saw2move,saw3move,saw4move,saw1move
        KEY()
        if endless: 
            SETS=SETS+1
            if SETS>=100 and SETCHOOSER<25 and fireballmove<=0 and fireballmove<=0:
                SETCHOOSER=random.randint(0,100)
                SETS=0
            if SETS>=100 and SETCHOOSER>24 and SETCHOOSER<50 and axemove<=-20:
                SETCHOOSER=random.randint(0,100)
                SETS=0
            if SETS>=10 and SETCHOOSER>49 and SETCHOOSER<75 and meteormoveX>=800 and boomCount==0:
                SETCHOOSER=random.randint(0,100)
                SETS=0
            if SETS>=100 and SETCHOOSER>74 and sawmove<=0:
                SETCHOOSER=random.randint(0,100)
                SETS=0
            if SETCHOOSER<25:
                SAW_SETS()
                FIREBALL_SETS()
                axemove=800
            if SETCHOOSER>24 and SETCHOOSER<50:
                AXE()
                fireballmove=800
                sawmove=800
            if SETCHOOSER>49 and SETCHOOSER<75:
                METEOR()
                axemove=800
                fireballmove=800
                sawmove=800
            if SETCHOOSER>74:
                SAW()
                axemove=800
                fireballmove=800
        if levels:
            if level==1:
                FIREBALL_SETS1()
                SAW_SETS()
                axemove=800
                if fireballmove<=-20 and sawmove<=-20:
                    complete()
            if level==2:
                AXE_SET()
                SAW_SETS1()
                fireballmove=800
                if axemove<=-80 and saw1move<=-20:
                    complete()
            if level==3:
                SAW_SETS1()
                SAW_SETS2()
                SAW_SETS3()
                SAW_SETS4()
                axemove=800
                fireballmove=800
                if saw1move<=-20 and saw2move<=-20 and saw3move<=-20 and saw4move<=-20:
                    complete()
            if level==4:
                SAW_SETS1()
                AXE_SET()
                SAW_SETS2()
                FIREBALL_SETS1()
                METEOR_SET()
                if sawmove<=-20 and axemove<=-80 and saw2move<=-20 and meteormoveX<=-400:
                    complete()
###########BACKGROUND ANIMATION AND SETTINGS######################################################################################################################################################################################                    
    def BackgroundChange0():
        global n,MeteorX,MeteorY,SawX,FireballX,AxeX
        window.blit(bg5,[n,0])
        n=n-15
        window.blit(bg5,[screenWidth+screenWidth+screenWidth+screenWidth+screenWidth+n,0])
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
            window.blit(Jump[i],(gameX,gameY))
        if Slide:
            window.blit(Jump[j],(gameX,gameY))
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
                if not (Slide) and gameY>=380:    
                    if keys[pygame.K_DOWN]:
                        isJump=False
                        Run=False
                        Slide=True
                        walkCount=0
                        slideCount=0
                else:
                    if gameY>=380:                            
                        if slideCount>=-10:
                            neg=1
                            if slideCount<10:
                                neg=-1
                            gameY=400
                            j=j+1
                            if j>=4:
                                j=0
                            slideCount -=1
                        else:
                            isJump=False
                            Run=True
                            Slide=False
                            gameY=380
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
                        gameY -=(jumpCount**2)*0.5*neg
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
###########STATISTICS############################################################################################################################################################################################################
def STATISTICS():
    global Username
    Stats=True
    while Stats:
        window=pygame.display.set_mode([800,600])#,pygame.FULLSCREEN)
        window.blit(bg5,(0,0))
        Stats=open(Username+".txt","r")
        Stats.close()
        header=pygame.font.SysFont(None,140)
        font=pygame.font.SysFont(None,55)#55 is the size of the font
        header_text=header.render('STATS',False,(255,0,0))
        HScore_text=font.render(('HIGH SCORE: '+str(HighScore)),False,(255,0,0))
        TimesPlayed_text=font.render(('NUMBER OF TIMES PLAYED: '+str(TimesPlayed)),False,(255,0,0))
        KeysCollected_text=font.render(('NUMBER OF KEYS COLLECTED: '+str(KeysCollected)),False,(255,0,0))
        PlayTime_text=font.render(('TOTAL PLAY TIME: '+str(PlayTime)+'mins'),False,(255,0,0))
        window.blit(header_text,(250,50))
        window.blit(HScore_text,(10,200))
        window.blit(TimesPlayed_text,(10,300))
        window.blit(KeysCollected_text,(10,400))
        window.blit(PlayTime_text,(10,500))
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if mouse[0]>=525 and mouse[0]<=775 and mouse[1]>=450 and mouse[1]<=550:
            pygame.draw.rect(window,grey,[525,450,250,100])
            window.blit(BackTXT,(550,455))
            if click[0]==1:
                GUIMainMenu()
        else:
            pygame.draw.rect(window,black,[525,450,250,100])
            window.blit(BackTXT,(550,455))
        pygame.display.update()
############LEVELS MENU####################################################################################################################################################################################################
def LEVELS_MENU():
    global Username,level,Username,window,TimesPlayed,HighScore,PlayTime,KeysCollected,CurrentScore,endless,levels
    levels=True
    while levels:
        window=pygame.display.set_mode([800,600])#,pygame.FULLSCREEN)
        window.blit(bg1,(0,0))
        Stats=open(Username+".txt","r")
        Stats.close()
        header=pygame.font.SysFont(None,140)
        font=pygame.font.SysFont(None,55)#55 is the size of the font
        header_text=header.render('LEVELS',False,(255,0,0))
        level_text=font.render(('PLEASE SELECT A LEVEL'),False,(255,0,0))
        window.blit(header_text,(250,0))
        window.blit(level_text,(10,100))
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if mouse[0]>=525 and mouse[0]<=775 and mouse[1]>=450 and mouse[1]<=550:
            pygame.draw.rect(window,grey,[525,450,250,100])
            window.blit(BackTXT,(550,455))
            if click[0]==1:
                GUIMainMenu()
        else:
            pygame.draw.rect(window,black,[525,450,250,100])
            window.blit(BackTXT,(550,455))
        
        if mouse[0]>=40 and mouse[0]<=140 and mouse[1]>=150 and mouse[1]<=250:
            pygame.draw.rect(window,grey,[40,150,100,100])
            window.blit(oneTXT,(50,150))
            if click[0]==1:
                level=1
                window=pygame.display.set_mode([800,600])#,pygame.FULLSCREEN)
                levels=True
                endless=False
                gameLoop()
        else:
            pygame.draw.rect(window,black,[40,150,100,100])
            window.blit(oneTXT,(50,150))

        if mouse[0]>=180 and mouse[0]<=280 and mouse[1]>=150 and mouse[1]<=250:
            pygame.draw.rect(window,grey,[180,150,100,100])
            window.blit(twoTXT,(190,150))
            if click[0]==1:
                level=2
                window=pygame.display.set_mode([800,600])#,pygame.FULLSCREEN)
                levels=True
                endless=False
                gameLoop()
        else:
            pygame.draw.rect(window,black,[180,150,100,100])
            window.blit(twoTXT,(190,150))

        if mouse[0]>=320 and mouse[0]<=420 and mouse[1]>=150 and mouse[1]<=250:
            pygame.draw.rect(window,grey,[320,150,100,100])
            window.blit(threeTXT,(330,150))
            if click[0]==1:
                level=3
                window=pygame.display.set_mode([800,600])#,pygame.FULLSCREEN)
                levels=True
                endless=False
                gameLoop()
        else:
            pygame.draw.rect(window,black,[320,150,100,100])
            window.blit(threeTXT,(330,150))

        if mouse[0]>=460 and mouse[0]<=560 and mouse[1]>=150 and mouse[1]<=250:
            pygame.draw.rect(window,grey,[460,150,100,100])
            window.blit(fourTXT,(470,150))
            if click[0]==1:
                level=4
                window=pygame.display.set_mode([800,600])#,pygame.FULLSCREEN)
                levels=True
                endless=False
                gameLoop()
        else:
            pygame.draw.rect(window,black,[460,150,100,100])
            window.blit(fourTXT,(470,150))

        pygame.display.update()
############LOGIN MENU###########################################################################################################################################################################################################
def Menu():
    login1=("1","2","3")
    login= input("Are you a registered user?\n1)yes\n2)no\n3)quit\n")
    while login not in login1:
        login= input("That is not a valid input, please chooae options 1,2 or 3\n1)yes\n2)no\n3)quit\n")
    else:
        if login == "1":
            OldUser()
        elif login == "2":
            NewUser()
        elif login== "3":
            quit()
############EXISTING USERS#######################################################################################################################################################################################################
def OldUser():
    global Username,HighScore,TimesPlayed,PlayTime,KeysCollected,CurrentScore
    file1=open("Usernames.txt","r")
    total=len(file1.readlines())
    file1.close()
    file1=open("Usernames.txt","r")
    AccountNames=file1.readlines()
    file=open("Password.txt","r")
    AccountPasswords=file.readlines()
    Username=(input("Enter Username:  "))
    Password=(input("Enter Password:  "))
    i=0
    while Username not in AccountNames[i] and i < total:
        i=i+1
        if i == total:
            print("Username does not exist or password is incorrect")
            goBack=(input("\nDo you want to go back to the main menu\nPress B to go back\n"))
            if goBack =="b" or goBack =="B":
                Menu()
            else:
                OldUser()
                break
    else:
        while Password not in AccountPasswords[i]:
            print("Username does not exist or password is incorrect")
            goBack=(input("\nDo you want to go back to the main menu\nPress B to go back\n"))
            if goBack =="b" or goBack =="B":
                Menu()
            else:
                OldUser()
                break
        else:
            print("Login successful!")
            CurrentScore=0
            Stats=open(Username+".txt","r")
            lines=Stats.readlines()
            HighScore=lines[0][11]
            if lines[0][12] !=  " ":
                HighScore=HighScore+lines[0][12]
            TimesPlayed=lines[1][24]
            if lines[1][25] !=" ":
                TimesPlayed=TimesPlayed+lines[1][25]
            if lines[1][26] !=" ":
                TimesPlayed=TimesPlayed+lines[1][26]
            KeysCollected=lines[2][26]
            if lines[2][27] !=" ":
                KeysCollected=KeysCollected+lines[2][27]
            if lines[2][28] !=" ":
                KeysCollected=KeysCollected+lines[2][28]
            PlayTime=lines[3][17]
            if lines[3][18]!=" " and lines[3][18]!=".":
                PlayTime=PlayTime+lines[3][18]
            if lines[3][19]!=" " and lines[3][19]!=".":
                PlayTime=PlayTime+lines[3][19]
            HighScore=int(HighScore)
            KeysCollected=int(KeysCollected)
            PlayTime=int(PlayTime)
            TimesPlayed=int(TimesPlayed)
            CurrentScore=0
            GUIMainMenu()
############NEW USERS############################################################################################################################################################################################################
def NewUser():
    file1=open("Usernames.txt","r")
    total=len(file1.readlines())
    file1.close()
    file1=open("Usernames.txt","r")
    AccountNames=file1.readlines()
    NewUsername=(input("Enter Username:  "))
    i=0
    LetterNumberCheck=[' ']
    while NewUsername not in AccountNames[i] and i < total and NewUsername not in LetterNumberCheck:
        i=i+1
        if i == total:
            NewPassword=(input("Enter Password:  "))
            while NewPassword not in LetterNumberCheck:
                file=open("Password.txt","a+")
                file.write(NewPassword+"\n")
                file.close()
                file1=open("Usernames.txt","a+")
                file1.write(NewUsername+"\n")
                file1.close()
                print("\nNew user Created\n")
                print("Login successful!")
                Stats=open(NewUsername+".txt","w+")
                Stats.write("HighScore: 0           \n")
                Stats.write("Number of times played: 0          \n")
                Stats.write("Number of Keys collected: 0           \n")
                Stats.write("Total Play Time: 0              \n")
                Stats.close()
                Menu()
                break
            else:
                print("Please use 'a-z' text or numbers")
                NewUser()
    else:
        if NewUsername in LetterNumberCheck:
            print("Please use 'a-z' text or numbers")
            NewUser()
        print("This is an Exisiting User")
        NewUser()


############GUI MENU#############################################################################################################################################################################################################
def GUIMainMenu():
    global Username,endless,levels,level
    pygame.init()
    def ENDLESS():
        global Username,window,TimesPlayed,HighScore,PlayTime,KeysCollected,CurrentScore,endless,levels
###########LOADING AND SETTING STATISTICS########################################################################################################################################################################################
        window=pygame.display.set_mode([800,600])#,pygame.FULLSCREEN)
        endless=True
        levels=False
        gameLoop()
    def SHOP():
        print("SHOP")
    def STATS():
        window=pygame.display.set_mode([800,600])
        STATISTICS()
    def BACK():
        pygame.display.quit()
        Menu()
    intro=True
    while intro:
        for event in pygame.event.get():
            window=pygame.display.set_mode([800,600])#,pygame.FULLSCREEN)
            bgwindow=pygame.image.load('Waterfall1.png')
            bgwindow=pygame.transform.scale(bgwindow,(screenWidth+screenWidth+screenWidth+screenWidth,screenHeight+50))
            pygame.font.init()
            header=pygame.font.SysFont(None,100)
            font=pygame.font.SysFont(None,55)#55 is the size of the font
            header_text=header.render('WELCOME '+Username,False,(255,0,0))
            window.blit(bg3,(0,0))
            window.blit(EndlessTXT,(50,75))
            window.blit(LevelsTXT,(450,75))
            window.blit(ShopTXT,(50,375))
            window.blit(BackTXT,(550,375))
            window.blit(StatsTXT,(275,250))
            window.blit(header_text,(100,screenHeight/64))
            mouse=pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()
            if mouse[0]>=50 and mouse[0]<=350 and mouse[1]>=150 and mouse[1]<=250:
                pygame.draw.rect(window,Lgreen,[50,150,300,100])
                if click[0]==1:
                    Slide=True
                    ENDLESS()
            else:
                pygame.draw.rect(window,green,[50,150,300,100])
                
            if mouse[0]>=450 and mouse[0]<=750 and mouse[1]>=150 and mouse[1]<=250:
                pygame.draw.rect(window,Lgold,[450,150,300,100])
                if click[0]==1:
                    LEVELS_MENU()
            else:
                pygame.draw.rect(window,gold,[450,150,300,100])

            if mouse[0]>=250 and mouse[0]<=550 and mouse[1]>=330 and mouse[1]<=430:
                pygame.draw.rect(window,Lred,[250,330,300,100])
                if click[0]==1:
                    window.blit(bg3,(0,0))
                    STATS()
            else:
                pygame.draw.rect(window,red,[250,330,300,100])

            if mouse[0]>=50 and mouse[0]<=350 and mouse[1]>=450 and mouse[1]<=550:
                pygame.draw.rect(window,Lblue,[50,450,300,100])
                if click[0]==1:
                    print("SHOP")
            else:
                pygame.draw.rect(window,blue,[50,450,300,100])
            
            if mouse[0]>=450 and mouse[0]<=750 and mouse[1]>=450 and mouse[1]<=550:
                pygame.draw.rect(window,grey,[450,450,300,100])
                if click[0]==1:
                    BACK()
            else:
                pygame.draw.rect(window,black,[450,450,300,100])
            pygame.display.update()
Menu()
