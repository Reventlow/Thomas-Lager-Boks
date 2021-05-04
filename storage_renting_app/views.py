from django.shortcuts import render, redirect
from .models import StorageUnits, StorageCenters, StorageReservations, Customers
#from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def customer_list(request):
    return render(request, 'customer_list.html')

def create_customer(request):
    return render(request, 'create_customer.html')