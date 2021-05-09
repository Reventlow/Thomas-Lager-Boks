from django.shortcuts import render, redirect
from .models import StorageUnits, StorageCenters, StorageReservations, Customers
from .forms import CreateCustomerForm, CustomerList, StorageCenterList, CreateStorageCenterForm, StorageUnitList, \
    CreateStorageUnitForm, StorageUnitAssign, StorageUnitAssign_Save, EditStorageUnitForm, EditStorageUnitForm_update
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
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


@login_required(login_url='login')
def create_customer(request):
    return render(request, 'create_customer.html')


@login_required(login_url='login')
def edit_customer(request, customer_id):
    if request.method == 'POST':
        customer = Customers.objects.get(pk=customer_id)
        form = CreateCustomerForm(request.POST or None, instance=customer)
        if form.is_valid() and request.POST['name'] != '':
            form.save()
            all_items = Customers.objects.all
            messages.success(request, request.POST['name'] + ' er blevet redigeret i din kundelist')
            return redirect('customer_list')
        else:
            messages.success(request, 'Kunde er ikke blevet redigeret i din kundelist')
            return redirect('customer_list')
    else:
        form = Customers.objects.get(pk=customer_id)
        context = {'form': form}
        return render(request, 'edit_customer.html', context)


@login_required(login_url='login')
def delete_customer(request, customer_id):
    customer = Customers.objects.get(pk=customer_id)
    customer.delete()
    messages.success(request, 'Kunden er blevet slettet fra din kundelist')
    return redirect('customer_list')


@login_required(login_url='login')
def storageCenter_list(request):
    if request.method == 'POST':
        form = StorageCenterList(request.POST or None)
        if form.is_valid() and request.POST['name'] != '':
            form.save()
            all_items = StorageCenters.objects.all
            messages.success(request, request.POST['name'] + ' er blevet tilføjet ')
            context = {'all_items': all_items}
            return render(request, 'storageCenter_list.html', context)
        else:
            print(form.errors)
            messages.error(request, form.errors)
            return render(request, 'storageCenter_list.html')
    else:
        all_items = StorageCenters.objects.all
        context = {'all_items': all_items}
        return render(request, 'storageCenter_list.html', context)

@login_required(login_url='login')
def create_storageCenter(request):
    return render(request, 'create_storageCenter.html')

@login_required(login_url='login')
def edit_storageCenter(request, storageCenter_id):
    if request.method == 'POST':
        storageCenter = StorageCenters.objects.get(pk=storageCenter_id)
        form = CreateStorageCenterForm(request.POST or None, instance=storageCenter)
        if form.is_valid() and request.POST['name'] != '':
            form.save()
            all_items = StorageCenters.objects.all
            messages.success(request, request.POST['name'] + ' er blevet redigeret')
            return redirect('storageCenter_list')
        else:
            messages.success(request, 'Der skete en fejl i redigering')
            return redirect('storageCenter_list')
    else:
        form = StorageCenters.objects.get(pk=storageCenter_id)
        context = {'form': form}
        return render(request, 'edit_storageCenter.html', context)

@login_required(login_url='login')
def delete_storageCenter(request, storageCenter_id):
    location = StorageCenters.objects.get(pk=storageCenter_id)
    location.delete()
    messages.success(request, 'Lokation er blevet slettet')
    return redirect('storageCenter_list')

@login_required(login_url='login')
def storageUnit_list(request):
    if request.method == 'POST':
        form = StorageUnitList(request.POST or None)
        if form.is_valid() and request.POST['name'] != '':
            form.save()
            all_items = StorageUnits.objects.all
            messages.success(request, request.POST['name'] + ' er blevet tilføjet ')
            context = {'all_items': all_items}
            return render(request, 'storageUnit_list.html', context)
        else:
            print(form.errors)
            messages.error(request, form.errors)
            return render(request, 'storageUnit_list.html')
    else:
        all_items = StorageUnits.objects.all
        context = {'all_items': all_items}
        return render(request, 'storageUnit_list.html', context)

@login_required(login_url='login')
def create_storageUnit(request):
    context = {}
    form = CreateStorageUnitForm(request.POST or None)
    context['form'] = form
    return render(request, 'create_storageUnit.html', context)

@login_required(login_url='login')
def edit_storageUnit(request, storageUnit_id):
    if request.method == 'POST':
        storageUnit = StorageUnits.objects.get(pk=storageUnit_id)
        form = EditStorageUnitForm(request.POST or None, instance=storageUnit)
        if form.is_valid() and request.POST['name'] != '':
            form.storageCenter = storageUnit.storageCenter
            form.save()
            messages.success(request, 'Rummet er blevet redigeret')
            return redirect('storageUnit_list')
        else:
            messages.success(request, 'Der skete en fejl i redigering')
            return redirect('storageUnit_list')
    else:
        storageUnit = StorageUnits.objects.get(pk=storageUnit_id)
        form = EditStorageUnitForm(request.POST or None, instance=storageUnit)
        context = {'form': form, 'form_id': storageUnit_id}
        thisId = storageUnit_id
        return render(request, 'edit_storageUnit.html', context)

@login_required(login_url='login')
def edit_storageUnit_update(request, storageUnit_id):
    if request.method == 'POST':
        storageUnit = StorageUnits.objects.get(pk=storageUnit_id)
        form = EditStorageUnitForm_update(request.POST or None, instance=storageUnit)
        if form.is_valid() and request.POST['name'] != '':
            form.save()
            messages.success(request, 'Rummet er blevet redigeret')
            return redirect('storageUnit_list')
        else:
            messages.success(request, 'Der skete en fejl i redigering')
            return redirect('storageUnit_list')
    else:
        return render(request, 'edit_storageUnit.html')

@login_required(login_url='login')
def delete_storageUnit(request, storageUnit_id):
    location = StorageUnits.objects.get(pk=storageUnit_id)
    location.delete()
    messages.success(request, 'Lokation er blevet slettet')
    return redirect('storageUnit_list')

@login_required(login_url='login')
def assign_storageUnit(request, storageUnit_id):
    if request.method == 'POST':
        storageUnit = StorageUnits.objects.get(pk=storageUnit_id)
        form = StorageUnitAssign_Save(request.POST or None, instance=storageUnit)
        if form.is_valid() and request.POST['name'] != '':
            form.save()

            messages.success(request, 'Udlejning er gemt')
            return redirect('storageUnit_list')
        else:
            messages.success(request, 'Der skete en fejl i redigering')
            return redirect('storageUnit_list')
    else:
        context = {}
        storageUnit = StorageUnits.objects.get(pk=storageUnit_id)
        form = StorageUnitAssign(request.POST or None, instance=storageUnit)
        context = {'form': form, 'form_id': storageUnit_id}
        return render(request, 'assign_storageUnit.html', context)

@login_required(login_url='login')
def assign_storageUnit_delete(request, storageUnit_id):
    storageUnit = StorageUnits.objects.get(pk=storageUnit_id)
    storageUnit.rentedTo = None
    storageUnit.save()
    messages.success(request, 'Kunde fjernnet fra rum')
    return redirect('storageUnit_list')

@login_required(login_url='login')
def service_storageUnit_setTrue(request, storageUnit_id):
    storageUnit = StorageUnits.objects.get(pk=storageUnit_id)
    storageUnit.inService = True
    storageUnit.save()
    return redirect('storageUnit_list')

@login_required(login_url='login')
def service_storageUnit_setFalse(request, storageUnit_id):
    storageUnit = StorageUnits.objects.get(pk=storageUnit_id)
    storageUnit.inService = False
    storageUnit.save()
    return redirect('storageUnit_list')
