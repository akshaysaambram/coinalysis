import os
import numpy as np
import pandas as pd
import yfinance as yf

import shutil

import datetime as dt
from datetime import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

yf.pdr_override()

from sklearn.preprocessing import MinMaxScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM


def start_anaylysis(symbol):
    # LSTM Code

    # Load Data
    ticker = symbol # BTC-USD

    start = dt.datetime(2019, 1, 1)
    end = dt.datetime(2022, 1, 1)

    df = pdr.get_data_yahoo(ticker, start, end)

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df['Close'].values.reshape(-1, 1))

    prediction_days = 60

    x_train, y_train = [], []

    for x in range(prediction_days, len(scaled_data)):
        x_train.append(scaled_data[x - prediction_days:x, 0])
        y_train.append(scaled_data[x, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # Get the base directory of your Django project
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Define the file path for the static folder of your app
    static_path = os.path.join(BASE_DIR, 'mainapp', 'static', 'mainapp', 'models')

    # Get today's date
    today = datetime.today()

    # Format the date as DDMMYYYY
    formatted_date = today.strftime('%d%m%Y')

    coin_names = {
        'BTC-USD': 'bitcoin',
        'ETH-USD': 'etherum',
        'XRP-USD':  'xrp',
        'DOGE-USD': 'dogecoin',
    }

    coin_name = coin_names[symbol]

    # Specify the filename for your model
    filename = f'{coin_name}{formatted_date}'

    # Construct the full file path
    filepath = os.path.join(static_path, filename)

    if os.path.exists(filepath):
        from tensorflow import keras
        model = keras.models.load_model(f'{static_path}/{coin_name}{formatted_date}')
    else:
        # Build the Model
        model = Sequential()

        model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50))
        model.add(Dropout(0.2))
        model.add(Dense(units=1))

        model.compile(optimizer='adam', loss='mean_squared_error')
        model.fit(x_train, y_train, epochs=25, batch_size=32)

        other_models = [f for f in os.listdir(static_path) if os.path.isdir(os.path.join(static_path, f))]
        for other_model in other_models:
            if other_model.startswith('bitcoin'):
                shutil.rmtree(os.path.join(static_path, other_model))

        model.save(filepath)


    # Testing the Model
    test_start = dt.datetime(2022, 1, 1)
    test_end = dt.datetime.now()

    test_data = pdr.get_data_yahoo(ticker, test_start, test_end)
    actual_prices = test_data['Close'].values

    total_dataset = pd.concat((df['Close'], test_data['Close']), axis=0)

    model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].values
    model_inputs = model_inputs.reshape(-1, 1)
    model_inputs = scaler.transform(model_inputs)

    # Make Predictions on Test Data

    x_test = []

    for x in range(prediction_days, len(model_inputs)):
        x_test.append(model_inputs[x - prediction_days:x, 0])

    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

    predicted_prices = model.predict(x_test)
    predicted_prices = scaler.inverse_transform(predicted_prices)

    plt.plot(actual_prices, color='red', label=f'Actual {ticker} price')
    plt.plot(predicted_prices, color='green', label=f'Predicted price')
    plt.title(f'{ticker} Share Price')
    plt.xlabel('Time')
    plt.ylabel(f'{ticker} Share Price')
    legend = plt.legend()

    if legend:
        legend.remove()

    plt.legend()

    # Define the file path for the static folder of your app
    static_path = os.path.join(BASE_DIR, 'mainapp', 'static', 'mainapp', 'graphs')

    # Specify the filename for your image
    filename = f'{coin_name}.png'

    # Construct the full file path
    filepath = os.path.join(static_path, filename)

    plt.savefig(filepath)

    # Prediction for Very next One day
    real_data = [model_inputs[len(model_inputs) + 1 - prediction_days:len(model_inputs) + 1, 0]]
    real_data = np.array(real_data)
    real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1], 1))

    prediction = model.predict(real_data)
    prediction = scaler.inverse_transform(prediction)
    print(f"LSTM predicted {ticker} tomorrow's stock price: {prediction[0][0]:.6f}")

    return ticker, test_data.index, actual_prices, predicted_prices, f"{prediction[0][0]:.6f}"

