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


ROOT_PATH = ROOT_PATH = "https://raw.githubusercontent.com/Strideyy/G6-Stock-Predictor/master/sample/"


numpy.random.seed(7)


def load_stock_data(root_path=ROOT_PATH):
    csv_path = os.path.join(root_path, "SNA.csv") # MUST be a .csv located in /master/sample
    return pd.read_csv(csv_path, usecols=['Close'])


look_back = 1


def create_dataset(dataset, look_back):
    data_x, data_y = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        data_x.append(a)
        data_y.append(dataset[i+look_back, 0])
    return numpy.array(data_x), numpy.array(data_y)


stock_data = load_stock_data()

dataset = stock_data.values
dataset = dataset.astype('float32')

scaler = MinMaxScaler(feature_range=(0, 1))  # Normalise for better performance
dataset = scaler.fit_transform(dataset)

train_size = int(len(dataset) * 0.70)  # Training set size: 70%
test_size = len(dataset) - train_size  # Test set size: remaining 30%
train, test = dataset[0:train_size, :], dataset[train_size:len(dataset), :]
print("Training set size:", len(train), "\nTest set size:", len(test))

trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)

trainX = numpy.reshape(trainX, (trainX.shape[0], trainX.shape[1], 1))
testX = numpy.reshape(testX, (testX.shape[0], testX.shape[1], 1))


def create_model(look_back):
    model = Sequential()
    model.add(LSTM(4, input_shape=(1, look_back)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model 


def train_test(look_back, trainX, testX, trainY, testY, dataset):
    model = create_model(look_back)
    model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)
    
    trainPredict = model.predict(trainX)
    testPredict = model.predict(testX)

    trainPredict = scaler.inverse_transform(trainPredict)
    trainY = scaler.inverse_transform([trainY])
    testPredict = scaler.inverse_transform(testPredict)
    testY = scaler.inverse_transform([testY])

    trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:, 0]))
    print('Train Score: %.2f RMSE' % (trainScore))
    testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:, 0]))
    print('Test Score: %.2f RMSE' % (testScore))

    plot(trainPredict, testPredict, dataset)


def plot(trainPredict, testPredict, dataset):
    trainPredictPlot = numpy.empty_like(dataset)
    trainPredictPlot[:, :] = numpy.nan
    trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
    # shift test predictions for plotting
    testPredictPlot = numpy.empty_like(dataset)
    testPredictPlot[:, :] = numpy.nan
    testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict
    # plot baseline and predictions
    plt.plot(scaler.inverse_transform(dataset))
    plt.plot(trainPredictPlot)
    plt.plot(testPredictPlot)
    plt.show()


train_test(look_back, trainX, testX, trainY, testY, dataset)