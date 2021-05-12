"""
Created on Wed Mar 17 14:31:14 2021
@author: Tom
"""

from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import plotly.express as px

import main

window = Tk() #Create window
window.title("G6 Stocks Predictor") #Title of window
window.geometry("1280x720") #Resize window
#window.configure(background = "grey") #Can alter background of window

title = Label(window, text="NASDAQ Stocks Predictor", anchor=N) #Add title label
title.config(font=("TkDefaultFont", 18)) #Set font and font size
title.pack(pady=20) #Pack label with spacing

closeButton = Button(window, text="Close App", anchor=CENTER, command=window.destroy) #Add exit button
closeButton.place(x=1200, y=680) #Place button bottom left of app

##############################################################################
stockEntryLabel = Label(window, text="Enter Company Choice (Symbol):")
stockEntryLabel.place(x=20, y=50)

stockEntry = Entry(window, width=20) #Needs validation against dataset
stockEntry.place(x=20, y=75)

#def getEntry (): #Collects the input from the entry box
#stockEntryChoice = stockEntry.get()

def showTheGraph():
    #url ='https://raw.githubusercontent.com/Strideyy/G6-Stock-Predictor/master/sample/' + stockEntry.get() + '.csv'
    index = main.split_data()
    result = main.train_test(1, index[0],index[1],index[2],index[3],index[4],index[5])
    plot_result = main.plot(result[0],result[1],result[2],result[3]) 
    #fig = px.line(df, x = 'Date', y = 'Close', title='Closing Share Prices Over Time')
    plt.plot(plot_result[0])
    plt.plot(plot_result[1])
    plt.show()
    
stockEntryButton = Button(window, text="Enter", anchor=CENTER, command=showTheGraph) #Runs command for entry input
stockEntryButton.place(x=150, y=75)

##############################################################################
stockPurchaseLabel = Label(window, text="Enter Number Of Shares To Buy (At Most Recent Closing Price):")
stockPurchaseLabel.place(x=20, y=100)

stockPurchase = Entry(window, width=20)
stockPurchase.place(x=20, y=125)

stockPurchaseButton = Button(window, text="Enter", anchor=CENTER) #Needs command
stockPurchaseButton.place(x=150, y=125)
##############################################################################
lossStoppageLabel = Label(window, text="Enter Loss Stoppage Amount (Optional):")
lossStoppageLabel.place(x=20, y=150)

lossStoppage = Entry(window, width=20)
lossStoppage.place(x=20, y=175)

lossStoppageButton = Button(window, text="Enter", anchor=CENTER) #Needs command
lossStoppageButton.place(x=150, y=175)
##############################################################################
sellPointLabel = Label(window, text="Enter The Point You Wish To Sell At (Optional):")
sellPointLabel.place(x=20, y=200)

sellPoint = Entry(window, width=20)
sellPoint.place(x=20, y=225)

sellPointButton = Button(window, text="Enter", anchor=CENTER) #Needs command
sellPointButton.place(x=150, y=225)
##############################################################################

window.mainloop() #Run window
