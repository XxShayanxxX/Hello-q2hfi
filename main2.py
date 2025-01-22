from tkinter import *
from PIL import Image, ImageTk  

window = Tk()   

window.title("Welcome to DHGWUIDHIEF")
window.geometry('350x200')
window.configure(bg='black')

upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))

image = ImageTk.PhotoImage(upload)

label = Label(window, image=image)  

label.place(x = 180 , y = 20 )

label1 = Label(window, text="Hello" ) 
label1.place(relax = 0.5, y = 150, anchor = CENTER)


window.mainloop()

