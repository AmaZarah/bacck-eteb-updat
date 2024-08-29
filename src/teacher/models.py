from django.db import models

# Create your models here.
class Teacher(models.Model):
    CHOICE_GENRE = (
        ('h', 'homme'),
        ('f', 'femme'),
    )

    subject_choice = (
        ('MATHS', 'maths'),
        ('SVT', 'svt'),
        ('PHYSIQUE', 'physique'),
        ('English', 'English'),
        ('Frensh', 'Frensh'),


    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(choices=subject_choice, max_length=10)
    birth_day = models.DateField()
    sex = models.CharField(choices=CHOICE_GENRE, max_length=10)
    town = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)
    
    