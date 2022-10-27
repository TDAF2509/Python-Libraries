def one():
    print("   ¬--------------¬")
    print("   |              |")
    print("   |              |")
    print("   |       O      |")
    print("   |              |")
    print("   |              |")
    print("   ¬--------------¬")
def two():
    print("   ¬--------------¬")
    print("   |              |")
    print("   |       O      |")
    print("   |              |")
    print("   |       O      |")
    print("   |              |")
    print("   ¬--------------¬")
def three():
    print("   ¬--------------¬")
    print("   |              |")
    print("   |    O     O   |")
    print("   |              |")
    print("   |       O      |")
    print("   |              |")
    print("   ¬--------------¬")
def four():
    print("   ¬--------------¬")
    print("   |              |")
    print("   |    O     O   |")
    print("   |              |")
    print("   |    O     O   |")
    print("   |              |")
    print("   ¬--------------¬")
def five():
    print("   ¬--------------¬")
    print("   |              |")
    print("   |   O     O    |")
    print("   |      O       |")
    print("   |   O     O    |")
    print("   |              |")
    print("   ¬--------------¬")
def six():
    print("   ¬--------------¬")
    print("   |              |")
    print("   |     O  O     |")
    print("   |     O  O     |")
    print("   |     O  O     |")
    print("   |              |")
    print("   ¬--------------¬")
WIN=0
def Guess():
    global WIN
    number3=(['1','2','3','4','5','6'])
    print("THE GAME REVOLVES AROUND A STANDARD SIX SIDED DICE\n")
    print("THEREFORE COULD ALL GUESSES BE BETWEEN 1 AND 6\n")
    print("THE AIM OF THE GAME IS TO GUESS WHAT NUMBER THE DICE WILL LAND ON\n")
    guess= input("PLEASE ENTER A GUESS FOR THE DICE ROLL\n")
    while guess not in number3:
        print ("THE VALUE YOU ENTERED IS INVALID\n")
        guess= input("PLEASE ENTER A GUESS FOR THE DICE ROLL\n")
    else:
        comfirm=("")
        enter=input("PRESS ENTER TO ROLL THE DICE")
        while enter not in comfirm:
            print("INVALID INPUT\n")
            enter=input("PLEASE PRESS ENTER TO ROLL THE DICE\n")
    import random
    valid_values2=['1','2','3','4','5','6']
    roll=random.choice(valid_values2)
    if roll=='1':
        (one())
    elif roll=='2':
        (two())
    elif roll=='3':
        (three())
    elif roll=='4':
        (four())
    elif roll=='5':
        (five())
    elif roll=='6':
        (six())
    if roll==guess:
        print("\nCORRECT GUESS")
        WIN=WIN+1
    else:
        print("\nWRONG")
    play_again=input("DO YOU WISH TO PLAY AGAIN?\n")
    while play_again=="y" or play_again=="Y":
        (Guess())
    else:
        if play_again=="n" or play_again=="N":
            (menu())
            
        else:
            print("PLEASE ENTER A VALID YES OR NO ANSWER\n")
            play_again=input("DO YOU WISH TO PLAY AGAIN?\n")


PLAYER1_WIN=0
PLAYER2_WIN=0
DRAW=0            
def game():
    global PLAYER1_WIN
    global PLAYER2_WIN
    global DRAW
    number2=((['1','2','3','4','5','6']))
    print("THE GAME REVOLVES AROUND A STANDARD SIX SIDED DICE\n")
    print("THEREFORE COULD ALL GUESSES BE BETWEEN 1 AND 6\n")
    print("THE AIM OF THE GAME IS TO GUESS WHAT NUMBER THE DICE WILL LAND ON\n")
    print("THE PLAYER WITH THE CLOSER GUESS WINS")  
    Player1= input("CAN PLAYER 1 PLEASE ENTER A GUESS FOR THE DICE ROLL\n")
    while Player1 not in number2:
        print ("THE VALUE YOU ENTERED IS INVALID\n")
        Player1= input("CAN PLAYER 1 PLEASE ENTER A GUESS FOR THE DICE ROLL\n")
    else:
        Player2=input("CAN PLAYER 2 PLEASE ENTER A GUESS FOR THE DICE ROLL\n")
        while Player2 not in number2:
            print ("THE VALUE YOU ENTERED IS INVALID\n")
            Player2= input("CAN PLAYER 2 PLEASE ENTER A GUESS FOR THE DICE ROLL\n")
        else:
            print("\n")
    Enter=input("PRESS ENTER TO ROLL THE DICE")
    while Enter is not D015:
        Enter=input("PLEASE PRESS TO ROLL THE DICE")
        
    valid_values=['1','2','3','4','5','6']
    import random
    roll=random.choice(valid_values)
    if roll=='1':
        (one())
    elif roll=='2':
        (two())
    elif roll=='3':
        (three())
    elif roll=='4':
        (four())
    elif roll=='5':
        (five())
    elif roll=='6':
        (six())
    if roll<=Player1 and Player1<Player2 or roll>=Player1 and Player1>Player2:
          print("PLAYER 1 WINS THE ANSWER WAS ",roll)
          PLAYER1_WIN=PLAYER1_WIN+1
          print("\n")
    elif roll<=Player2 and Player2<Player1 or roll>=Player2 and Player2>Player1:
          print("PLAYER 2 WINS THE ANSWER WAS ",roll)
          PLAYER2_WIN=PLAYER2_WIN+1
          print("\n")
    elif roll==Player1 and roll==Player2:
          print("ITS A DRAW THE ANSWER WAS ",roll)
          DRAWW=DRAW+1
          print("\n")
    print("PLAYER 1 HAS WON ",PLAYER1_WIN," TIMES")
    print("PLAYER 2 HAS WON ",PLAYER2_WIN," TIMES\n")
    print("THE PLAYERS HAVE DRAWN ",DRAW," TIMES\n") 

    play_again=input("DO YOU WISH TO PLAY AGAIN?\n")
    while play_again=="y" or play_again=="Y":
        (game())
    else:
        if play_again=="n" or play_again=="N":
            print("YOU WILL BE TAKEN BACK TO THE MAIN MENU")
            (menu())
        else:
            print("PLEASE ENTER A VALID YES OR NO ANSWER\n")
            play_again=input("DO YOU WISH TO PLAY AGAIN?\n")


