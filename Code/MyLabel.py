# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 16:29:49 2021

@author: Concept Team
"""
from tkinter import filedialog
from tkinter import * 
import tkinter
from PIL import Image, ImageTk



# GLOBAL Path Diffintion

background_file = 'Background\_background2.gif'
icon_file       = 'icon\icon.ico'


root = None
f12 = None
hoursLabel = None
minutsLabel = None
secondsLabel = None

class MyLabel(Label):
	def __init__(self, master, filename):
		im = Image.open(filename)
		w,h=im.size
		master.geometry("%dx%d" % (w, h))
		seq =  []
		try:
			while 1:
				seq.append(im.copy())
				im.seek(len(seq)) # skip to next frame
		except EOFError:
			pass # we're done

		try:
			self.delay = im.info['duration']
		except KeyError:
			self.delay = 100
            
		first = seq[0].convert('RGBA')
		self.frames = [ImageTk.PhotoImage(first)]

		Label.__init__(self, master, image=self.frames[0])

		temp = seq[0]
		for image in seq[1:]:
			temp.paste(image)
			frame = temp.convert('RGBA')
			self.frames.append(ImageTk.PhotoImage(frame))

		self.idx = 0

		self.cancel = self.after(self.delay, self.play)

	def play(self):
		self.config(image=self.frames[self.idx])
		self.idx += 1
		if self.idx == len(self.frames):
			self.idx = 0
		self.cancel = self.after(self.delay, self.play)  
        
        
def gui():
    global root,f12,hoursLabel,minutsLabel,secondsLabel
    try:
        root = Tk()
    except:
        root = tkinter.Toplevel()
    root.title("Countdown")
# Read Image And Icon
    im = Image.open(background_file)
    root.iconbitmap(icon_file)
    w,h=im.size
    root.maxsize(w,h)
    root.minsize(w,h) 

# Background
    anim = MyLabel(root,background_file)
    anim.place(x=0, y=0)
    frame = Frame(root)
    frame.place(x=315, y=520)
    frame.config(relief=RIDGE)
    #F11
    f11 = ttk.Frame(frame)
    f11.pack()
    f11.config(relief=RIDGE)
    #F12
    f12 = ttk.Frame(frame)
    f12.pack()
    f12.config(relief=RIDGE)
    
    
    #hours
    hoursLabel=ttk.Entry(f11,width=3,font=('Arial',10))
    hoursLabel.grid(row=0,column=0,sticky=NSEW)
    hoursLabel.insert(END, '0')
    #minuts
    minutsLabel=ttk.Entry(f11,width=3,font=('Arial',10))
    minutsLabel.grid(row=0,column=1,sticky=NSEW)
    minutsLabel.insert(END, '0')
    #minuts
    secondsLabel=ttk.Entry(f11,width=3,font=('Arial',10))
    secondsLabel.grid(row=0,column=3,sticky=NSEW)
    secondsLabel.insert(END, '0')

    
