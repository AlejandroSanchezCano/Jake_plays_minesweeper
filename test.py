from tkinter import *
from PIL import Image
from PIL import ImageTk

tk = Tk()
flag = PhotoImage('a.png').zoom(200)
b = Button(image = flag, height=400, width = 400)
b.place(relx=0.5, rely=0.5, anchor='center')
tk.mainloop()


tk = Tk()
img = Image.open("flag.png")
img = img.resize((50,50))
photoImg =  ImageTk.PhotoImage(img)
b = Button(image = photoImg, height=400, width = 400)
b.place(relx=0.5, rely=0.5, anchor='center')
tk.mainloop()
