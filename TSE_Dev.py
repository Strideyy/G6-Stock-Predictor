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

def showTheGraph():
    url ='https://raw.githubusercontent.com/Strideyy/G6-Stock-Predictor/master/sample/' + stockEntry.get() + '.csv'
    df = pd.read_csv(url, index_col=-1)

    figure = plt.Figure(figsize=(7.75,3.5), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, window)
    chart_type.get_tk_widget().place(x=500, y=50)
    df = df[['Date','Close']].groupby('Date').sum()
    df.plot(kind='line', legend=True, ax=ax)
    ax.set_title('Closing Share Prices Over Time')

    #fig = px.line(df, x = 'Date', y = 'Close', title='Closing Share Prices Over Time')
    #fig.show()
    
stockEntryButton = Button(window, text="Enter", anchor=CENTER, command=showTheGraph) #Runs command for entry input
stockEntryButton.place(x=150, y=75)

##############################################################################

stockPurchaseLabel = Label(window, text="Click Here To Run LSTM Model (may take a few minutes)")
stockPurchaseLabel.place(x=20, y=100)

def showModelGraph():
    index = main.split_data(stockEntry.get())
    result = main.train_test(1, index[0],index[1],index[2],index[3],index[4],index[5])
    plot_result = main.plot(result[0],result[1],result[2],result[3]) 

    fig = plt.figure(figsize = (10.75,4.5)) 
    graph = FigureCanvasTkAgg(fig, window)
    graph.draw()
    graph.get_tk_widget().place(x=500, y=410)
    plt.xlabel('Time Step',fontsize=18)
    plt.ylabel('Close Price',fontsize=18)
    plt.plot(plot_result[0], "-b", label="Training Data")
    plt.plot(plot_result[1], "-r", label="Test Data")
    plt.legend(loc="upper right")

##############################################################################

window.mainloop() #Run window