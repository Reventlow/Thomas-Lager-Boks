from django import forms
from .models import Customers, StorageCenters, StorageReservations, StorageUnits

class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields=["name", "address","zipCode", "city","state", "country","telephone", "email","notes"]

class CustomerList(forms.ModelForm):
    class Meta:
        model = Customers
        fields=["id","name", "address","zipCode", "city","state", "country","telephone", "email","notes", "lastAssociation"]

class CreateStorageCenterForm(forms.ModelForm):
    class Meta:
        model = StorageCenters
        fields=["name", "address","zipCode", "city"]

class StorageCenterList(forms.ModelForm):
    class Meta:
        model = StorageCenters
        fields=["id","name", "address","zipCode", "city"]
