import time
time.sleep(1)
print(" "*14,"-"*52)
print(" "*14,"*"*10,"WELCOME TO NAUGHTS AND CROSSES","*"*10)
print(" "*14,"-"*52)
print("\n")
print("\n")
time.sleep(1)
def security():
    secure= (['1','2'])
    choice= input("1)START THE GAME\n2)QUIT\n")
    while choice not in secure:
        print ("THE VALUE YOU ENTERED IS INVALID\n")
        choice= input("1)START THE GAME\n2)QUIT\n")
    else:
        if choice=='2':
            quit()
(security())
time.sleep(2)
print("THE AIM OF THE GAME IS TO GET THE SAME ICON THREE TIMES IN A ROW, COLUMN OR DIAGONAL LINE\n")
time.sleep(1)
print("THE GAME ENDS WHEN\n1)THE USER WINS\nOR\n2)THE GRID IS FILLED WITH NO WINNER\n")
time.sleep(2)
print ("CAN PLAYER 1 PLEASE CHOOSE THEIR ICON FROM THE OPTIONS BELOW PLAYER 2 WILL BE GIVEN THE OTHER")
print("\n")


secure2= (['1','2'])
icon= input("SELECT 1 FOR X\nSELECT 2 FOR O\n")
while icon not in secure2:
    print ("THE VALUE YOU ENTERED IS INVALID\n")
    icon= input("SELECT 1 FOR X\nSELECT 2 FOR O\n")
else:
    if icon =='1':
        print ("PLAYER 1 IS X AND PLAYER 2 IS O\n")
    elif icon =='2':
        print ("PLAYER 1 IS O AND PLAYER 2 IS X\n")

time.sleep(2)
print("THE PLAYER TO GO FIRST WILL BE RANDOMLY SELECTED")
time.sleep(2)
import random
first=random.randint(1,2)
if first ==1:
    print("PLAYER 1 GOES FIRST\n")
else:
    print ("PLAYER 2 GOES FIRST\n")
