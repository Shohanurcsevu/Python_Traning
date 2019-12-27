from tkinter import*
from tkinter import messagebox

top = Tk()
top.geometry("500x500")
def printSomething():
    d= messagebox.showinfo('Hi! Done')

B = Button(top, text='Click', command= printSomething)
B.place(x=250,y=250)
top.mainloop()