from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('shop/', views.shop, name="shop"),
    path('product/', views.product, name="product"),
    path('login/', views.emaillookup, name="emaillookup"),
    path('password/', views.password, name="password"),
    path('signup/', views.signup, name="signup"),
]