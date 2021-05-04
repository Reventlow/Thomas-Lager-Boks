from django import forms
from .models import Customers

class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields=["name", "address","zipCode", "city","state", "country","telephone", "email","notes"]

class CustomerList(forms.ModelForm):
    class Meta:
        model = Customers
        fields=["id","name", "address","zipCode", "city","state", "country","telephone", "email","notes", "lastAssociation"]

