from django import forms

class ArticuloForm(forms.Form):
    texto = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        help_text=""
    )
    
