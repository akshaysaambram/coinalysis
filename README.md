# Coinalysis Documentation

Welcome to the documentation for Coinalysis, a Django project that utilizes LSTM machine learning (with TensorFlow and Keras) to predict cryptocurrency prices. This project fetches data using the yfinance Python library and offers virtual trading, portfolio tracking, and dynamic visualized graphs for analysis.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Predicting Cryptocurrency Prices](#predicting-cryptocurrency-prices)
   - [Virtual Trading](#virtual-trading)
   - [Portfolio Management](#portfolio-management)
   - [Coin Analysis](#coin-analysis)
4. [Data Collection](#data-collection)
5. [Machine Learning Model](#machine-learning-model)
6. [Contributing](#concense)

## Introduction
Coinalysis is a comprehensive web application built with Django that aims to provide cryptocurrency enthusiasts with valuable tools for investment decisions. The main features of Coinalysis are:

1. **Cryptocurrency Price Prediction:** Coinalysis utilizes LSTM machine learning, powered by TensorFlow and Keras, to predict cryptocurrency prices based on historical data. Users can view dynamic visualized graphs to analyze predicted prices alongside actual market prices.

2. **Virtual Trading:** The application enables users to engage in virtual trading, allowing them to buy and sell cryptocurrencies without using real money. This feature provides a risk-free environment for users to practice trading strategies.

3. **Portfolio Management:** Coinalysis empowers users to track their virtual trading activities through portfolio management. Users can monitor their holdings, track performance, and analyze investment decisions.

4. **Coin Analysis:** Coinalysis provides technical analysis indicators such as Moving Average Convergence Divergence (MACD), 100-day Exponential Moving Average (EMA), and 200-day EMA. Visualized graphs are available to help users make informed decisions.

## Installation
To run Coinalysis on your local machine, follow these steps:

1. Clone the repository from GitHub:
    ```
        git clone https://github.com/your-username/Coinalysis.git
    ```
2. Navigate to the project directory:
    ```
        cd Coinalysis
    ```

3. Create a virtual environment:
    ```
        python -m venv venv
    ```

4. Activate the virtual environment:
- On Windows: `venv\Scripts\activate`
- On macOS and Linux: `source venv/bin/activate`

5. Install the required dependencies:
    ```
        pip install -r requirements.txt
    ```

6. Run the Django development server:
    ```
        python manage.py runserver
    ```

7. Open your web browser and access the application at [http://localhost:8000/](http://localhost:8000/).

## Usage

### Predicting Cryptocurrency Prices
To predict cryptocurrency prices using Coinalysis, follow these steps:

1. Register or log in to your account.
2. Navigate to the "Predict" section.
3. Select the cryptocurrency you want to predict the price for.
4. Choose the date range for the historical data you want to use for prediction.
5. Click on the "Predict" button to get the forecasted price.

### Virtual Trading
Coinalysis provides virtual trading functionality to simulate real trading without financial risks. To use virtual trading, do the following:

1. Register or log in to your account.
2. Navigate to the "Virtual Trading" section.
3. Select the cryptocurrency you want to buy or sell.
4. Specify the quantity you want to transact.
5. Execute the trade by clicking on the "Buy" or "Sell" button.

### Portfolio Management
The portfolio management feature allows users to track their virtual trading activities. To manage your portfolio, follow these steps:

1. Register or log in to your account.
2. Navigate to the "Portfolio" section.
3. View your current holdings and their performance.
4. Analyze your past transactions and profit/loss.

### Coin Analysis
Coinalysis provides technical analysis indicators with visualized graphs. To access coin analysis, follow these steps:

1. Register or log in to your account.
2. Navigate to the "Coin Analysis" section.
3. Select the cryptocurrency you want to analyze.
4. Choose the specific technical indicators (e.g., MACD, 100EMA, 200EMA).
5. Observe the dynamically updated graphs for analysis.

## Data Collection
Coinalysis relies on the yfinance Python library to collect historical cryptocurrency price data. This library provides a simple and convenient way to fetch data from Yahoo Finance.

The data collection process involves the following steps:

1. Fetching historical price data for the selected cryptocurrencies using yfinance.
2. Preprocessing the data to handle missing values and normalize the features.
3. Splitting the data into training and testing sets.

## Machine Learning Model
The core of Coinalysis lies in its LSTM-based machine learning model, utilizing TensorFlow and Keras. LSTM is a type of recurrent neural network (RNN) that excels in sequence prediction tasks. The LSTM model is trained on the historical cryptocurrency price data collected from Yahoo Finance.

The machine learning workflow includes:

1. Designing the LSTM architecture.
2. Training the model on the preprocessed data.
3. Evaluating the model's performance on the test set.
4. Making predictions based on user input in the web application.

## Contributing
We welcome contributions to Coinalysis! If you want to contribute to the project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name for your feature/bug fix.
3. Make your changes and commit them with clear commit messages.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository.
