from Article_Summarizer.program.summarizer import generarResumen
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Summary


def generate_summary_status(summary, article):
    return get_object_or_404(Summary, pk=article.pk) if summary else Summary(pk=article.pk)

def summary_generator(summaries, article):
    for summary in summaries:
        if not summary.summary:
            summary.summary = generarResumen(article.content)
            summary.summaryDate = timezone.now()
        summary.article = article 
        summary.save()