from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)   
    model = models.CharField(max_length=50)    
    year = models.IntegerField()               
    color = models.CharField(max_length=30)     
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    stock = models.IntegerField(default=0)    

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

    def to_dict(self):
        return {
            "id": self.id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "color": self.color,
            "price": float(self.price),
            "stock": self.stock,
        }
