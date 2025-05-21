from django import forms
from .models import Tag
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth.forms import UserCreationForm

class TagSelectionForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'select2'})
    )
    
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, max_length=50)
    
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'nombre', 'password2']
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2
    
class ArticleInserterForm(forms.Form):
    title = forms.CharField(
        label="Title", 
        required=True,
        widget=forms.TextInput(attrs={
            'style': 'width: 100%;'
        }))
    
    link = forms.URLField(
        label="Link", 
        required=True,
        widget=forms.TextInput(attrs={
            'style': 'width: 100%;'
        }))
    
    content = forms.CharField(
        label="Artículo", 
        required=True,
        widget=forms.Textarea(attrs={
            'style': 'width: 100%;'
        })
        )
    
    summary = forms.CharField(
        label="Resumen (opcional)", 
        required=False,
        widget=forms.Textarea(attrs={
            'style': 'width: 100%;'
        })
        )