from django.urls import path
from .views import ver_resumen

urlpatterns = [
    path('', ver_resumen, name='summarizer'),
]