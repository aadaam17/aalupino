from django.shortcuts import render
from .models import Product, Article

# Create your views here.

def home(request):
    articles = Article.objects.all()[0:7]
    context = {'articles': articles}
    return render(request, 'home.html', context)

def allproducts(request):
    products = Product.objects.all()
    articles = Article.objects.all()[0:7]
    context = {
        'products': products, 
        'articles': articles
    }
    return render(request, 'products.html', context)

def products(request, slug):
    products = Product.objects.filter(cat_slug=slug) or Product.objects.filter(tag_slug=slug)
    articles = Article.objects.all()[0:7]
    context = {
        'articles': articles,
        'products': products,
        }
    return render(request, 'products.html', context)

def product(request, slug):
    product = Product.objects.get(pro_slug=slug)
    articles = Article.objects.all()[0:7]
    context = {
        'product': product, 
        'articles': articles
        }
    return render(request, 'product.html', context)

def emaillookup(request):
    return render(request, 'emaillookup.html')

def password(request):
    return render(request, 'password.html')

def signup(request):
    return render(request, 'signup.html')

def article(request, slug):
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(request, 'article.html', context)