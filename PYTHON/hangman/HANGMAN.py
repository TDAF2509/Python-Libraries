#hangman
def hangmanstart():
    print("   -----------")
    
def hangman2():
    print("     |")
    print("     |")     
    print("     |")
    print("     |")     
    print("     |")
    print("     |")
    print("     |    ")
    print("     |    ")
    print("   -----------")

def hangman3():
    print("   -------¬")
    print("     |")
    print("     |")     
    print("     |")
    print("     |")     
    print("     |")
    print("     |")
    print("     |    ")
    print("     |    ")
    print("   -----------")

def hangman4():
    print("   -------¬")
    print("     |    |")
    print("     |")     
    print("     |")
    print("     |")     
    print("     |")
    print("     |")
    print("     |    ")
    print("     |    ")
    print("   -----------")

def hangman5():
    print("   -------¬")
    print("     |    |")
    print("     |    O")     
    print("     |")
    print("     |")     
    print("     |")
    print("     |")
    print("     |    ")
    print("     |    ")
    print("   -----------")

def hangman6():
    print("   -------¬")
    print("     |    |")
    print("     |    O")     
    print("     |    +")
    print("     |")     
    print("     |")
    print("     |")
    print("     |    ")
    print("     |    ")
    print("   -----------")

def hangman7():
    print("   -------¬")
    print("     |    |")
    print("     |    O")     
    print("     |  --+")
    print("     |  / | ")     
    print("     |")
    print("     |")
    print("     |    ")
    print("     |    ")
    print("   -----------")

def hangman8():
    print("   -------¬")
    print("     |    |")
    print("     |    O")     
    print("     |  --+--")
    print("     |  / | \ ")
    print("     |")
    print("     |")
    print("     |    ")
    print("     |    ")
    print("   -----------")

def hangman9():
    print("   -------¬")
    print("     |    |")
    print("     |    O")     
    print("     |  --+--")
    print("     |  / | \ ")     
    print("     |   / ")
    print("     |  /  ")
    print("     |    ")
    print("     |    ")
    print("   -----------")

def hangman10():
    print("   -------¬")
    print("     |    |")
    print("     |    O")     
    print("     |  --+--")
    print("     |  / | \ ")     
    print("     |   / \ ")
    print("     |  /   \ ")
    print("     |    ")
    print("     |    ")
    print("   -----------")

ftblplyrs=['Messi','Ronaldo','Hazard','Neymar','Xavi','Iniesta','Ibrahimovic','Falcao','van Persie','Pirlo','Toure','Cavani','Aguero','Casillas','Mesut Ozil','Silva', 'Schweinsteiger'  ,'Buffon','Suarez','Ramos','Kompany','Pique','Lahm','Willian','Reus','Ribery','Neuer','Rooney','Mata','Muller','Benzema','Fabregas','Oscar','Fernandinho','Gareth Bale','Alves','Cech','Hummels','Di Maria','Tevez','Drogba']
tvshows=['The Big Bang Theory','The Flash','Arrow','DCs Legends of Tomorrow','Black lightning','Holby City','Eastenders','Hollyoaks','The Simpsons','Modern Family','Futurama','The Middle','Impractical Jokers','Dancing on Ice','Rick and Morty','Stricly Come Dancing','X factor','Britains got talent','The Chase','SAS Who Dares Wins','NCIS LA','Hawaii Five-O','American Dad','Family Guy','Ninja Warrior','The Apprentice','Dragons Den','Daredevil','Luke Cage','Iron Fist','Jessica Jones','The Defenders','Fresh Prince of Bel-Air','Ultimate Fighting Champion','Top Gear','Emmerdale','Criminal Minds','Crystal Maze','Mastermind','University Challange','Casualty','Greys anatomy','Death in Paradise']
Animeshws=['One Piece','Naruto Shippuuden','Dragon Ball Super','Hunter x Hunter','Fairy Tail','Bleach','Naruto','One Punch Man','Detective Conan','Boruto: Naruto Next Generations','Dragon Ball Z','Boku no Hero Academia','Gintama','Sword Art Online','Attack on Titan','Akame ga Kill','Twin Star exorcist','Katekyo Hitman Reborn','Haikyuu','Shokugeki no Souma','Fullmetal Alchemist Brotherhood','The Seven Deadly Sins','Tokyo Ghoul','Kuroko no Basket','Dragon Ball','Pokemon','Assassination Classroom','Death note','High School DXD',"Jojo's Bizarre Adventure Phantom Blood","Jojo's Bizarre Adventure Battle Tendancy","Jojo's Bizarre Adventure Stardust Crusaders","Jojo's Bizarre Adventure Diamond is Unbreakable","Jojo's Bizarre Adventure Venta aureo","Jojo's Bizarre Adventure Stone Ocean","Jojo's Bizarre Adventure Steel Ball Run","Jojo's Bizarre Adventure Jojolion",'Blue exorcist','Black clover','Black lagoon','Noragami','Beelzebub','Soul Eater','Toriko','Saiki Kusuo no Psi Nan','Yuu Yuu Hakusho','No game no life','Is this a Zombie','The World God only knows','Blood Lad',]
AnimeCharacters=['Goku','Luffy','Naruto','Ichigo','Tsuna','Gon','Natsu','Saitama','Conan','Boruto','Deku','Gintoki,','Kirito','Erin','Akame','Saiki','Toriko','Kaneki','Souma','Hinata','Meliotis','Kuroko','Vlad','Soul','Oga','Revy','Yato','Jonathan Joestar','Joseph Joestar','Jotaro Kujo','Josuke Higashikata','Giorno Giovanna','Jolyne Cujoh','Johnny Joestar','Josuke Higashikata eight','Edward','Ash','Nagisa','Light','Asta','Rin','Yusuke']
def ftbllgame():
          global ftblplyrs
          import random
          
          ftword=random.choice(ftblplyrs).lower()
          plyrguess= None
          lttrguessed=[]
          wrdguessed=[]
          for letter in ftword:
              wrdguessed.append("-")
          addedword= None
          chsnword= len(ftword)-1
          attempts=10

          while (attempts!=0 and "-" in wrdguessed):
              print ("\n\nYou have ",attempts,"left\n\n")
              joinedword="".join(wrdguessed)
              print(joinedword)

              try:
                  plyrguess= str(input("\nPlease choose a letter between A and Z\n"))
              except:
                  print("That is not valid answer please choose a letter between A and Z")
                  continue
              else:
                  if not plyrguess.isalpha():
                      print("That is not valid answer please choose a letter between A and Z")
                      continue
                  elif len (plyrguess)>1:
                      print("That is not valid answer please choose a letter between A and Z")
                      continue
                  else:
                      pass
              lttrguessed.append(plyrguess)

              for letter in range(len(ftword)):
                  if plyrguess==ftword[letter]:
                      wrdguessed[letter]=plyrguess

              if plyrguess not in ftword:
                  attempts=attempts-1
                  if attempts==9:
                      print("\n")
                      hangmanstart()
                  if attempts==8:
                      print("\n")
                      hangman2()
                  if attempts==7:
                      print("\n")
                      hangman3()
                  if attempts==6:
                      print("\n")
                      hangman4()                                            
                  if attempts==5:
                      print("\n")
                      hangman5()                
                  if attempts==4:
                      print("\n")
                      hangman6()
                  if attempts==3:
                      print("\n")
                      hangman7()
                  if attempts==2:
                      print("\n")
                      hangman8()
                  if attempts==1:
                      print("\n")
                      hangman9()
                  if attempts==0:
                      print("\n")
                      hangman10()
                      plyagain=input("do you want to play again")
                      if plyagain=="y":
                          ftbllgame()
                      elif plyagin=="n":
                          title()
              if "-" not in wrdguessed:
                  print(wrdguessed)
                  print("Congratulations on guessing the word")

                  plyagain=input("do you want to play again y or n?")
                  plyans=['y','n','Y','N']
                  while plyagain not in plyans:
                      print("please enter a valid y or n answer")
                      plyagain=input("do you want to play again y or n?")
                  if plyagain=="y" or "Y":
                      ftbllgame()
                  if plyagain=="n" or "N":
                      title()







