from django.urls import path
from galeria.views import index, imagem, busca

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("busca", busca, name="busca"),
]