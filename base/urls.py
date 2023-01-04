from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.allproducts, name="allproducts"),
    path('products/<slug:slug>/', views.products, name="products"),
    path('product/<slug:slug>/', views.product, name="product"),
    path('login/', views.emaillookup, name="emaillookup"),
    path('password/', views.password, name="password"),
    path('signup/', views.signup, name="signup"),
    path('article/<slug:slug>/', views.article, name="article"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)