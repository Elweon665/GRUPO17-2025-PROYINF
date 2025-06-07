from django import forms
from .models import Summary
from scraping.models import Scrap
from django.forms.models import inlineformset_factory

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Scrap
        fields = ['title', 'link', 'content']
        labels = {
            'title': 'Título',
            'link': 'URL',
            'content': 'Contenido',
        }
        widgets = {
            'title': forms.TextInput(attrs={'style': 'width: 100%;'}),
            'link': forms.URLInput(attrs={'style': 'width: 100%;'}),
            'content': forms.Textarea(attrs={'style': 'width: 100%;'}),
        }

class SummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        fields = ['summary', 'summaryDate']
        labels = {
            'summary': 'Resumen (Si se deja vacio se generará uno automáticamente)',
            'summaryDate': 'Fecha del resumen actual',
        }
        widgets = {
            'summary': forms.Textarea(attrs={'style': 'width: 100%;'}),
            'summaryDate': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'style': 'width: 100%;'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['summary'].required = False
        self.fields['summaryDate'].disabled = True

SummaryFormSet = inlineformset_factory(
    Scrap,
    Summary,
    form=SummaryForm,
    extra=1,
    can_delete=False
)

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