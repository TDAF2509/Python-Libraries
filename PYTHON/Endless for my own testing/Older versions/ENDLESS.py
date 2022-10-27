
if 101>=100:
    print("h")


from tkinter import *
def ENDLESS():
    print("RULES TO ADD WHEN I THINK OF THEM PROPERLY")
    window=Tk()
    canvas=Canvas(window,width=window.winfo_screenwidth(),height=window.winfo_screenheight())
    canvas.pack()
    #window.geometry('canvas')

    ball=canvas.create_oval(10,450,60,500,fill="blue")

    window.wm_attributes('-alpha',0.7)
    
    window.title('ENDLESS')


    window.mainloop()





ENDLESS()
