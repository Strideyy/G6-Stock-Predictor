from tkinter import *
import csv
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


filepath = '/Users/Dell/Desktop/ML_project/companies.csv'
File = open (filepath)
Reader = csv.reader(File)

#####################################################################

#reading the CSV file and implement a line graph 

df = pd.read_csv('/Users/Dell/Desktop/ML_project/AAPL.csv') 
fig = px.line(df, x = 'Date', y = 'Close', title='Apple Share Prices over time (2014)')



#######################################################################
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
#Line graph   
# Year = Data_AAPL[0] #x axis
# Unemployment_Rate = Data_AAPL[1] #y axis
# plt.figure(figsize=(16,8))  
# plt.plot(Year, Unemployment_Rate)
# plt.title('Unemployment Rate Vs Year')
# plt.xlabel('Year')
# plt.ylabel('Unemployment Rate')
##############################################################################
def showTheGraph():
    fig.show()
   # myLabel = Label(window,text=clicked.get()).pack()#show on the graph

Data_Companies = list(Reader)

clicked=StringVar()
clicked.set(Data_Companies[0])


stockEntry = OptionMenu(window , clicked, Data_Companies[0],Data_Companies[1] )
stockEntry.place(x=20, y=75)

stockEntryButton = Button(window,text="Enter",command=showTheGraph)
stockEntryButton.place(x=150, y=75)

stockEntryLabel = Label(window, text="choose the Company (Symbol):")
stockEntryLabel.place(x=20, y=50)


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
graphLabel1 = Label(window, text="Current Performance:")
graphLabel1.place(x=1000, y=50)

graphLabel2 = Label(window, text="Predicted Performance:")
graphLabel2.place(x=1000, y=350)
##############################################################################

window.mainloop() #Run window