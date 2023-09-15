import tkinter
from tkinter import *
from chatgui import go
from PIL import Image, ImageTk
t=Tk()

t.title("KIWI")
t.geometry("400x500")
t.resizable(width=False, height=False)
t.iconbitmap(r'KIWI.ico')
bg=PhotoImage(file="KIWII.png")

label=Label(t,image=bg)
label.place(x=0,y=0)

def close():
    t.destroy()
button=Button(t,text="Enter",height=2,borderwidth=3,width=20, font=("Lora", '14', 'bold'), bd=3, bg="#32CD32", activebackground="#7CFC00", fg='#ffffff', command=go)
button.place(x=86,y=400)
frame = Frame(t, relief=RAISED, borderwidth=1)
frame.pack(fill=BOTH, expand=False)

t.mainloop()
