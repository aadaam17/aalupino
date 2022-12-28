from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('shop/<str:pk>/', views.shop, name="shop"),
    path('product/<str:pk>/', views.product, name="product"),
    path('login/', views.emaillookup, name="emaillookup"),
    path('password/', views.password, name="password"),
    path('signup/', views.signup, name="signup"),
    path('article/<str:pk>/', views.article, name="article"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)