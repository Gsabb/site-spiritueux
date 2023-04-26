from django.shortcuts import render
from django.template import loader
from .models import *

def paiement(request):
    context = {}
    return render(request, 'paiement.html', context)

def panier(request):
    context = {}
    return render(request, 'panier.html', context)

def info(request):
    context = {}
    return render(request, 'info.html', context)

def boutique(request):
    products = Produit.objects.all()
    context = {'products':products}
    return render(request, 'boutique.html', context)