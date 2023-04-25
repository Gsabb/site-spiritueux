from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
   user = models.OneToOneField(User, on_delete = models.CASCADE, null=True, blank=True)
   name = models.charField(max_length=200, null=True)
   email = models.charField(max_length=200, null=True)

   def __str__(self):
    return self.name

class Produit(models.Model):
    name = models.charField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default = False, null = True, blank = True)

   def __str__(self):
    return self.name
