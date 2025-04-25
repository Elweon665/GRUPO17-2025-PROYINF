from django import forms

class ArticuloForm(forms.Form):
    texto = forms.CharField(
        label="Pon tu artículo aquí.",
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        help_text="Pega aquí el artículo que quieres resumir."
    )
    
