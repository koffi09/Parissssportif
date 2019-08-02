from django.shortcuts import render

# Create your views here.
from .models import Rencontre

from .forms import Pariform

from .models import Pays

def home(request):
    rencontre1= Rencontre.objects.get(id=1)
    rencontre2 = Rencontre.objects.get(id=2)

    pays1 = Pays.objects.get(id=1)
    pays2 =Pays.objects.get(id=2)
    pays3 =Pays.objects.get(id=3)
    pays4 =Pays.objects.get(id=4)


    return render(request,'pages/home.html',{'pays1':pays1 ,'pays2':pays2,'pays3':pays3,'pays4':pays4,'rencontre1':rencontre1,'rencontre2':rencontre2})


def parier(request): 
    
    pays1 = Pays.objects.get(id=1)
    pays2 =Pays.objects.get(id=2)
    pays3 =Pays.objects.get(id=3)
    pays4 =Pays.objects.get(id=4)

    rencontre = Rencontre.objects.get(id=1)
    return render(request,'pages/parier.html',{ 'pays1':pays1,'pays2':pays2,'pays3':pays3,'pays4':pays4,'rencontre':rencontre})


def resultat(request):
     
    if request.method =='POST':
          
         
         form = Pariform(request.POST)
         
         if form.is_valid():
           nom  = form.cleaned_data['nom']
           prenom = form.cleaned_data['prenom']
           winner = form.cleaned_data['winner']
           email = form.cleaned_data['email']
           montant= form.cleaned_data['montant']
         if winner =="Cote d'Ivoire" :
             gagnant = montant*8
         if winner =="Mali":
             gagnant =montant*4
           
    else:
        form = Pariform()
    return render(request,'pages/resultat.html',{"nom":form.cleaned_data['nom'],"prenom":form.cleaned_data['prenom'],"winner":form.cleaned_data['winner'],"email":form.cleaned_data['email'],"montant":form.cleaned_data['montant'],"gagnant":gagnant})
        






             


  