from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipCode = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country  = models.CharField(max_length=200)
    telefon = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    notes = models.CharField(max_length=200)
    lastAssociation = models.DateField(default=None)

    def __str__(self):
        return self.item +' | ' +  str(self.completed)

class StorageCenters(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipCode = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.item +' | ' +  str(self.completed)

class StorageUnits(models.Model):
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    storagecenterId = models.ForeignKey(StorageCenters, on_delete=models.CASCADE)
    inService = models.BooleanField(default=True)
    rentedToId = models.ForeignKey(Customers, on_delete=models.CASCADE)
    notes = models.CharField(max_length=500)

    def __str__(self):
        return self.item +' | ' +  str(self.completed)

class StorageReservations(models.Model):
    customerId = models.ForeignKey(Customers, on_delete=models.CASCADE)
    storageUnitId = models.ForeignKey(StorageUnits, on_delete=models.CASCADE)
    notes = models.CharField(max_length=500)

    def __str__(self):
        return self.item +' | ' +  str(self.completed)
