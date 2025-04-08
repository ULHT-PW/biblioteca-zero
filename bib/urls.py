from django.urls import path, include
from . import views

urlpatterns = [
    path('autores-json/', views.autores_json_view),
    path('autores/', views.autores_view, name='autores'),
    path('livros/', views.livros_view, name='livros'),
    path('autores/<int:autor_id>', views.autor_view, name='autor_path')
]