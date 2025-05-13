from django.db import models
class Personnalite(models.Model):
        nom = models.CharField(max_length=100)
        prenom = models.CharField(max_length = 100)
        date_naissance = models.DateField(blank=True, null = True)
        pays = models.ForeignKey("pays", on_delete=models.CASCADE, default=None)



        def __str__(self):
                chaine = f"{self.nom}␣et␣{self.prenom}␣née␣en␣{self.date_parution}␣dans␣le␣pays␣suivant␣{self.pays}"
                return chaine

class Pays(models.Model):
        pays = models.CharField(max_length=100, blank=False)
        description = models.TextField(null = True, blank = True)

        def __str__(self):
                return self.pays

        def dico(self):
                return {"pays": self.pays, "description": self.description}



