from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import PaysForm
from . import models
from .models import Pays
from django.shortcuts import HttpResponseRedirect


def ajoutp(request):
    if request.method == "POST":
        form = PaysForm(request.POST)
        if form.is_valid():
            pays = form.save()
            return render(request, "pays/affichep.html", {"pays ": pays })
        else:
            return render(request, "pays/ajoutp.html", {"form": form})
    else:
        form = PaysForm()
        return render(request, "pays/ajoutp.html", {"form": form})


def traitementp(request):
    lform = PaysForm(request.POST)
    if lform.is_valid():
        pays = lform.save()
        return render(request, 'pays/affichep.html', {
            "pays": pays  
        })
    return redirect('ajoutp')


def readp(request, id):
    Pays = models.Pays.objects.get(pk=id)
    return render(request, "pays/affichep.html", {"Pays": Pays})


def traitementupdatep(request, id):
    lform = PaysForm(request.POST)
    if lform.is_valid():
        Pays = lform.save(commit=False)
        Pays.id = id;
        Pays.save()
        return HttpResponseRedirect("/firstapp/")
    else:
        return render(request, "pays/updatep.html", {"form": lform, "id": id})


def afficher_allp(request):
    liste_pays = Pays.objects.all()
    return render(request, "pays/afficher_allp.html", {"liste": liste_pays})


def updatep(request, id):
    pays = get_object_or_404(models.Pays, id=id)
    if request.method == "POST":
        form = PaysForm(request.POST, instance=pays)
        if form.is_valid():
            form.save()
            return redirect('afficher_allp')
    else:
        form = PaysForm(instance=pays)

    return render(request, "pays/updatep.html", {"form": form})


def supprimerp(request, id):
    pays = get_object_or_404(models.Pays, pk=id)
    pays.delete()
    return redirect("afficher_allp")