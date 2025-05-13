from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class PaysForm(ModelForm):
    class Meta:
        model = models.Pays
        fields = '__all__'
        labels = {
            'pays': _('Nom du pays'),
            'description': _('Description')
        }
        widgets = {
            'pays': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le nom du pays...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Description du pays...'
            }),
        }

class PersonnaliteForm(ModelForm):
    class Meta:
        model = models.Personnalite
        fields = ['nom', 'prenom', 'date_naissance', 'pays_saisie']
        labels = {
            'nom': _('Nom'),
            'prenom': _('Prénom'),
            'date_naissance': _('Date de naissance'),
            'pays_saisie': _('Pays')
        }
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le nom...'
            }),
            'prenom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le prénom...'
            }),
            'date_naissance': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'pays_saisie': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le pays...'
            }),
        }