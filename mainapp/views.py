import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime

from .models import Order, Transaction
from .forms import BuyForm
from django.shortcuts import get_object_or_404, render, redirect


# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')


def coins(request):
    return render(request, 'mainapp/coins.html')


def coin(request, pk):

    symbols = {
        'bitcoin': 'BTC-USD',
        'etherum': 'ETH-USD',
        'xrp':  'XRP-USD',
        'dogecoin': 'DOGE-USD',
    }

    ticker = yf.Ticker(symbols[pk])
    price_arr = ticker.history(period='1d')['Close']
    price = np.array(price_arr)[0]

    previousClose = ticker.info['previousClose']

    df = ticker.history(period='1y')
    df['Date'] = df.index.strftime('%d-%m-%Y')
    selected_df = df[['Date', 'Close']]

    ema_period = 100
    selected_df['EMA'] = selected_df['Close'].ewm(span=ema_period, adjust=False).mean()

    # Calculate the 12-day EMA
    ema_12 = df['Close'].ewm(span=12).mean()

    # Calculate the 26-day EMA
    ema_26 = df['Close'].ewm(span=26).mean()

    # Calculate the MACD line (the difference between the 12-day EMA and the 26-day EMA)
    macd_line = ema_12 - ema_26

    # Calculate the 9-day EMA of the MACD line (the signal line)
    signal_line = macd_line.ewm(span=9).mean()

    # Print the MACD values
    macd_values = pd.concat([macd_line, signal_line], axis=1)
    macd_values.columns = ['MACD Line', 'Signal Line']

    macd_values['Date'] = df['Date']

    json_data = selected_df.to_json(orient='records', date_format='iso')
    macd_data = macd_values.to_json(orient='records', date_format='iso')

    if request.method == 'POST':
        form = BuyForm(request.POST)

        if form.is_valid():
            form.instance.coin = ticker.info['name']
            form.instance.symbol = ticker.info['symbol']
            form.instance.bought_price = price
            form.instance.user = request.user
            form.save()
            return redirect('portfolio')
    else:
        form = BuyForm()

    context = {
        'info': ticker.info,
        'price': price,
        'diff': price - previousClose,
        'diff_percent': ((price - previousClose)/price)*100,
        'json_data': json_data,
        'macd_data': macd_data,

        'form': form,

        'img_path': f'mainapp/{pk}.png',
    }

    return render(request, 'mainapp/coin.html', context)


def portfolio(request):
    orders = Order.objects.all()

    prices = {}
    total_investment = 0
    current_investment = 0
    for order in orders: 
        ticker = yf.Ticker(order.symbol)
        price = ticker.history(period='1d')['Close']
        prices[order.coin] = np.array(price)[0]

        total_investment += order.bought_price * order.quantity
        current_investment += np.array(price)[0] * order.quantity

    if request.method == 'POST':
        order = get_object_or_404(Order, id=int(request.POST.get('order-id')))
        selling_price = float(request.POST.get('selling-price'))
        profit_or_loss = float(request.POST.get('profit-or-loss'))

        transaction = Transaction.objects.create(
            coin=order.coin,
            symbol=order.symbol,
            bought_price=order.bought_price,
            quantity=order.quantity,
            bought_at=order.bought_at,
            selling_price=selling_price,
            profit_or_loss=profit_or_loss,
            transaction_date=datetime.now(),
            user=request.user,
        )
        order.delete()
        
        return redirect('transactions')
    else:
        pass

    context = {
        'orders': orders,
        'prices': prices,
        'total_investment': total_investment,
        'current_investment': current_investment,
        'p_or_l': current_investment - total_investment,
    }

    return render(request, 'mainapp/portfolio.html', context)


def transactions(request):
    trans = Transaction.objects.all()

    context = {
        'trans': trans,
    }

    return render(request, 'mainapp/transactions.html', context)

