from django.shortcuts import render, redirect
from .models import StorageUnits, StorageCenters, StorageReservations, Customers
from .forms import CreateCustomerForm, CustomerList
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def customer_list(request):
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST or None)
        if form.is_valid() and request.POST['name'] != '':
            form.save()
            all_items = Customers.objects.all
            messages.success(request, request.POST['name'] + ' er blevet tilføjet til din kundelist')
            context = {'all_items': all_items}
            return render(request, 'customer_list.html', context)
        else:
            print(form.errors)
            messages.error(request, form.errors)
            return render(request, 'customer_list.html')
    else:
        all_items = Customers.objects.all
        context = {'all_items': all_items}
        return render(request, 'customer_list.html', context)


def create_customer(request):
    return render(request, 'create_customer.html')

def edit_customer(request, customer_id):
    if request.method ==  'POST':
        customer = Customers.objects.get(pk=customer_id)
        form = CreateCustomerForm(request.POST or None, instance=customer)
        if form.is_valid() and request.POST['name'] != '':
            form.save()
            all_items = Customers.objects.all
            messages.success(request, request.POST['name']+ ' er blevet redigeret i din kundelist')
            return redirect('customer_list')
        else:
            messages.success(request, 'Kunde er ikke blevet redigeret i din kundelist')
            return redirect('customer_list')
    else:
        form =Customers.objects.get(pk=customer_id)
        context = {'form': form}
        return render(request, 'edit_customer.html', context)

def delete_customer(request, customer_id):
    customer = Customers.objects.get(pk=customer_id)
    customer.delete()
    messages.success(request, 'Kunden er blevet slettet fra din kundelist')
    return redirect('customer_list')
