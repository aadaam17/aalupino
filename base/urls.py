from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.allproducts, name="allproducts"),
    path('products/<slug:slug>/', views.products, name="products"),
    path('product/<slug:slug>/', views.product, name="product"),
    path('article/<slug:slug>/', views.article, name="article"),
    path('profile/', views.profile, name="profile"),

    path('login/', views.emaillookup, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('password/', views.password, name="password"),
    path('signup/', views.register, name="signup"),

    path('create-product/', views.createProduct, name="create-product"),
    path('create-article/', views.createArticle, name="create-article"),
    path('update-product/<str:pk>/', views.updateProduct, name="update-product"),
    path('update-article/<str:pk>/', views.updateArticle, name="update-article"),

    path('delete-product/<str:pk>/', views.deleteProduct, name="delete-product"),
    path('delete-article/<str:pk>/', views.deleteArticle, name="delete-article"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)