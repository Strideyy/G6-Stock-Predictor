import os
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout 
import math
from sklearn.metrics import mean_squared_error


def load_stock_data(user_choice):
    root_path = "https://raw.githubusercontent.com/Strideyy/G6-Stock-Predictor/master/sample/"
    csv_path = os.path.join(root_path, user_choice + ".csv")
    print(csv_path)
    
    return pd.read_csv(csv_path, usecols=['Close'])


numpy.random.seed(7) # Fix seed for reporoducibility 
look_back = 1 # Number of time-steps to learn from

# Converting dataset to matrix, X=t (sample data at current time step) Y=t (x+1 sample at next time step)
def create_dataset(dataset, look_back):
    data_x, data_y = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        data_x.append(a)
        data_y.append(dataset[i+look_back, 0])
    
    return numpy.array(data_x), numpy.array(data_y)


def split_data(user_choice):
    stock_data = load_stock_data(user_choice)

    dataset = stock_data.values
    dataset = dataset.astype('float32')

    scaler = MinMaxScaler(feature_range=(0, 1))  # Scaler to normalise for better performance
    dataset = scaler.fit_transform(dataset)

    train_size = int(len(dataset) * 0.70)  # Training set size: 70%
    test_size = len(dataset) - train_size  # Test set size: remaining 30%
    train, test = dataset[0:train_size, :], dataset[train_size:len(dataset), :]
    print("Training set size:", len(train), "\nTest set size:", len(test))

    train_x, train_y = create_dataset(train, look_back)
    test_x, test_y = create_dataset(test, look_back)

    train_x = numpy.reshape(train_x, (train_x.shape[0], train_x.shape[1], 1)) # One time step per sample of data
    test_x = numpy.reshape(test_x, (test_x.shape[0], test_x.shape[1], 1))

    return train_x, test_x, train_y, test_y, dataset, scaler


def create_model(look_back):
    model = Sequential()
    model.add(LSTM(units = 4, input_shape=(1, look_back))) # Neural layer (4 neurons)
    model.add(Dense(1)) # Output layer
    model.compile(loss='mean_squared_error', optimizer='adam')
    
    return model 


def train_test(look_back, train_x, test_x, train_y, test_y, dataset, scaler):
    model = create_model(look_back)
    # Epochs = Number of times model is trained, more epochs is longer runtime
    model.fit(train_x, train_y, epochs=30, batch_size=1, verbose=0) 
    
    train_predict= model.predict(train_x)
    test_predict = model.predict(test_x)
    # The data needs to be in the same format as the original to get accurate RMSE
    train_predict = scaler.inverse_transform(train_predict)
    train_y = scaler.inverse_transform([train_y])
    test_predict = scaler.inverse_transform(test_predict)
    test_y = scaler.inverse_transform([test_y])

    # Calculate RMSE for model fit evaluation
    train_score = math.sqrt(mean_squared_error(train_y[0], train_predict[:, 0]))
    print('Train Score: %.2f RMSE' % (train_score))
    test_score = math.sqrt(mean_squared_error(test_y[0], test_predict[:, 0]))
    print('Test Score: %.2f RMSE' % (test_score))

    return train_predict, test_predict, dataset, scaler


def plot(train_predict, test_predict, dataset, scaler):
    train_predict_plot = numpy.empty_like(dataset)
    train_predict_plot[:, :] = numpy.nan
    train_predict_plot[look_back:len(train_predict)+look_back, :] = train_predict
    # shift test predictions for plotting
    test_predict_plot = numpy.empty_like(dataset)
    test_predict_plot[:, :] = numpy.nan
    test_predict_plot[len(train_predict)+(look_back*2)+1:len(dataset)-1, :] = test_predict
    
    # Return data to be used in UI line graph
    return train_predict_plot, test_predict_plot  
