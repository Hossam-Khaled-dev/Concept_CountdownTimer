# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 14:54:29 2021

@author: Concept Team
"""

from tkinter import filedialog
from tkinter import * 
from tkinter.ttk import  Style,Treeview
import MyLabel
import time
import threading
import helper

   
def coutdown(n):
    if n ==0:
        helper.setdata(n)
        return 0
    else:
       helper.setdata(n)        # Set Gui Data
       if helper.threadAport(): # Stop Thread
            return 0
       time.sleep(1)
       coutdown(n-1) 

def caller(n):
    coutdown(n)
    enableButton(startButton)  #Enable Button Again
    helper.sound(70,100)
       
def startThread(h,m,s):
    disableButton(startButton)  # Disable Button to Forbidine Multi Threading
    n = ( h*3600 )+ ( m *60 )+ s
    helper.SharedGlobalflag = 0
    helper.x = threading.Thread(target=caller,args=(n,))
    helper.x.start()
    

def enableButton(button):
    button["state"] = "normal"

def disableButton(button):
    button["state"] = "disabled"
    

# Main 

MyLabel.gui()

startButton = Button(MyLabel.f12, text='STARTF',command=lambda :startThread(int(MyLabel.hoursLabel.get()),int(MyLabel.minutsLabel.get()),int(MyLabel.secondsLabel.get())), width=10, height=2)
startButton.grid(row=0,column=1,sticky=NSEW)

stopButton = Button(MyLabel.f12, text='STOP',command=lambda:helper.stopThread(), width=10, height=2)
stopButton.grid(row=0,column=2,sticky=NSEW)

MyLabel.root.mainloop()




