###########IMPORTING##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
import pygame
import time
import random
pygame.init()
###########WINDOW CREATION############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
screenWidth=800
screenHeight=600
#window=pygame.display.set_mode([screenWidth,screenHeight])
#pygame.display.set_caption("STATS")
black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)
red=(255,0,0)
#line=1
def LEADERBOARD_HSCORE():
    #global line
    line=1
    Stats=open("Usernames.txt","r")
    Total=len(Stats.readlines())
    Stats.close()
    Stats=open("Usernames.txt","r")
    opening=Stats.readlines()
    print(Total)
    if Total-line>0:
        UsersLine=opening[Total-line]
        UsersLine=str(UsersLine)
        account=open(UsersLine +".txt","r")
        Fileline=account.readlines()
        print(account[0])
        line=line+1
LEADERBOARD_HSCORE()
##if TimesPlayed>=1:
##    TimesPlayed=str(TimesPlayed)
##    Stats=open("TEST obstacle.txt","r")
##    lines=Stats.readlines()
##    HighScore=lines[0][11]
##    if lines[0][12] !=  " ":
##        HighScore=HighScore+lines[0][12]
##    if lines[1][25] !=" ":
##        TimesPlayed=TimesPlayed+lines[1][25]
##        if lines[1][26] !=" ":
##            TimesPlayed=TimesPlayed+lines[1][26]
##    KeysCollected=lines[2][26]
##    if lines[2][27] !=" ":
##        KeysCollected=KeysCollected+lines[2][27]
##    PlayTime=lines[3][17]
##    if lines[3][18]!=" " and lines[3][18]!=".":
##        PlayTime=PlayTime+lines[3][18]
##        if lines[3][19]!=" " and lines[3][19]!=".":
##            PlayTime=PlayTime+lines[3][19]
##else:
##    HighScore=0
##    KeysCollected=0
#############INITIALISING##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
##HighScore=int(HighScore)
##KeysCollected=int(KeysCollected)
##PlayTime=int(PlayTime)
##TimesPlayed=int(TimesPlayed)
#############GAME OVER SCREEN AND UPDATING THE STATISTICS END GAME AND QUIT OR PLAY-AGAIN##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
##        Stats=open("TEST obstacle.txt","w+")
##        Stats.write("HighScore: "+str(HighScore)+"           "+"\n")
##        Stats.write("Number of times played: "+str(TimesPlayed)+"          "+"\n")
##        Stats.write("Number of Keys collected: "+str(KeysCollected)+"           "+"\n")
##        Stats.write("Total Play Time: "+str(PlayTime/15)+"           "+"\n")
##        Stats.close()
##                HighScore=int(HighScore)
##                TimesPlayed=int(TimesPlayed)
##                if n==0:
##                    CurrentScore=CurrentScore+1
##                    if CurrentScore>HighScore:
##                        HighScore=CurrentScore
##                Stats=open("TEST Obstacle.txt","w+")
##                Stats.write("HighScore: "+str(HighScore)+"           "+"\n")
##                Stats.write("Number of times played: "+str(TimesPlayed)+"          "+"\n")
##                Stats.write("Number of Keys collected: "+str(KeysCollected)+"           "+"\n")
##                Stats.write("Total Play Time: "+str(PlayTime/15)+"           "+"\n")
##                Stats.close()
##            pygame.quit()
##            quit()
##gameLoop()
