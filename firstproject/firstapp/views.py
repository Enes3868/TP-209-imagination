from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import PersonnaliteForm
from . import models
from .models import Personnalite
from django.shortcuts import HttpResponseRedirect


def ajout(request):
    if request.method == "POST":
        form = PersonnaliteForm(request.POST)
        if form.is_valid():
            personnalite = form.save()
            return redirect('confirmation', id=personnalite.id)  # Redirection vers la confirmation
        else:
            return render(request, "firstapp/ajout.html", {"form": form})
    else:
        form = PersonnaliteForm()
        return render(request, "firstapp/ajout.html", {"form": form})

def traitement(request):
    if request.method == "POST":
        form = PersonnaliteForm(request.POST)
        if form.is_valid():
            personnalite = form.save()
            return render(request, "firstapp/affiche.html", {
                "personnalite": personnalite,
                "message": "La personnalité a bien été enregistrée !"
            })
        else:
            return render(request, "firstapp/ajout.html", {"form": form})
    return redirect('ajout')  # Redirige si accès direct sans POST

def confirmation(request, id):
    personnalite = models.Personnalite.objects.get(pk=id)
    return render(request, "firstapp/affiche.html", {"personnalite": personnalite})

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

def update(request, id):
    personnalite = get_object_or_404(models.Personnalite, id=id)
    if request.method == "POST":
        form = PersonnaliteForm(request.POST, instance=personnalite)
        if form.is_valid():
            form.save()
            return redirect('afficher_all')
    else:
        form = PersonnaliteForm(instance=personnalite)
    
    return render(request, "firstapp/update.html", {"form": form})

def supprimer(request, id):
    personnalite = models.Personnalite.objects.get(pk=id)
    personnalite.delete()
    return HttpResponseRedirect("firstapp/afficher_all.html/")