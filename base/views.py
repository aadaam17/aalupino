from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def shop(request):
    return render(request, 'shop.html')

def product(request):
    return render(request, 'product.html')

def emaillookup(request): 
    return render(request, 'emaillookup.html')

def password(request): 
    return render(request, 'password.html')

def signup(request): 
    return render(request, 'signup.html')
    