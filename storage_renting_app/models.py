from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    zipCode = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    country  = models.CharField(max_length=200, null=True, blank=True)
    telephone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)
    lastAssociation = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name

class StorageCenters(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipCode = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class StorageUnits(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField()
    price = models.IntegerField()
    storageCenter = models.ForeignKey(StorageCenters, related_name="%(class)s_requests_created", on_delete=models.CASCADE, default=1)
    inService = models.BooleanField(default=True)
    rentedTo = models.ForeignKey(Customers, on_delete=models.CASCADE, default=None, null=True, blank=True)
    notes = models.CharField(max_length=500, default=None, null=True, blank=True)

    def __str__(self):
        return self.name +' | ' +  str(self.id)

class StorageReservations(models.Model):
    customerId = models.ForeignKey(Customers, on_delete=models.CASCADE)
    storageUnitId = models.ForeignKey(StorageUnits, on_delete=models.CASCADE)
    notes = models.CharField(max_length=500)

    def __str__(self):
        return self.item +' | ' +  str(self.completed)
