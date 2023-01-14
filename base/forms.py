from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from .models import User, Product, Article

class UserForm(UserCreationForm):
    email = forms.CharField(required=True, widget=forms.HiddenInput())
    password2 = None
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'date_of_birth',)

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        try:
            password_validation.validate_password(password1, self.instance)
        except forms.ValidationError as error:

            # Method inherited from BaseForm
            self.add_error('password1', error)
        return password1

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'