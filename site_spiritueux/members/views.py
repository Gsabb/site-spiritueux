from django.http import HttpResponse
from django.template import loader
from .models import Member

def paiement(request):
    template = loader.get_template('paiement.html')
    return HttpResponse(template.render())

def panier(request):
    template = loader.get_template('panier.html')
    return HttpResponse(template.render())

def info(request):
    template = loader.get_template('info.html')
    return HttpResponse(template.render())

def boutique(request):
    template = loader.get_template('boutique.html')
    return HttpResponse(template.render())