from django . urls import path
from . import views

urlpatterns = [
    path('ajout/', views.ajout, name='ajout'),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/',views.read),
    path('/update/<int:id>/',views.traitementupdate),
    path('afficher_all/', views.afficher_all, name='afficher_all'),
    path('update/<int:id>/', views.update, name='update'),

]