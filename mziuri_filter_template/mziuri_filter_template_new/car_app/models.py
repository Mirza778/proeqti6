from django.db import models

# Create your models here.


class Car(models.Model):
    
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    model_year = models.PositiveIntegerField()
    vin = models.CharField(max_length=17, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"