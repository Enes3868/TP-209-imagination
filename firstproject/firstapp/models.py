from django.db import models
class Personnalite(models.Model):
        nom = models.CharField(max_length=100)
        prenom = models.CharField(max_length = 100)
        date_naissance = models.DateField(blank=True, null = True)

        pays = models.CharField(blank=False)

        def __str__(self):
                chaine = f"{self.nom}␣et␣{self.prenom}␣née␣en␣{self.date_parution}␣dans␣le␣pays␣suivant␣{self.pays}"
                return chaine