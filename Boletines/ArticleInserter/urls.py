from django.urls import path
from . import views

urlpatterns = [
    path('', views.editarArticulo, name='editar_articulo'),
]