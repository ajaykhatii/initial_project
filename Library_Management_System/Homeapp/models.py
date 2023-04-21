from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    isbn = models.IntegerField()
    description = models.CharField(max_length=100)
    image = models.ImageField(max_length=700)
    
