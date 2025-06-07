from django.urls import path
from . import views

urlpatterns = [
    path('editar/<int:pk>/', views.editarArticulo, name='editar_articulo'),
    path('insert/', views.insertarArticulo, name='insertar_articulo'),
    path('', views.Articulo_view, name='articles')
]