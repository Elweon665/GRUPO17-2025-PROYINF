from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/editar/', views.editarArticulo, name='editar_articulo'),
    path('insert/', views.insertarArticulo, name='insertar_articulo')
]