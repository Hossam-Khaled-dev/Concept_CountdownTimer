# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 14:54:29 2021

@author: Concept Team
"""
import threading
from tkinter import * 
import winsound

import MyLabel

SharedGlobalflag = 0
x = None

def set_text(text,e):
    e.delete(0,END)
    e.insert(0,text)
    return


def stopThread():
    global SharedGlobalflag 
    SharedGlobalflag = 1
    
def threadAport():
    if SharedGlobalflag == 1:
        set_text(0,MyLabel.hoursLabel)
        set_text(0,MyLabel.minutsLabel)
        set_text(0,MyLabel.secondsLabel)
        return 1
        #x.join()
        #button["state"] = "normal" #Enable Button Again
def setdata(n):
    set_text(int(n/3600),MyLabel.hoursLabel)
    set_text( int((n%3600)/60) ,MyLabel.minutsLabel )
    set_text(int(n%60),MyLabel.secondsLabel)
    
def sound(duration,freq):
   for  i in range(7):
       winsound.Beep(freq+(i*50), duration+(i*50))   
   winsound.Beep(freq, duration+1000)