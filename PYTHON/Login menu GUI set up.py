from tkinter import *
def ENDLESS():
    print("ENDLESS")

def LEVELS():
    print("LEVELS")

def SHOP():
    print("SHOP")

def BACK():
    print("BACK")
window=Tk()

window.title('MAIN MENU')
topFrame= Frame(window)
topFrame.pack()
bottomFrame=Frame(window)
bottomFrame.pack(side=BOTTOM)

photo=PhotoImage(file='mangekyou_sharingan___sasuke_by_diab0lik5.png')
button1= Button(topFrame,text="ENDLESS",fg="red", height=15, width=30, command=ENDLESS)
button2= Button(topFrame,text="LEVELS",fg="blue",height=15, width=30,command=LEVELS)
button3= Button(bottomFrame,text="SHOP",fg="black",height=15, width=30,command=SHOP)
button4= Button(bottomFrame,text="BACK",fg="gold",height=15, width=30,command=BACK)

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)





window.mainloop()
