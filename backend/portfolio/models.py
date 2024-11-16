from django.db import models
from users.models import User
from assets.models import Asset


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="portfolios")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.name} at {self.created_at}"


class PortfolioAsset(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="portfolio_assets")
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, related_name="asset_portfolios")
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.asset.symbol} in {self.portfolio.name}"
