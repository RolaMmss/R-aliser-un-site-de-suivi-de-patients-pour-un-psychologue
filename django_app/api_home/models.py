from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class home_page(models.Model):
    slug = models.CharField(
        max_length = 100,
        blank =  False,
    )



# class TestModel(models.Model):
#     resultat = models.CharField(max_length=500)



class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    password = models.CharField(max_length=100, default='mot_de_passe_par_defaut')

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    

