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

class CreateStorageUnitForm(forms.ModelForm):
    name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Rum navn'}))
    size = forms.CharField(label="",  widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Rummets størrelse (kun tal)'}))
    price = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Rummets pris (kun tal)'}))
    storageCenter = forms.ModelChoiceField(queryset=StorageCenters.objects.all(), label="Sted", widget=forms.Select(
        attrs={'class': 'form-control'}))
    inService = forms.BooleanField(label="Er rummet brugbar", initial=True)
    notes = forms.CharField(label="Noter", max_length=100, required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', }))

    class Meta:
        model = StorageUnits
        fields=["name", "size","price", "storageCenter", "inService", "notes"]

class StorageUnitList(forms.ModelForm):
    class Meta:
        model = StorageUnits
        fields=["id","name", "size","price", "storageCenter", "inService","rentedTo", "notes"]

class StorageUnitAssign(forms.ModelForm):

    name = forms.CharField(label="Rum", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'readonly':'readonly'}))
    rentedTo = forms.ModelChoiceField(queryset=Customers.objects.all(), required=False,label="Kunde", widget=forms.Select(
        attrs={'class': 'form-control'}))

    class Meta:
        model = StorageUnits
        fields=["id","name","rentedTo"]


class StorageUnitAssign_Save(forms.ModelForm):

    class Meta:
        model = StorageUnits
        fields=["rentedTo"]

class EditStorageUnitForm(forms.ModelForm):

    name = forms.CharField(label="Rum navn", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Rum navn'}))
    size = forms.CharField(label="Rummets størrelse (kun tal)",  widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Rummets størrelse (kun tal)'}))
    price = forms.CharField(label="Rummets pris (kun tal)", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Rummets pris (kun tal)'}))
    storageCenter = forms.ModelChoiceField(queryset=StorageCenters.objects.all(), label="Sted", widget=forms.Select(
        attrs={'class': 'form-control'}))
    inService = forms.BooleanField(label="Er rummet brugbar", initial=True)
    notes = forms.CharField(label="Noter", max_length=100, required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', }))

    class Meta:
        model = StorageUnits
        fields=["id","name", "size","price", "storageCenter", "inService", "notes"]

class EditStorageUnitForm_update(forms.ModelForm):
    class Meta:
        model = StorageUnits
        fields=["name", "size","price", "storageCenter", "inService", "notes"]
