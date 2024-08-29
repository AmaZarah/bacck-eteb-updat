from django.db import models

# Create your models here.
class User(models.Model):
    pseudo = models.CharField(max_length=10, unique=True)
    pass_word = models.CharField(max_length=128)
    creat_dat = models.DateField(auto_now_add=True)
      