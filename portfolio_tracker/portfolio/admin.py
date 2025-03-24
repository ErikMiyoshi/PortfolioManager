from django.contrib import admin
from .models import Portfolio, Asset, Transaction, Broker

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Broker)
admin.site.register(Asset)
admin.site.register(Transaction)