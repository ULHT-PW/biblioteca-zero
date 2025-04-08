from django.shortcuts import render
from django.http import JsonResponse
from biblioteca.models import Autor, Livro

# Create your views here.

def autores_json_view(request):
    autores = list(Autor.objects.values())
    return JsonResponse(autores, safe=False)


def about_view(request):
    context = {
        'ano': 2025,
        'autores': Autor.objects.all().order_by('nome')
    }
    return render(request, "bib/autores.html", context)


def autores_view(request):
    context = {
        'ano': 2025,
        'autores': Autor.objects.all().order_by('nome')
    }
    return render(request, "bib/autores.html", context)


def livros_view(request):
    context = {
        'ano': 2025,
        'livros': Livro.objects.all()
    }
    return render(request, "bib/livros.html", context)



def autor_view(request, autor_id):
    context = {
        'autor': Autor.objects.get(id=autor_id)
    }
    return render(request, "bib/autor.html", context)