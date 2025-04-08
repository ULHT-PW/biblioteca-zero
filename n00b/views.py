from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_view(request):
    return HttpResponse("Olá n00b, esta é a pagina mais basica do mundo!")


def bom_ano_view(request, ano):
    return HttpResponse(f"bom {ano}!")
