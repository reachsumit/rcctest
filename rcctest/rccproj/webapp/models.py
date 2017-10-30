from django.db import models

# Create your models here.
class Bikes(models.Model):
    SKU = models.CharField(max_length=17,null=False,primary_key=True,unique=True)
    name = models.CharField(max_length=50,null=False)
    description = models.CharField(max_length=180,default="No description available.")
    rating = models.DecimalField(max_digits=1,decimal_places=1,default=0.0)
    price = models.DecimalField(max_digits=8,decimal_places=2,null=False)
    quantity = models.IntegerField(default=0)
    type = models.CharField(max_length=25,default='others')
    image = models.ImageField()

    def __str__(self):
        return self.name
