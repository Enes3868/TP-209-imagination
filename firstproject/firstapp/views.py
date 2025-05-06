from django.shortcuts import render

from django.shortcuts import render
from .forms import PersonnaliteForm
from . import models
def ajout(request):
    if request.method == "POST":
        form = PersonnaliteForm(request)
        if form.is_valid():
            Personnalite = form.save()
            return render(request,"firstapp/affiche.html",{"Personnalite" : Personnalite})
        else:
            return render(request,"firstapp/ajout.html",{"form": form})


def traitement(request):
    lform = PersonnaliteForm(request.POST)
    if lform.is_valid():
        personnalite = lform.save()
        return render(request,"firstapp/affiche.html",{"Personnalite" : personnalite})
    else:
        return render(request,"firstapp/ajout.html",{"form": lform})


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

