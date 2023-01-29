from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import User, Product, Article
from .forms import UserForm, ProductForm, ArticleForm

# Create your views here.
def emaillookup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        request.session['email'] = email 

        try:
            user = User.objects.get(email=email)
            return redirect('password')
        except:
            return redirect('signup')

    context = {}
    return render(request, 'base/emaillookup.html', context)

def password(request):
    if 'email' in request.session:
        email = request.session['email']
    else:
        return redirect('login')

    if request.method == 'POST':
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Incorrect Password')

    context = {'email': email}
    return render(request, 'base/password.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def register(request):
    if 'email' in request.session:
        email = request.session['email']
    else:
        return redirect('login')

    form = UserForm()
    form.fields['email'].initial = email

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            return redirect('login')
        else:
            messages.error(request, 'An error occured during registration')

    context = {
        'email': email,
        'form': form,
        }
    return render(request, 'base/signup.html', context)

def home(request):
    articles = Article.objects.all()[0:7]
    context = {'articles': articles}
    return render(request, 'base/home.html', context)

def allproducts(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    products = Product.objects.filter(
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(category__icontains=q) |
        Q(tag__icontains=q)
    )

    product_count = products.count()
    articles = Article.objects.all()[0:7]
    context = {
        'products': products, 
        'articles': articles,
        'product_count': product_count,
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

@login_required(login_url='login')
def dashboard(request):
    products = Product.objects.all()
    articles = Article.objects.all()

    context = {
        'products': products,
        'articles': articles,
    }
    return render(request, 'base/dashboard.html', context)

@login_required(login_url='login')
def profile(request):
    products = Product.objects.all()
    articles = Article.objects.all()
    context = {
        'products': products,
        'articles': articles,
    }
    return render(request, 'base/profile.html', context)

def article(request, slug):
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(request, 'base/article.html', context)

@login_required(login_url='login')
def createProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'base/product_form.html', context)

@login_required(login_url='login')
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'base/product_form.html', context)

@login_required(login_url='login')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('dashboard')
    return render(request, 'base/delete.html', {'obj': product})

@login_required(login_url='login')
def createArticle(request):
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'base/article_form.html', context)

@login_required(login_url='login')
def updateArticle(request, pk):
    article = Article.objects.get(id=pk)
    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'base/article_form.html', context)

@login_required(login_url='login')
def deleteArticle(request, pk):
    article = Article.objects.get(id=pk)
    
    if request.method == 'POST':
        article.delete()
        return redirect('dashboard')
    return render(request, 'base/delete.html', {'obj': article})