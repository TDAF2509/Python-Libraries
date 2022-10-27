import time
time.sleep(1)
print(" "*14,"-"*52)
print(" "*14,"*"*10,"WELCOME TO NAUGHTS AND CROSSES","*"*10)
print(" "*14,"-"*52)
print("\n")
print("\n")
time.sleep(1)
print("1)START THE GAME\n2)QUIT")
choice=int(input("PLEASE ENTER A CHOICE FROM THE MENU\n"))
while  choice <1  or choice >2:
    print ("THE VALUE YOU ENTERED IS INVALID\n")
    choice=int(input("PLEASE ENTER A CHOICE FROM THE MENU\n"))
if choice==2:
    quit()

time.sleep(2)
print ("CAN PLAYER 1 PLEASE CHOOSE THEIR ICON PLAYER 2 WILL BE GIVEN THE OTHER")
print("\n")
icon=int(input("SELECT 1 FOR X\nSELECT 2 FOR O\n"))
while icon <1 or icon >2:
    print("THE VALUE YOU ENTERED WAS INVALID\n")
    icon=int(input("SELECT 1 FOR X\nSELECT 2 FOR O\n"))
if icon ==1:
    print ("PLAYER 1 IS X AND PLAYER 2 IS O\n")
elif icon ==2:
    print ("PLAYER 1 IS O AND PLAYER 2 IS X\n")
import random
first=random.randint(1,2)
if first ==1:
    print("PLAYER 1 GOES FIRST")
else:
    print ("PLAYER 2 GOES FIRST")
seven=7=="7"
eight=8=="8"
nine=9=="9"
four=4=="4"
five=5=="5"
six=6=="6"
one=1=="1"
two=2=="2"
three=3=="3"


def maingame():
    global first
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    print(' ','-'*19)
    print('  | ', "7" , ' | ' , 8 , ' | ' , 9, ' | ')
    print(' ','-'*19)
    print('  | ', 4 , ' | ' , 5 , ' | ' , 6, ' | ')
    print(' ','-'*19)
    print('  | ', 1 , ' | ' , 2 , ' | ' , 3, ' | ')
    print(' ','-'*19)
    place = int(input("PLEASE ENTER A NUMBER ON THE GRID TO PLACE YOUR ICON"))
    while place <1 or place > 9:
        print("THE VALUE YOU ENTERED WAS INVALID\n")
        place = int(input("PLEASE ENTER A NUMBER ON THE GRID TO PLACE YOUR ICON"))
    if place == 7 and first==1:
        7=="X"
    elif place ==7 and first==2:
        7=="O"
    if eight != "X":
        print(maingame())
maingame()
