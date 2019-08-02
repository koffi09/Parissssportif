
from django import forms


class Pariform(forms.Form):

    nom = forms.CharField(max_length=50)
    prenom = forms.CharField(max_length=50)
    winner= forms.CharField()
    email = forms.EmailField(label="Votre adresse mail")
    montant = forms.IntegerField()

