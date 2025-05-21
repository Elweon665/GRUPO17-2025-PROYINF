from django.shortcuts import render, get_object_or_404, redirect
from .models import Scrap, Summary
from .forms import ArticleForm, SummaryFormSet
from Article_Summarizer.program.summarizer import generarResumen
from django.utils import timezone


def editarArticulo(request, pk):
    article = get_object_or_404(Scrap, pk=pk)
    summary = Summary.objects.filter(pk=article.pk).first()
    if summary:
        summary = get_object_or_404(Summary, pk=article.pk)
    else:
        summary = Summary(pk=article.pk)
        
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

            for summary in summaries:
                if not summary.summary:
                    summary.summary = generarResumen(article.content)
                    summary.summaryDate = timezone.now()
                summary.article = article 
                summary.save()
            formset.save_m2m()
            
            summary = Summary.objects.filter(pk=article.pk).first()
            if summary:
                summary = get_object_or_404(Summary, pk=article.pk)
            else:
                summary = Summary(pk=article.pk)
                
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