from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    dateDuJour = datetime.today()
    """Envoyer une variable à la vue index: on use le dico context"""
    return render(request, "docBlog/index.html", context={
        "dateDuJour":dateDuJour,
        "nom": "Kwette"
    })
    #return HttpResponse("<h1>Bonjour et bienvenue sur mon site</h1>")