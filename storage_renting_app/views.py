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
        item = Jobs.objects.get(pk=job_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid() and request.POST['item'] != '':
            form.save()
            all_items = Jobs.objects.all
            messages.success(request, request.POST['item']+ ' er blevet redigeret i din opgave list')
            return redirect('todo')
    else:
        item =Jobs.objects.get(pk=job_id)
        context = {'item': item}
        return render(request, 'edit.html', context)

def delete_customer(request, customer_id):
    item = Customers.objects.get(pk=customer_id)
    item.delete()
    messages.success(request, 'Kunden er blevet slettet fra din kundelist')
    return redirect('customer_list')
