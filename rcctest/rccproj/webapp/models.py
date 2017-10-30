from django.db import models

BIKE_TYPE_CHOICES = (
    ('0', 'Road Bike'),
    ('1', 'Mountain Bike'),
    ('2', 'Hybrid Bike'),
    ('3', 'City Bike'),
    ('4', 'Others'),
)

# Create your models here.
class Bikes(models.Model):
    SKU = models.CharField(max_length=17,null=False,primary_key=True,unique=True)
    name = models.CharField(max_length=50,null=False)
    description = models.CharField(max_length=180,default="No description available.")
    rating = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8,decimal_places=2,null=False)
    quantity = models.IntegerField(default=0)
    type = models.CharField(max_length=15, choices=BIKE_TYPE_CHOICES)
    image = models.ImageField()

    def __str__(self):
        return self.name
