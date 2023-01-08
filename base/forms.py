from django.forms import ModelForm
from .models import Product, Article

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'