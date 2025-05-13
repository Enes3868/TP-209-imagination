from django . urls import path
from . import views, viewsp

urlpatterns = [
    path('ajout/', views.ajout, name='ajout'),
    path('traitement/', views.traitement, name='traitement'),
    path('confirmation/<int:id>/', views.confirmation, name='confirmation'),
    path('/update/<int:id>/',views.traitementupdate),
    path('afficher_all/', views.afficher_all, name='afficher_all'),
    path('update/<int:id>/', views.update, name='update'),
    path('supprimer/<int:id>/', views.supprimer, name='supprimer'),


    path('ajoutp/', viewsp.ajoutp, name='ajoutp'),
    path('traitementp/', viewsp.traitementp),
    path('affichep/<int:id>/', viewsp.readp),
    path('/updatep/<int:id>/', viewsp.traitementupdatep),
    path('afficher_allp/', viewsp.afficher_allp, name='afficher_allp'),
    path('updatep/<int:id>/', viewsp.updatep, name='updatep'),
    path('supprimerp/<int:id>/', viewsp.supprimerp, name='supprimerp')

]