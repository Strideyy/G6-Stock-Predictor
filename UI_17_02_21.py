# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:31:14 2021

@author: Tom
"""

from tkinter import *

window = Tk() #Create window
window.title("G6 Stocks Predictor") #Title of window
window.geometry("1280x720") #Resize window
#window.configure(background = "grey") #Can alter background of window

title = Label(window, text="G6 Stocks Predictor", anchor=N) #Add title label
title.config(font=("TkDefaultFont", 18)) #Set font and font size
title.pack(pady=20) #Pack label with spacing

closeButton = Button(window, text="Close App", anchor=CENTER, command=window.destroy) #Add exit button
closeButton.place(x=1200, y=680) #Place button bottom left of app

##############################################################################
stockEntryLabel = Label(window, text="Enter Company Stock Choice (Symbol):")
stockEntryLabel.place(x=20, y=50)

stockEntry = Entry(window, width=20) #Needs validation against dataset
stockEntry.place(x=20, y=75)

stockEntryButton = Button(window, text="Enter", anchor=CENTER) #Needs command
stockEntryButton.place(x=150, y=75)
##############################################################################
stockPurchaseLabel = Label(window, text="Enter Share Purchase Amount:")
stockPurchaseLabel.place(x=20, y=100)

stockPurchase = Entry(window, width=20)
stockPurchase.place(x=20, y=125)

stockPurchaseButton = Button(window, text="Enter", anchor=CENTER) #Needs command
stockPurchaseButton.place(x=150, y=125)
##############################################################################

window.mainloop() #Run window
