# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 00:36:04 2021

@author: Debashis Show
"""

import tkinter
from tkinter import *
from chatbots import chatbot_response
from p import bola
import speech_recognition as sr
import pyttsx3
r = sr.Recognizer() 
  
# Function to convert text to
# speech
def SpeakText(command):
      
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
      
def go():
    def send():
        msg = EntryBox.get("1.0",'end-1c').strip()

        EntryBox.delete("0.0",END)
        if msg != '':
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "You: " + msg + '\n\n')
            ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
            res = chatbot_response(msg)
            ChatLog.insert(END, "Kiwi: " + res + '\n\n')
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
            SpeakText(res)
    def speech():
        msg1=bola()
        print(msg1)
        if msg1!=' ':
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "You: " + msg1 + '\n\n')
            ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
            res = chatbot_response(msg1)
            ChatLog.insert(END, "Kiwi: " + res + '\n\n')
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)
            SpeakText(res)
    base = Tk()
    base.title("KIWI")
    base.geometry("400x500")
    base.resizable(width=FALSE, height=FALSE)
    base.iconbitmap(r'KIWI.ico')
    #Create Chat window
    ChatLog = Text(base, bd=1, bg="#D0F0C0", height="8", width="50", font="Roboto, 14",)
    ChatLog.config(state=DISABLED)
    #Bind scrollbar to Chat window
    scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="hand2",troughcolor="#006400",)
    ChatLog['yscrollcommand'] = scrollbar.set
    #Create Button to send message
    SendButton = Button(base, font=("Lora",16,'bold'), text="Send", width="12", height=5,
                        bd=2, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= send )
    #create a button to exit from the window.
    ExitButton = Button(base, font=("Lora",10,'bold'), text="Exit", width="05", height=5, bd=2, bg="#354A21", activebackground="#99EDC3",fg='#ffffff', command= exit)
    SpeechButton = Button(base, font=("Lora",10,'bold'), text="Speak", width="05", height=5, bd=2, bg="#354A21", activebackground="#99EDC3",fg='#ffffff', command= speech)

    #Create the box to enter message
    EntryBox = Text(base, bd=1, bg="#90EE90",width="29", height="5", font="Arial")
    #EntryBox.bind("<Return>", send)
    #Place all components on the screen
    scrollbar.place(x=376,y=6, height=386)
    ChatLog.place(x=6,y=6, height=386, width=370)
    EntryBox.place(x=6, y=401, height=90, width=200)
    SendButton.place(x=210, y=401, height=90, width=100)
    ExitButton.place(x=316, y=450, height=39, width=50)
    SpeechButton.place(x=316, y=401, height=39, width=50)
    base.mainloop()
