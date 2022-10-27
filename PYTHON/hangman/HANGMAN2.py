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
    print("     |  / | \"")     
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
    print("     |  / | \"")     
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
    print("     |  / | \"")     
    print("     |   / \"")
    print("     |  /   \"")
    print("     |    ")
    print("     |    ")
    print("   -----------")
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
    choice= input("1)HANGMAN\n2)QUIT\nPLEASE CHOOSE FROM THE MENU\n")
    while choice not in number:
        print ("THE VALUE YOU ENTERED IS INVALID\n")
        choice=input("1)HANGMAN\n2)QUIT\nPLEASE CHOOSE FROM THE MENU\n")
    else:
        if choice=='1':
            (hangman())
        elif choice=='4':
            quit()

    
