from django.db import models


class Asset(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    market_cap = models.BigIntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    asset_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.symbol}: {self.market_cap}$, {self.asset_type}"


class PriceHistory(models.Model):
    asset = models.ForeignKey(Asset, related_name="price_history", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField()

    def __str__(self):
        return f"{self.asset.symbol}: {self.open_price}$-{self.close_price}$ at {self.timestamp}"
