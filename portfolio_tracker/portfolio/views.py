from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import CreateView

from django.urls import reverse_lazy

from .models import Transaction, Asset

import requests
from django.conf import settings


from django.http import HttpResponseRedirect
from .forms import UploadFileForm

from .file_import import handle_uploaded_file

# Create your views here.
#@login_required
def home(request):
    #stock_data = get_stock_data('AAPL')  # Example for Apple stock
    assets = Asset.objects.all().order_by('asset_type')

    value_dict = {}
    for asset in assets:
        value_asset = asset.average_price()
        value_dict.update({asset: value_asset})

    context = {
       'assets': assets,
       #'value_asset': value_asset,
       'value_dict':value_dict,
    }
    return render(request, "portfolio/home.html", context)

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

def logout_view(request):
  logout(request)
  return redirect('home')


def get_stock_data(symbol):
    api_key = settings.ALPHA_VANTAGE_KEY
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    #url = f'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

    # Extract the time series data from the response
    time_series = data.get('Time Series (Daily)', {})
    
    # Format the data into a more readable format
    formatted_data = []
    for date, stats in time_series.items():
        formatted_data.append({
            'date': date,
            'open': stats.get('1. open'),
            'high': stats.get('2. high'),
            'low': stats.get('3. low'),
            'close': stats.get('4. close'),
            'volume': stats.get('5. volume')
        })

    return formatted_data

def asset(request, pk):
  asset = Asset.objects.get(pk=pk)
  transactions = asset.transaction_set.all().order_by('date')
  context = {
     "transactions": transactions,
  }
  #transactions = 0
  return render(request, "portfolio/asset.html", context)


def import_file(request):
  if request.method == "POST":
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      handle_uploaded_file(request.FILES["file"])
      return HttpResponseRedirect("/import")
  else:
    form = UploadFileForm()
  return render(request, "portfolio/import.html", {"form": form})