from django.db import models

from django.db import models

from django.db import models

class Pays(models.Model):
    pays = models.CharField(max_length=100, unique=True, verbose_name="Pays")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.pays

    class Meta:
        verbose_name_plural = "Pays"

class Personnalite(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    date_naissance = models.DateField(blank=True, null=True, verbose_name="Date de naissance")
    pays = models.ForeignKey("firstapp.Pays", on_delete=models.CASCADE, default=None) 

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.pays}"
    
    