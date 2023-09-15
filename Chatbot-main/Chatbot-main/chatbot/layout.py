import tkinter
from tkinter import *
from chatgui import go
from PIL import Image, ImageTk
t=Tk()

t.title("love")
t.geometry("400x500")
t.resizable(width=False, height=False)
bg=PhotoImage(file="chatbot.png")
label=Label(t,image=bg,height=500,width=500)
label.place(x=0,y=0)

def close():
    t.destroy()
button=Button(t,text="next",height=4,width=40,command=lambda:[close(),go()])
button.pack()
button1=Button(t,text="exit",height=4,width=40,command=close)
button1.place(x=60,y=400)
frame = Frame(t, relief=RAISED, borderwidth=1)
frame.pack(fill=BOTH, expand=False)

t.mainloop()