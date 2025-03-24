from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Broker(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Asset(models.Model):
    ASSET_TYPES = [
        ('savings','Savings'),
        ('fixed_income BR','Fixed Income BR'),
        ('stock_br','Stock BR'),
        ('real_state_br', 'Real State (BR)'),
        ('stock_us','Stock US'),
        ('long_time_inv','Long Time Investiment'),
        ('fixed_income US','Fixed Income US'),
        ('real_state_us', 'Real State (US)'),
        ('emergency_fund', 'Emergency Fund'),
        ('crypto', 'Cryptocurrency'),
    ]

    RATE_TYPES = [
        ("prefixed", "Prefixed"),
        ("post_fixed","Post Fixed"),
        ("hybrid", "Hybrid"),
    ]

    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)  # Example: AAPL, BTC
    #asset_type = models.ForeignKey(AssetType, on_delete=models.PROTECT)
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rate_type = models.CharField(max_length=20, choices=RATE_TYPES, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.symbol})"
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     asset_type = cleaned_data["asset_type"]

    #     if asset_type == "fixed_income BR" or asset_type == "savings" or asset_type == "long_time_inv" or asset_type == "emergency_fund":
    #         self.Fields['rate'].required = True
    #         self.Fields['rate_type'].required = True
    #     else:
    #         self.Fields['rate'].required = False
    #         self.Fields['rate_type'].required = False

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]

    CURRENCY_TYPES = [
        ('usd', 'USD $'),
        ('brl', 'BRL R$'),
    ]

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    costs = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    currency_type = models.CharField(max_length=10, choices=CURRENCY_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expire_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.transaction_type.upper()} {self.quantity} {self.asset.symbol} @ {self.price_per_unit}"