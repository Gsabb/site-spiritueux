from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from django.template import loader
from .models import *
from .utils import cartData, cookieCart, guestOrder


def paiement(request):
    data = cartData(request)
    items = data['items']
    cartItems = data['cartItems']
    order = data['order']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'paiement.html', context)


def panier(request):
    data = cartData(request)
    items = data['items']
    cartItems = data['cartItems']
    order = data['order']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'panier.html', context)


def info(request):
    context = {}
    return render(request, 'info.html', context)


def boutique(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Produit.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'boutique.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ', action)
    print('Product ID: ', productId)

    customer = request.user.client
    product = Produit.objects.get(id=productId)
    order, created = Commande.objects.get_or_create(
        client=customer, complete=False)
    orderItem, created = ProduitCommande.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.client
        order, created = Commande.objects.get_or_create(
            client=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        AdresseLivraison.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment complete', safe=False)
