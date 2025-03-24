import csv
from django.http import HttpRequest
from django.db import models
from django.db import IntegrityError
from .models import Asset, Broker, Transaction, Portfolio
from django.contrib.auth.models import User
from datetime import datetime


def handle_uploaded_file(f):
    with open("portfolio/teste3.csv", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    with open('portfolio/teste3.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        reader_obj = csv.DictReader(csvfile) 
        for row in reader_obj:
            asset = row.get('asset')
            asset_type = row.get('asset_type')
            transaction_type = row.get('transaction_type')
            quantity = float(row.get('quantity').replace(',', '.'))
            price_per_unit = float(row.get('price_per_unit').replace(',', '.'))
            costs = float(row.get('costs').replace(',', '.'))
            date = row.get('date')
            broker = row.get('broker')
            description = row.get('description')
            currency_type = row.get('currency_type')
            user = row.get('user')
            portfolio = row.get('portfolio')

            object_user = User.objects.get(username=user)
            object_portfolio, create = Portfolio.objects.get_or_create(user=object_user, name=portfolio)
            object_asset, create = Asset.objects.get_or_create(portfolio=object_portfolio, name=asset, symbol=asset,asset_type=asset_type)

            transaction_type = "buy"
            if quantity < 0:
                transaction_type = "sell"
                quantity = quantity*(-1)

            object_date = datetime.strptime(date, '%d/%m/%Y').date()
            
            object_broker, create = Broker.objects.get_or_create(name=broker)
            
            try:
                object_transaction, created = Transaction.objects.get_or_create(asset=object_asset,
            transaction_type=transaction_type,quantity=quantity,price_per_unit=price_per_unit,costs=costs,date=object_date,broker=object_broker,description=description,currency_type=currency_type,user=object_user)
            except IntegrityError as e:
                # Catch IntegrityError if a duplicate is found
                print(f"Skipping because already exists.")




