from django.shortcuts import render, redirect
from .models import Product, Article
from .forms import ProductForm, ArticleForm

# Create your views here.

def home(request):
    articles = Article.objects.all()[0:7]
    context = {'articles': articles}
    return render(request, 'base/home.html', context)

def allproducts(request):
    products = Product.objects.all()
    articles = Article.objects.all()[0:7]
    context = {
        'products': products, 
        'articles': articles
    }
    return render(request, 'base/products.html', context)

def products(request, slug):
    products = Product.objects.filter(cat_slug=slug) or Product.objects.filter(tag_slug=slug)
    articles = Article.objects.all()[0:7]
    context = {
        'articles': articles,
        'products': products,
        }
    return render(request, 'base/products.html', context)

def product(request, slug):
    product = Product.objects.get(pro_slug=slug)
    articles = Article.objects.all()[0:7]
    context = {
        'product': product, 
        'articles': articles
        }
    return render(request, 'base/product.html', context)

def emaillookup(request):
    return render(request, 'base/emaillookup.html')

def password(request):
    return render(request, 'base/password.html')

def signup(request):
    return render(request, 'base/signup.html')

def profile(request):
    products = Product.objects.all()
    articles = Article.objects.all()
    context = {
        'products': products,
        'article': articles,
    }
    return render(request, 'base/profile.html', context)

def article(request, slug):
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(request, 'base/article.html', context)

def createProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'base/product_form.html', context)

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'base/product_form.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('profile')
    return render(request, 'base/delete.html', {'obj': product})

def createArticle(request):
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'base/article_form.html', context)

def updateArticle(request, pk):
    article = Article.objects.get(id=pk)
    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'base/article_form.html', context)

def deleteArticle(request, pk):
    article = Article.objects.get(id=pk)
    
    if request.method == 'POST':
        article.delete()
        return redirect('profile')
    return render(request, 'base/delete.html', {'obj': article})