from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms
class PersonnaliteForm(ModelForm):
    class Meta:
        model = models.Personnalite
        fields = ('nom', 'prenom', 'date_naissance', 'pays')
        labels = {
            'nom' : _('Nom'),
            'prenom' : _('Prenom') ,
            'date_naissance' : _('date␣de␣naissance'),
            'pays' : _('Pays'),

        }

        widgets = {
        'nom': forms.TextInput(attrs={'class': 'class_css_input', 'placeholder': 'Le nom…'}),
        'prenom': forms.TextInput(attrs={'class': 'class_css_input', 'placeholder': 'Le prénom…'}),
        'date_naissance': forms.TextInput(attrs={'class': 'class_css_input', 'placeholder': 'La date de naissance …'}),
        'pays': forms.TextInput(attrs={'class': 'class_css_area', 'placeholder': 'Le pays…'}),
        }