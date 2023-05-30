from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):

    coin = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50)
    bought_price = models.FloatField()
    quantity = models.IntegerField(default=1)
    bought_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.bought_at} : {self.symbol} at {self.bought_price}'
    

class Transaction(models.Model):

    coin = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50)
    bought_price = models.FloatField()
    quantity = models.IntegerField(default=1)
    bought_at = models.DateTimeField(default=datetime.now)
    selling_price = models.FloatField() 
    profit_or_loss = models.FloatField()
    transaction_date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.coin} - Sell - {self.profit_or_loss}'
