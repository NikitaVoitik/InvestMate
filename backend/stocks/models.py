from django.db import models


class Asset(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)


class Exchange(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)


class StocksData(models.Model):
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()
    market_cap = models.BigIntegerField()
    asset_id = models.ForeignKey(Asset, on_delete=models.PROTECT)
    exchange_id = models.ForeignKey(Exchange, on_delete=models.PROTECT)
    last_updated = models.DateTimeField(auto_now=True)


class Price(models.Model):
    assets_data_id = models.ForeignKey(StocksData, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
