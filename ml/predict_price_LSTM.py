import pandas
import numpy
from keras.layer.core import Dense, Activation, Dropout
from keras.layer.recurrent import LSTM
from keras.models import Sequential
import matplotlib.pyplot as plt

CONST_TRAINING_SEQUENCE_LENGTH = 60
CONST_TESTING_CASES = 5
#change

def dataNormalization(data):
    return [(datum - data[0]) / data[0] for datum in data]


def dataDeNormalization(data, base):
    return [(datum + 1) * base for datum in data]


def getDeppLearningData(ticker):
    # Step 1. Load data
    data = panads.read_csv('./Data/IntradayUS/' +
                           ticker + '.csv')['close'].tolist()

    # Step 2. Building training data
    dataTraining = []
    for i in range(len(data) - CONST_TRAINING_SEQUENCE_LENGTH * CONST_TESTING_CASES):
        dataSegment = data[i:i + CONST_TRAINING_SEQUENCE_LENGTH + 1]
        dataTraining.append(dataNormalization(dataSegment))
    dataTraining = numpy.array(dataTraining)
    numpy.random.shuffle(dataTraining)
    X_Training = dataTraining[:, :-1]
    Y_Training = dataTraining[:, -1]

    # Step 3. Building testing data
    X_Testing = []
    Y_Testing_Base = []
    for i in range(CONST_TESTING_CASES, 0, -1):
        dataSegment = data[-(i + 1) * CONST_TRAINING_SEQUENCE_LENGTH:-
                           i * CONST_TRAINING_SEQUENCE_LENGTH]
        Y_Testing_Base.append(dataSegment[0])
        X_Testing.append(dataNormalization(dataSegment))
    Y_Testing = data[-CONST_TESTING_CASES * CONST_TRAINING_SEQUENCE_LENGTH:]

    X_Testing = numpy.array(X_Testing)
    Y_Testing = numpy.array(Y_Testing)

    # Step 4. Reshape for deep learning
    X_Training = numpy.reshape(
        X_Training, (X_Training.shape[0], X_Training.shape[1], 1))
    X_Testing = numpy.reshape(
        X_Testing, (X_Testing.shape[0], X_Testing.shape[1], 1))

    return X_Training, Y_Training, X_Testing, Y_Testing


def predictLSTM(ticker):
    # Step 1. Load data
    X_Training, Y_Training, X_Testing, Y_Testing = getDeppLearningData(ticker)
    print(Y_Testing)

    # Step 2. Build model

    # Step 3. Train model

    # Step 4. Predict

    # Step 5. De-nomalize

    # Step 6. Plot


predictLSTM(ticker='AAPL')
