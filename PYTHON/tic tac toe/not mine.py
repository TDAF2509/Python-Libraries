import turtle

t = turtle.Pen()
t.speed(300),t.pu(),t.goto(-150,-150),t.pd()

canvas = turtle.Screen()
canvas.setup(800,400)
canvas.title("Tic Tac Toe")

def square():
    for i in range(0,4):
        t.forward(100)
        t.left(90)

def grid():
    for i in range(0,3):
        square()
        t.forward(100)

grid(),t.pu(),t.goto(-150,-50),t.pd()
grid(),t.pu(),t.goto(-150,50),t.pd()
grid(),t.ht()

def Xs_and_Os(choice, seal):
    t.pu()
    grid_pos = {1:(-100,100), 2:(0,100),  3:(100,100),
                4:(-100,0),   5:(0,0),    6:(100,0),
                7:(-100,-100),8:(0,-100), 9:(100,-100)}
    if choice in grid_pos:
        t.setpos(grid_pos[choice])
        t.pd()
        t.write(seal, font = ("Arial",30,"bold"))

grid_choices = [1,2,3,4,5,6,7,8,9]
while grid_choices != []:
    x = canvas.numinput( "Player 1, choose a grid."," ",9,1)
    while x not in grid_choices:
        x = canvas.numinput("Player 1, choose again."," ",9,1)
    grid_choices.remove(x)
    Xs_and_Os(x,"X")

    y = canvas.numinput("\n" + "Player 2, choose a square.     "," ",9,1)
    while y not in grid_choices:
        y = canvas.numinput("\n" + "Player 2, choose a square.     "," ",9,1)
    grid_choices.remove(y)
    Xs_and_Os(y, "O")

python 
