from django.db import models
from django.utils import timezone
from scraping.models import Scrap

class Summary(models.Model):
    article = models.OneToOneField(
        Scrap,
        on_delete=models.CASCADE,
        primary_key=True
    )
    summary = models.TextField()
    summaryDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.article.title