from django.shortcuts import render
from django.template import loader
from .models import *

def paiement(request):
    if request.user.is_authenticated:
        customer = request.user.client
        order, created = Commande.objects.get_or_create(client=customer, complete=False)
        items = order.produitcommande_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'paiement.html', context)

def panier(request):

    if request.user.is_authenticated:
        customer = request.user.client
        order, created = Commande.objects.get_or_create(client=customer, complete=False)
        items = order.produitcommande_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'panier.html', context)

def info(request):
    context = {}
    return render(request, 'info.html', context)

def boutique(request):
    products = Produit.objects.all()
    context = {'products':products}
    return render(request, 'boutique.html', context)