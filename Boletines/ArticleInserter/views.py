from django.shortcuts import render, get_object_or_404, redirect
from .models import Scrap, Summary
from .forms import ArticleForm, SummaryFormSet, ArticleInserterForm
from Article_Summarizer.program.summarizer import generarResumen
from django.utils import timezone
from django.core.paginator import Paginator
from .functions import summary_generator, generate_summary_status


def editarArticulo(request, pk):
    article = get_object_or_404(Scrap, pk=pk)
    summary = Summary.objects.filter(pk=article.pk).first()
    summary = generate_summary_status(summary, article)
    if request.method == 'POST':
        if 'delete' in request.POST:
            article.delete()
            return redirect('/articles/')
        form = ArticleForm(request.POST, instance=article)
        formset = SummaryFormSet(request.POST, instance=article)
        if form.is_valid() and formset.is_valid():
            form.save()
            
            article = get_object_or_404(Scrap, pk=pk)
            summaries = formset.save(commit=False)

            summary_generator(summaries, article)
            
            formset.save_m2m()
            
            summary = Summary.objects.filter(pk=article.pk).first()
            summary = generate_summary_status(summary, article)
                
            form = ArticleForm(instance=article)
            formset = SummaryFormSet(instance=article)
            
            message = True
            
            return render(request, 'edit_article.html', {
                'form': form,
                'formset': formset,
                'article': article,
                'summary':summary,
                'message': message
            })
    else:
        form = ArticleForm(instance=article)
        formset = SummaryFormSet(instance=article)

    return render(request, 'edit_article.html', {
        'form': form,
        'formset': formset,
        'article': article,
        'summary':summary
    })
    
def insertarArticulo(request):
    send = False
    form = ArticleInserterForm()
    
    if request.method == 'POST':
        form = ArticleInserterForm(request.POST)
        if form.is_valid():
            # Guardar valores en la BD y Generar resumen si es que no se ingresó
            article = Scrap()
            article.title = form.cleaned_data['title']
            article.link = form.cleaned_data['link']
            article.content = form.cleaned_data['content']
            
            resumen = form.cleaned_data['summary']
            summary = Summary()
            if not resumen:
                summary.summary = generarResumen(article.content)
            else:
                summary.summary = resumen
            article.save()
            summary.article = article
            summary.save()
                
            send = True
        else:
            return render(request, 'insert_article.html', {'form':form,'error':True})
    return render(request, 'insert_article.html', {'form':form,'send':send})


def Articulo_view(request):
    scraps_list = Scrap.objects.all().order_by('-id')  
    paginator = Paginator(scraps_list, 20)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    current = page.number
    total = paginator.num_pages
    page_range = [1]

    dots = False
    for num in range(2, total + 1):
        if num < current - 2 or num > current + 2:
            if not dots:
                page_range.append("...")
                dots = True
        else: 
            page_range.append(num)
            dots = False
    
    if page_range[-1] != total:
        page_range.append(total)
            
    return render(request, 'Articulos.html', {'page_obj':page,'page_range':page_range})
    