time.sleep(1)
print ("BELOW IS A LAYOUT OF THE GRID YOU WILL BE PLAYING ON\n")
time.sleep(1)
print ("THE NUMBERS REPRESENT THE GRID PLACES YOUR ICON WILL BE PLACED IN\n")
print(' ','-'*19)
print('  | ', "1" , ' | ' , "2" , ' | ' , "3", ' | ')
print(' ','-'*19)
print('  | ', "4" , ' | ' , "5" , ' | ' , "6", ' | ')
print(' ','-'*19)
print('  | ', "7" , ' | ' , "8" , ' | ' , "9", ' | ')
print(' ','-'*19)
time.sleep(2)
print("\nWHEN PLAYING CHOOSE A NUMBER IN ORDER TO PLACE YOUR ICON IN THAT GRID PLACE\n")
time.sleep(4)
enter=input("PRESS ENTER TO CONTINUE\n")
a=["","","","","","","","","",""]
enteredalready=[]
Xwin=0
Owin=0
Draw=0
def game():
    a=[" "," "," "," "," "," "," "," "," "," "]
    i = 0
    def maingame(a):
        global x
        global o
        print("   -------------------------------")
        print("   |   ",a[1],"   |   ",a[2],"   |   ",a[3],"   |")
        print("   -------------------------------")
        print("   |   ",a[4],"   |   ",a[5],"   |   ",a[6],"   |")
        print("   -------------------------------")
        print("   |   ",a[7],"   |   ",a[8],"   |   ",a[9],"   |")
        print("   -------------------------------")

    def x_place():
        global x
        global enteredalready
        secure3=([1,2,3,4,5,6,7,8,9])
        if i==0:
            enteredalready=[]
        x= int(input("PLEASE ENTER A SPACE FOR X "))
        while x not in secure3:
            print("PLEASE CHOOSE A NUMBER ON THE GRID")
            x= int(input("PLEASE ENTER A SPACE FOR X "))
        else:
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
        secure4=([1,2,3,4,5,6,7,8,9])
        if i==0:
            enteredalready=[]
        o= int(input("PLEASE ENTER A SPACE FOR O "))
        while o not in secure4:
            print("PLEASE CHOOSE A NUMBER ON THE GRID")
            o= int(input("PLEASE ENTER A SPACE FOR X "))
        else:
            if not(o in enteredalready):
                enteredalready+=[o]
                a[o]=o="O" 
            else:
                print("Choose Another Number")
                (maingame(a))
                (o_place())
    global Xwin
    global Owin
    global Draw
    global x
    global o
    global icon
    while i<=4:
        if first==1 and icon=='1':
            (maingame(a))
            (x_place())
            first==2
        elif first==1 and icon=='2':
            (maingame(a))
            (o_place())
            first==1
        elif first==2 and icon=='1':
            (maingame(a))
            (x_place())
            first==1
        elif first==2 and icon=='2':
            (maingame(a))
            (o_place)
            first==1

        if a[1]==a[2]==a[3]==x:
            print("X WINS")
            Xwin=Xwin+1
            print("X has won ",Xwin," times")
            a=[" "," "," "," "," "," "," "," "," "," "]
            break
        elif a[4]==a[5]==a[6]==x:
            print("X WINS")
            Xwin=Xwin+1
            print("X has won ",Xwin," times")
            a=[" "," "," "," "," "," "," "," "," "," "]
            break
        elif a[7]==a[8]==a[9]==x:
            print("X WINS")
            Xwin=Xwin+1
            print("X has won ",Xwin," times")
            a=[" "," "," "," "," "," "," "," "," "," "]
            break
        elif a[1]==x and a[4]==x and a[7]==x:
            print("X WINS")
            Xwin=Xwin+1
            print("X has won ",Xwin," times")
            a=[" "," "," "," "," "," "," "," "," "," "]
            break
        elif a[1]==x and a[5]==x and a[9]==x:
            print("X WINS")
            Xwin=Xwin+1
            print("X has won ",Xwin," times")
            a=[" "," "," "," "," "," "," "," "," "," "]
            break
        elif a[3]==x and a[5]==x and a[7]==x:
            print("X WINS")
            Xwin=Xwin+1
            print("X has won ",Xwin," times")
            a=[" "," "," "," "," "," "," "," "," "," "]
            break
        elif a[3]==x and a[6]==x and a[9]==x:
            print("X WINS")
            Xwin=Xwin+1
            print("X has won ",Xwin," times")
            a=[" "," "," "," "," "," "," "," "," "," "]
            break
        (o_place())
        i=i+1
        if a[1]==o and a[2]==o and a[3]==o:
            print("O WINS")
            Owin=Owin+1
            print("O has won ",Owin," times")
            a=[" "," "," "," "," "," "," "," "," "," "]
            break
        elif a[4]==o and a[5]==o and a[6]==o:
            print("O WINS")
            Owin=Owin+1
            print("O has won ",Owin," times")
            a=[" "," "," "," "," "," "," "," "," "," "]
            break
        elif a[7]==o and a[8]==o and a[9]==o:
            print("O WINS")
            Owin=Owin+1
            print("O has won ",Owin," times")
            a=[" "," "," "," "," "," "," "," "," "," "]
            break
        elif a[1]==o and a[4]==o and a[7]==o:
            print("O WINS")
            Owin=Owin+1
            print("O has won ",Owin," times")
            a=[" "," "," "," "," "," "," "," "," "," "]
            break
        elif a[1]==o and a[5]==o and a[9]==o:
            print("O WINS")
            Owin=Owin+1
            print("O has won ",Owin," times")
            a=[" "," "," "," "," "," "," "," "," "," "]
            break
        elif a[3]==o and a[5]==o and a[7]==o:
            print("O WINS")
            Owin=Owin+1
            print("O has won ",Owin," times")
            a=[" "," "," "," "," "," "," "," "," "," "]
            break
        elif a[3]==o and a[6]==o and a[9]==o:
            print("O WINS")
            Owin=Owin+1
            print("O has won ",Owin," times")
            a=[" "," "," "," "," "," "," "," "," "," "]
            break
    else:
        print("ITS A DRAW")
        Draw=Draw+1
    def end():
        global Xwin
        global Owin
        global Draw
        play_again=input("DO YOU WANT TO PLAY AGAIN\nYES OR NO?\n")
        while play_again=="y" or play_again=="Y":
            game()
            if play_again=="n" or play_again=="N":
                print("X has won ",Xwin," times")
                print("O has won ",Owin," times")
                print("YOU HAVE DRAWN ",Draw," times")
            elif Xwin>Owin:
                import turtle
                turtle.screensize(20000,15000)
                turtle.bgcolor("black")
                turtle.begin_fill()
                turtle.color("gold")
                turtle.circle(120)
                turtle.end_fill()
                turtle.goto(0,100)
                turtle.pensize(10)
                turtle.color("white")
                turtle.lt(45)
                turtle.fd(130)
                turtle.goto(0,100)
                turtle.lt(90)
                turtle.fd(130)
                turtle.goto(0,100)
                turtle.rt(180)
                turtle.fd(105)
                turtle.goto(0,100)
                turtle.rt(90)
                turtle.fd(105)
                time.sleep(3)
                turtle.bye
                print("X WINS OVERALL")
            elif Owin>Xwin:
                import turtle
                turtle.screensize(20000,15000)
                turtle.bgcolor("black")
                turtle.begin_fill()
                turtle.color("gold")
                turtle.circle(120)
                turtle.end_fill()
                turtle.goto(0,50)
                turtle.pensize(10)
                turtle.color("white")
                turtle.circle(60)
                time.sleep(3)
                turtle.bye
                print("O WINS OVERALL")
            quit()
        else:
            print("PLEASE ENTER A VALID YES OR NO ANSWER")
            (end())
    (end())
game()


    
