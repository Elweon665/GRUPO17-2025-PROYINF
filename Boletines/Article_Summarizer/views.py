from django.shortcuts import render
from .program.summarizer import generarResumen
from .forms import ArticuloForm

def ver_resumen(request):
    resumen = None
    
    if request.method == "POST":
        form = ArticuloForm(request.POST)
        if form.is_valid():
            resumen = generarResumen(form.cleaned_data['texto'])
    
    else:
        form = ArticuloForm()
    
    return render(request, 'summarizer.html', {'form': form, 'resumen': resumen})