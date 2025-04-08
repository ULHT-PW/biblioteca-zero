
from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index_view),
    path('bom-ano/<str:ano>', views.bom_ano_view),
]
