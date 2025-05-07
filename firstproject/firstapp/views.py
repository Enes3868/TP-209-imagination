from django.shortcuts import render

from django.shortcuts import render
from .forms import PersonnaliteForm
from . import models
from .models import Personnalite

def ajout(request):
     if request.method == "POST":
        form = PersonnaliteForm(request.POST)  
        if form.is_valid():
            personnalite = form.save()
            return render(request, "firstapp/affiche.html", {"personnalite": personnalite})  
        else:
            return render(request, "firstapp/ajout.html", {"form": form})  
     else:
        form = PersonnaliteForm()
        return render(request, "firstapp/ajout.html", {"form": form}) 


def traitement(request):
    lform = PersonnaliteForm(request.POST)
    if lform.is_valid():
        personnalite = lform.save()
        return render(request, 'firstapp/affiche.html', {
                "nom": personnalite.nom,
                "prenom": personnalite.prenom,
                "date_naissance": personnalite.date_naissance,
            })
    return redirect('ajout')


def read(request, id):
    Personnalite = models.Personnalite.objects.get(pk=id)
    return render(request,"firstapp/affiche.html",{"Personnalite": Personnalite})

def traitementupdate(request, id):
    lform = PersonnaliteForm(request.POST)
    if lform.is_valid():
        Personnalite = lform.save(commit=False)
        Personnalite.id = id;
        Personnalite.save()
        return HttpResponseRedirect("/firstapp/")
    else:
        return render(request, "firstapp/update.html", {"form": lform, "id": id})


def afficher_all(request):
    liste_personnalites = Personnalite.objects.all()
    return render(request, "firstapp/afficher_all.html", {"liste": liste_personnalites})

