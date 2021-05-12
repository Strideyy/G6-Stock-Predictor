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
window.geometry("1280x800") #Resize window
#window.configure(background = "grey") #Can alter background of window

title = Label(window, text="NASDAQ Stocks Predictor", anchor=N) #Add title label
title.config(font=("TkDefaultFont", 18)) #Set font and font size
title.pack(pady=20) #Pack label with spacing

closeButton = Button(window, text="Close App", anchor=CENTER, command=window.destroy) #Add exit button
closeButton.place(x=1200, y=760) #Place button bottom left of app

##############################################################################
stockEntryLabel = Label(window, text="Enter Company Choice (Symbol):")
stockEntryLabel.place(x=20, y=50)

stockEntry = Entry(window, width=20) #Needs validation against dataset
stockEntry.place(x=20, y=75)

def showTheGraph(): #Function to display historical data for chosen company
    url ='https://raw.githubusercontent.com/Strideyy/G6-Stock-Predictor/master/sample/' + stockEntry.get() + '.csv'
    df = pd.read_csv(url, index_col=-1)
    #Reads the chosen dataset from github repo into a pandas dataframe

    figure = plt.Figure(figsize=(7.75,3.5), dpi=100) #Graph size and resolution
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, window)
    chart_type.get_tk_widget().place(x=500, y=50) #Where the graph is placed on the window
    df = df[['Date','Close']].groupby('Date').sum() #X and Y axis
    df.plot(kind='line', legend=True, ax=ax) #Chart type
    ax.set_title('Closing Share Prices Over Time')

    #fig = px.line(df, x = 'Date', y = 'Close', title='Closing Share Prices Over Time')
    #fig.show() 
    #Online graph method
    
stockEntryButton = Button(window, text="Enter", anchor=CENTER, command=showTheGraph) #Runs showTheGraph function
stockEntryButton.place(x=150, y=75)

##############################################################################

runModelLabel = Label(window, text="Click Here To Run LSTM Model (may take a few minutes)")
runModelLabel.place(x=20, y=100)

def showModelGraph(): #Funcion to run main.py to run and train LSTM model, accuracy score is displayed in console
    index = main.split_data(stockEntry.get())
    result = main.train_test(1, index[0],index[1],index[2],index[3],index[4],index[5])
    plot_result = main.plot(result[0],result[1],result[2],result[3]) 

    fig = plt.figure(figsize = (10.75,4.5)) #Graph size and resolution
    graph = FigureCanvasTkAgg(fig, window)
    graph.draw()
    graph.get_tk_widget().place(x=500, y=410) #Where the graph is placed on the window
    plt.xlabel('Time Step',fontsize=18)
    plt.ylabel('Close Price',fontsize=18) #X and Y axis
    plt.plot(plot_result[0], "-b", label="Training Data")
    plt.plot(plot_result[1], "-r", label="Test Data")
    plt.legend(loc="upper right") #Legends for colour coding the training and test data

runModelButton = Button(window, text="Enter", anchor=CENTER, command=showModelGraph)
runModelButton.place(x=150, y=125)
##############################################################################

##############################################################################
# stockPurchaseLabel = Label(window, text="Enter Number Of Shares To Buy (At Most Recent Closing Price):")
# stockPurchaseLabel.place(x=20, y=150)

# stockPurchase = Entry(window, width=20)
# stockPurchase.place(x=20, y=175)

# stockPurchaseButton = Button(window, text="Enter", anchor=CENTER) #Needs command
# stockPurchaseButton.place(x=150, y=175)
# ##############################################################################
# lossStoppageLabel = Label(window, text="Enter Loss Stoppage Amount (Optional):")
# lossStoppageLabel.place(x=20, y=200)

# lossStoppage = Entry(window, width=20)
# lossStoppage.place(x=20, y=225)

# lossStoppageButton = Button(window, text="Enter", anchor=CENTER) #Needs command
# lossStoppageButton.place(x=150, y=225)
# ##############################################################################
# sellPointLabel = Label(window, text="Enter The Point You Wish To Sell At (Optional):")
# sellPointLabel.place(x=20, y=250)

# sellPoint = Entry(window, width=20)
# sellPoint.place(x=20, y=275)

# sellPointButton = Button(window, text="Enter", anchor=CENTER) #Needs command
# sellPointButton.place(x=150, y=275)
##############################################################################

window.mainloop() #Run window