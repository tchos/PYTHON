from django.shortcuts import render

# Create your views here.
def index  (request):
    return render(request, "blog/index.html")

# vue pour l'article_01
def article (request, numero):
    if numero in ['01', '02', '03']:
        return render(request, f"blog/article_{numero}.html")
    else:
        return render(request, "blog/articleNonTrouve.html")