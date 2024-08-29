from django.db import models

# Create your models here.



class Student(models.Model):
    CHOICE_GENRE = (
        ('h', 'homme'),
        ('f', 'femme'),
    )

    level_choice = (
        ('1ère', '1ère'),
        ('2nde', '2nde'),
        ('3ème', '3ème'),
        ('4ème', '4ème'),
        ('5ème', '5ème'),


    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    level = models.CharField(choices=level_choice, max_length=10)
    birth_day = models.DateField(max_length=10)
    sex = models.CharField(choices=CHOICE_GENRE, max_length=10)
    town = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)
    registration_number= models.CharField(max_length=20)