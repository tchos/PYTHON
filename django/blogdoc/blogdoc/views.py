from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    #return HttpResponse("<h1>Bonjour</h1>")
    return render(request, "blogdoc/index.html", context={"date": datetime.today()})