from django.shortcuts import render
from .models import Product, Article

# Create your views here.

def home(request):
    articles = Article.objects.all()[0:7]
    context = {'articles': articles}
    return render(request, 'home.html', context)

def shop(request, pk):
    articles = Article.objects.all()[0:7]
    context = {'articles': articles}
    return render(request, 'shop.html', context)

def product(request, pk):
    product = Product.objects.get(id=pk)
    articles = Article.objects.all()[0:7]
    context = {'product': product, 'articles': articles}
    return render(request, 'product.html', context)

def emaillookup(request):
    return render(request, 'emaillookup.html')

def password(request):
    return render(request, 'password.html')

def signup(request):
    return render(request, 'signup.html')

def article(request, pk):
    article = Article.objects.get(id=pk)
    context = {'article': article}
    return render(request, 'article.html', context)