x=1
o=1
Xwin=0
Owin=0
def play():
        play_again=input("DO YOU WANT TO PLAY AGAIN\nYES OR NO?\n")
        while play_again=="y" or play_again=="Y":
            ludo()
        if play_again=="n" or play_again=="N":
            print("X has won ",Xwin," times")
            print("O has won ",Owin," times")
            if Xwin>Owin:
                import turtle
                import time
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
                import time
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
            menu()
        else:
            print("PLEASE ENTER A VALID YES OR NO ANSWER")
            play=input("DO YOU WANT TO PLAY AGAIN?\nYES OR NO?\n")


def ludo():
    import time
    a=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    b=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    i = 0
    secure=(['1','2'])
    print("THE AIM OF THE GAME IS TO GET YOUR ICON TO SPACE 25")
    print("YOU WILL BE ASKED TO ROLL A DICE WHICH WILL DETERMINE")
    print("THE SPACE YOUR ICON LANDS IN THE GRID")
    print("THE WINNER IS THE ONE TO GET TO 25 FIRST\n")
    print ("CAN PLAYER 1 PLEASE CHOOSE THEIR ICON FROM THE OPTIONS BELOW PLAYER 2 WILL BE GIVEN THE OTHER")
    print("\n")
    icon=input("SELECT 1 FOR X\nSELECT 2 FOR O\n")
    while icon not in secure:
        print("THE VALUE YOU ENTERED WAS INVALID\n")
        icon=input("SELECT 1 FOR X\nSELECT 2 FOR O\n")
    if icon =='1':
        print ("PLAYER 1 IS X AND PLAYER 2 IS O\n")
    elif icon =='2':
        print ("PLAYER 1 IS O AND PLAYER 2 IS X\n")
    time.sleep(2)
    import random
    first=random.randint(1,2)
    if first==1:
        print("PLAYER 1 GOES FIRST\n")
    elif first==2:
        print("PLAYER 2 GOES FIRST\n")
    def maingame(a,b):
        global x
        global o
        global movex
        global moveo
        import random
        if i==0:
            x=1
            o=1
            enteredalready=[]
            enteredalready+=[o]
            b[o]='o'
            enteredalready+=[x]
            a[o]='x'
        print(" START")
        print(" -----------------------------------------------¬")
        print(" |  ",a[1],b[1]," |  ",a[2],b[2]," |   ",a[3],b[3],"|   ",a[4],b[4],"  |   ",a[5],b[5],"|")
        print(" ------------------------------------------------")
        print(" |  ",a[6],b[6]," |  ",a[7],b[7]," |   ",a[8],b[8],"|   ",a[9],b[9],"  |   ",a[10],b[10],"|")
        print(" ------------------------------------------------")
        print(" |  ",a[11],b[11]," |  ",a[12],b[12]," |   ",a[13],b[13],"|   ",a[14],b[14],"  |   ",a[15],b[15],"|")
        print(" ------------------------------------------------")
        print(" |  ",a[16],b[16]," |  ",a[17],b[17]," |   ",a[18],b[18],"|   ",a[19],b[19],"  |   ",a[20],b[20],"|")
        print(" ------------------------------------------------")
        print(" |  ",a[21],b[21]," |  ",a[22],b[22]," |   ",a[23],b[23],"|   ",a[24],b[24],"  |   ",a[25],b[25],"|")
        print(" ------------------------------------------------")
        print("                                             END")


    def x_place2():
        global x
        global Xwin
        while 'x' in a[25] and x==25:
            x=25
            maingame(a,b)
            Xwin=Xwin+1
            print("X WINS:\nX HAS WON ",Xwin," TIMES!\n")
            play()

    def o_place2():
        global o
        global Owin
        while 'o' in b[25] and o==25:
            o=25
            maingame(a,b)
            Owin=Owin+1
            print("O WINS:\nO HAS WON ",Owin," TIMES!\n")
            play()

    def x_place():
        global x
        global enteredalready
        if i==0:
            enteredalready=[]
        xroll=input("PLEASE ROLL THE DICE FOR X\n")
        import random
        movex=random.randint(1,6)
        if movex==1:
            (one())
        elif movex==2:
            (two())
        elif movex==3:
            (three())
        elif movex==4:
            (four())
        elif movex==5:
            (five())
        elif movex==6:
            (six())
        x=x+movex
        xclr=x-movex
        if x>25:
            print("YOU NEED AN EXACT AMOUNT TO WIN\n")
            x=x-movex
        enteredalready+=[x]
        a[x]="x"
        if x!=xclr:
            enteredalready+=[xclr]
            a[xclr]=" "
        while 'x' in a[25] and 'o' not in b[25]:
            x_place2()

            
    def o_place():
        global enteredalready
        global o
        if i==0:
            enteredalready=[]
        oroll=input("PLEASE ROLL THE DICE FOR O\n")
        import random
        moveo=random.randint(1,6)
        if moveo==1:
            (one())
        elif moveo==2:
            (two())
        elif moveo==3:
            (three())
        elif moveo==4:
            (four())
        elif moveo==5:
            (five())
        elif moveo==6:
            (six())
        o=o+moveo
        oclr=o-moveo
        if o>25:
            print("YOU NEED TO GET TO 25 TO WIN\n")
            o=o-moveo
        enteredalready+=[o]
        b[o]='o'
        if o!=oclr:
            enteredalready+=[oclr]
            b[oclr]=" "
        while 'o' in b[25] and 'x' not in a[25]:
            o_place2()     

    global Xwin
    global Owin
    global Draw
    global x
    global o
    while first==1 and icon=='1':
        while x!=25 and 'x' not in a[25]or o!=25 and 'o' not in b[25]:
            maingame(a,b)
            x_place()
            i=i+1
            maingame(a,b)
            i=i-1
            o_place()
            i=i+1
            if x==25 and 'x' in a[25]:
                x_place2()
            if o==25 and 'o' in b[25]:
                o_place2()        
        else:
            play()
            
    while first==1 and icon=='2':
        while x!=25 and 'x' not in a[25]or o!=25 and 'o' not in b[25]:
            maingame(a,b)
            o_place()
            i=i+1
            maingame(a,b)
            i=i-1
            x_place()
            i=i+1
            if x==25 and 'x' in a[25]:
                x_place2()
            if o==25 and 'o' in b[25]:
                o_place2()        
        else:
            play()

    while first==2 and icon=='2':
        while x!=25 and 'x' not in a[25]or o!=25 and 'o' not in b[25]:
            maingame(a,b)
            x_place()
            i=i+1
            maingame(a,b)
            i=i-1
            o_place()
            i=i+1
            if x==25 and 'x' in a[25]:
                x_place2()
            if o==25 and 'o' in b[25]:
                o_place2()        
        else:
            play()

    while first==2 and icon=='1':
        while x!=25 and 'x' not in a[25]or o!=25 and 'o' not in b[25]:
            maingame(a,b)
            o_place()
            i=i+1
            maingame(a,b)
            i=i-1
            x_place()
            i=i+1
            if x==25 and 'x' in a[25]:
                x_place2()
            if o==25 and 'o' in b[25]:
                o_place2()        
        else:
            play()

    


def menu():
    import time
    time.sleep(1)
    print(" "*14,"-"*52)
    print("  "*12,"*"*10,"DICE GAME","*"*10)
    print(" "*14,"-"*52)
    print("\n")
    print("\n")
    time.sleep(1)
    number=(['1','2','3','4'])
    choice= input("1)GUESS MY NUMBER DICE GAME\n2)DICE GAME\n3)25 RACE\n4)QUIT\nPLEASE CHOOSE FROM THE MENU\n")
    while choice not in number:
        print ("THE VALUE YOU ENTERED IS INVALID\n")
        choice=input("1)GUESS MY NUMBER DICE GAME\n2)DICE GAME\n3)LUDO\n4)QUIT\nPLEASE CHOOSE FROM THE MENU\n")
    else:
        if choice=='1':
            (Guess())
        elif choice=='2':
            (game())
        elif choice=='3':
            (ludo())
        elif choice=='4':
            quit()
menu()
