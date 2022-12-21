from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def shop(request, pk):
    return render(request, 'shop.html')

def product(request, pk):
    product = None
    #for i in products:
        #if i['id'] == int(pk):
            #product = i
    #context = {'product': product}
    return render(request, 'product.html')

def emaillookup(request):
    return render(request, 'emaillookup.html')

def password(request):
    return render(request, 'password.html')

def signup(request):
    return render(request, 'signup.html')

def article(request, pk):
    return render(request, 'article.html')
    