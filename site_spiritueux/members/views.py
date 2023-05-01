from django.shortcuts import render
from django.http import JsonResponse
import json
from django.template import loader
from .models import *

def paiement(request):
    if request.user.is_authenticated:
        customer = request.user.client
        order, created = Commande.objects.get_or_create(client=customer, complete=False)
        items = order.produitcommande_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'paiement.html', context)

def panier(request):

    if request.user.is_authenticated:
        customer = request.user.client
        order, created = Commande.objects.get_or_create(client=customer, complete=False)
        items = order.produitcommande_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']


    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'panier.html', context)

def info(request):
    context = {}
    return render(request, 'info.html', context)

def boutique(request):
    if request.user.is_authenticated:
        customer = request.user.client
        order, created = Commande.objects.get_or_create(client=customer, complete=False)
        items = order.produitcommande_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    products = Produit.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, 'boutique.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ',action)
    print('Product ID: ', productId)

    customer = request.user.client
    product = Produit.objects.get(id = productId)
    order, created = Commande.objects.get_or_create(client=customer, complete=False)
    orderItem, created = ProduitCommande.objects.get_or_create(order = order, product = product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('Item added', safe=False)