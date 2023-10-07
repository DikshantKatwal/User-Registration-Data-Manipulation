
from django.db import models

# Create your models here.
class Products(models.Model):
    
    name = models.CharField(max_length=50)
    price =  models.IntegerField(default= 0)
    img = models.ImageField(upload_to='static\img', default='toggle-icon.png')

    
# Create your models here.
