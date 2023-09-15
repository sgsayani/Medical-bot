# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 18:13:16 2021

@author: hrith
"""

#Creating GUI with tkinter
import tkinter
from tkinter import *
from chatbot import chatbot_response
from PIL import ImageTk,Image

def go():
    def send():
        msg = EntryBox.get("1.0",'end-1c').strip()
        EntryBox.delete("0.0",END)
        if msg != '':
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "You: " + msg + '\n\n')
            ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
            res = chatbot_response(msg)
            ChatLog.insert(END, "friend: " + res + '\n\n')
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
    
    base = Tk()
    base.title("Chatbot")
    base.geometry("400x500")
    base.resizable(width=False, height=False)
    #Create Chat window
    ChatLog = Text(base, bd=0, bg="#57C34D", height="8", width="50", font="Arial",)
    ChatLog.config(state=DISABLED)
    #Bind scrollbar to Chat window
    scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
    ChatLog['yscrollcommand'] = scrollbar.set
    #Create Button to send message
    SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                        bd=0, bg="#A52A2A", activebackground="#3c9d9b",fg='#ffffff',
                        command= send )
    
    #Create the box to enter message
    EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
    #EntryBox.bind("<Return>", send)
    #Place all components on the screen
    scrollbar.place(x=376,y=6, height=386)
    ChatLog.place(x=6,y=6, height=386, width=370)
    EntryBox.place(x=128, y=401, height=90, width=265)
    SendButton.place(x=6, y=401, height=90)
    base.mainloop()