from django.shortcuts import render

from django.shortcuts import render
from .forms import PersonnaliteForm
from . import models
def ajout(request):
    if request.method == "POST":
        form = PersonnaliteForm(request)
        if form.is_valid():
            Livre = form.save() #
            return render(request,"firstapp/affiche.html",{"Personnalite" : Personnalite})
        else:
            return render(request,"firstapp/ajout.html",{"form": form})
    else:
            form = PersonnaliteForm()
            return render(request,"firstapp/ajout.html",{"form" : form})
