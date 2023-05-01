from django.urls import path
from . import views

urlpatterns = [
    path('', views.info, name='info'),
    path('boutique/', views.boutique, name='boutique'),
    path('panier/', views.panier, name='panier'),
    path('paiement/', views.paiement, name='paiement'),
    path('update_item/', views.updateItem, name="update_item")
    
]