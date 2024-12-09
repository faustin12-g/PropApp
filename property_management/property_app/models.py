from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model, SET_NULL


class Property(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    number_of_units = models.IntegerField()

    def __str__(self):
        return self.name

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    rent = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.unit_number)
class Tenant(models.Model):
        name=models.CharField(max_length=300)
        email=models.EmailField(max_length=50)
        phone_number=models.CharField(max_length=13)
        def __str__(self):
            return self.name

class Lease(models.Model):
        tenant=models.ForeignKey(Tenant,  on_delete=models.CASCADE)
        unit=models.ForeignKey(Unit, on_delete=models.SET_NULL, blank=True, null=True)
        start_date=models.DateField()
        end_date=models.DateField()
        amount=models.CharField(max_length=100)
        def __str__(self):
            return str(self.unit)













