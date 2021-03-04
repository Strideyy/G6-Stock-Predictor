import os
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import math
from sklearn.metrics import mean_squared_error


ROOT_PATH = "C:\\Users\\John\\Downloads\\archive\\stocks\\"
# Locally stored for now, until I find a proper remote host

numpy.random.seed(7)


def load_stock_data(root_path=ROOT_PATH):
    csv_path = os.path.join(root_path, "GME.csv")
    return pd.read_csv(csv_path, usecols=[4])  # Column: Close


stock_data = load_stock_data()

# Requires Jupyter
#plt.figure(figsize=(18, 9))
#plt.plot(range(stock_data.shape[0]), (stock_data['Low']+stock_data['High'])/2.0)
#plt.xticks(range(0, stock_data.shape[0], 500), stock_data['Date'].loc[::500], rotation=45)
#plt.xlabel('Date', fontsize=18)
#plt.ylabel('Mid Price', fontsize=18)
#plt.show()

dataset = stock_data.values
dataset = dataset.astype('float32')

scaler = MinMaxScaler(feature_range=(0, 1))  # Normalise for better performance
dataset = scaler.fit_transform(dataset)

train_size = int(len(dataset) * 0.70)  # Training set size: 70%
test_size = len(dataset) - train_size  # Test set size: remaining 30%
train, test = dataset[0:train_size, :], dataset[train_size:len(dataset), :]
print("Training set size:", len(train), "\nTest set size:", len(test))


def create_dataset(dataset, look_back=1):
    data_x, data_y = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        data_x.append(a)
        data_y.append(dataset[i+look_back, 0])
    return numpy.array(data_x), numpy.array(data_y)
