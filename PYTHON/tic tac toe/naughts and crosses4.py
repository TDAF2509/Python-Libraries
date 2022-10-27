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

a=["","","","","","","","","",""]
enteredalready=[]
Xwin=0
Owin=0
def maingame(a):
    global enteredalready
    global x
    global o
    print("-------------")
    print("|",a[1],"|",a[2],"|",a[3],"|")
    print("-------------")
    print("|",a[4],"|",a[5],"|",a[6],"|")
    print("-------------")
    print("|",a[7],"|",a[8],"|",a[9],"|")
    print("-------------")
    

def x_place():
    global x
    global enteredalready
    x= int(input("PLEASE ENTER A SPACE FOR X "))
    if not(x in enteredalready):
        enteredalready+=[x]
        a[x]=x="x"
        (maingame(a))
    else:
        print("Choose Another Number")
        (maingame(a))
        (x_place())

def o_place():
    global enteredalready
    global o
    o= int(input("PLEASE ENTER A SPACE FOR O "))
    if not(o in enteredalready):
        enteredalready+=[o]
        a[o]=o="O"
    else:
        print("Choose Another Number")
        print(maingame(a))
        print(o_place())
        

i = 1
while i<=5:
    i=i+1
    if first==1:
        first==2
    elif first==2:
        first==1
    (maingame(a))
    (x_place())
    if a[1]==a[2]==a[3]==x:
        print("X WINS")
        Xwin=Xwin+1
        print("X has won ",Xwin," times")
        break
    elif a[4]==a[5]==a[6]==x:
        print("X WINS")
        Xwin=Xwin+1
        print("X has won ",Xwin," times")
        break
    elif a[7]==a[8]==a[9]==x:
        print("X WINS")
        Xwin=Xwin+1
        print("X has won ",Xwin," times")
        break
    elif a[1]==x and a[4]==x and a[7]==x:
        print("X WINS")
        Xwin=Xwin+1
        print("X has won ",Xwin," times")
        break
    elif a[1]==x and a[5]==x and a[9]==x:
        print("X WINS")
        Xwin=Xwin+1
        print("X has won ",Xwin," times")
        break
    elif a[3]==x and a[5]==x and a[7]==x:
        print("X WINS")
        Xwin=Xwin+1
        print("X has won ",Xwin," times")
        break
    elif a[3]==x and a[6]==x and a[9]==x:
        print("X WINS")
        Xwin=Xwin+1
        print("X has won ",Xwin," times")
        break
    (o_place())
    if a[1]==o and a[2]==o and a[3]==o:
        print("O WINS")
        Owin=Owin+1
        print("O has won ",Owin," times")
        break
    elif a[4]==o and a[5]==o and a[6]==o:
        print("O WINS")
        Owin=Owin+1
        print("O has won ",Owin," times")
        break
    elif a[7]==o and a[8]==o and a[9]==o:
        print("O WINS")
        Owin=Owin+1
        print("O has won ",Owin," times")
        break
    elif a[1]==o and a[4]==o and a[7]==o:
        print("O WINS")
        Owin=Owin+1
        print("O has won ",Owin," times")
        break
    elif a[1]==o and a[5]==o and a[9]==o:
        print("O WINS")
        Owin=Owin+1
        print("O has won ",Owin," times")
        break
    elif a[3]==o and a[5]==o and a[7]==o:
        print("O WINS")
        Owin=Owin+1
        print("O has won ",Owin," times")
        break
    elif a[3]==o and a[6]==o and a[9]==o:
        print("O WINS")
        Owin=Owin+1
        print("O has won ",Owin," times")
        break
    
    
else:
    print("ITS A DRAW")

    
