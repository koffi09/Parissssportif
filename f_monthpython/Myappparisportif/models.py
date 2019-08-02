from django.db import models
from datetime import datetime, date, time


class Pays(models.Model):
    nom_pays = models.CharField(max_length=255)
    cote_pays = models.PositiveIntegerField()


class Rencontre(models.Model):
    nom_championat = models.CharField(max_length=255)
    rencontre_pays = models.CharField(max_length=255)
    date_rencontre = models.DateTimeField('Date_rencontre')
                       
    
class parieurs(models.Model):
    nom = models.CharField(max_length=50)
    montant_parier = models.PositiveIntegerField()
    choix_pays = models.CharField(max_length=150)












# Create your models here.