def tvgame():
          global tvshows
          import random
          tvword=random.choice(tvshows).lower()
          plyrguess= None
          lttrguessed=[]
          wrdguessed=[]
          for letter in tvword:
              wrdguessed.append("-")
          addedword= None
          chsnword= len(tvword)-1
          attempts=10

          while (attempts!=0 and "-" in wrdguessed):
              print ("You have ",attempts,"left")
              joinedword="".join(wrdguessed)
              print(joinedword)

              try:
                  plyrguess= str(input("\nPlease choose a letter between A and Z\n"))
              except:
                  print("That is not valid answer please choose a letter between A and Z")
                  continue
              else:
                  if not plyrguess.isalpha():
                      print("That is not valid answer please choose a letter between A and Z")
                      continue
                  elif len (plyrguess)>1:
                      print("That is not valid answer please choose a letter between A and Z")
                      continue
                  else:
                      pass
              lttrguessed.append(plyrguess)

              for letter in range(len(tvword)):
                  if plyrguess==tvword[letter]:
                      wrdguessed[letter]=plyrguess

              if plyrguess not in tvword:
                  attempts=attempts-1

              if "-" not in wrdguessed:
                  print("you finished the word")






def title():
    import time
    time.sleep(1)
    print(" "*14,"-"*52)
    print("  "*12,"*"*10,"HANGMAN","*"*10)
    print(" "*14,"-"*52)
    print("\n")
    print("\n")
    time.sleep(1)
    number=(['1','2'])
    number2=(['1','2','3','4'])
    choice= input("1)HANGMAN\n2)QUIT\nPLEASE CHOOSE FROM THE MENU\n")
    while choice not in number:
        print ("THE VALUE YOU ENTERED IS INVALID\n")
        choice=input("1)HANGMAN\n2)QUIT\nPLEASE CHOOSE FROM THE MENU\n")
    else:
        if choice=='1':
            choice2=input("please select a category:\n1)Football players names\n2)Tv shows\n3)Anime shows\n4)Anime characters\n")
        while choice2 not in number2:
            print ("THE VALUE YOU ENTERED IS INVALID\n")
            choice2=input("1)HANGMAN\n2)QUIT\nPLEASE CHOOSE FROM THE MENU\n")
        if choice2 == "1":
            ftbllgame()
        if choice2 == "2":
            tvgame()
        if choice2 == "3":
            AnimeShowGame()
        if choice2 == "4":
            AnimeCharacterGame()
        elif choice=='2':
            quit()

title()
    
