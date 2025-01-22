from tkinter import *

window = Tk()

window.title("Welcome to DHGWUIDHIU")
window.geometry('350x200')

def topwin():
    top = Toplevel()
    top.title("New Window")
    top.geometry('350x200')


    lbl = Label(top, text="Hello")
    lbl.pack()


    top.mainloop()


label = Label(window, text="Hello")
label.pack()

Button = Button(window, text="Open new window", command=topwin)
Button.pack()

window.mainloop()