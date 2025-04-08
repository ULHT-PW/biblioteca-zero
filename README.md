# Tutorial: criação de web app em Django com views, templates e urls.

### Recursos
* Aplicação biblioteca: https://bibliotecalusofona.pythonanywhere.com/
* Código: https://github.com/ULHTPW/bibliotecalusofona/tree/main/biblioteca
* Aplicação admin (usr:admin, pwd:admin): https://bibliotecalusofona.pythonanywhere.com/admin/

### Passos já realizados
Considera-se que:
* já foi feita a modelação dos dados da aplicação em [models.py](https://github.com/ULHT-PW/bibliotecalusofona/blob/main/biblioteca/models.py)
* existem disponiveis na [pasta json](https://github.com/ULHT-PW/bibliotecalusofona/tree/main/biblioteca/json) dados para alimentar a base de dados
* foram carregados dados disponiveis em JSON, usando um [script](https://github.com/ULHT-PW/bibliotecalusofona/blob/main/biblioteca/loader.py)  

### Passos para criação da aplicação
1. Analisar a modelação em [models.py](https://github.com/ULHT-PW/bibliotecalusofona/blob/main/biblioteca/models.py)
2. Ver dados na aplicação [admin](https://bibliotecalusofona.pythonanywhere.com/admin) (usr:admin, pwd:admin)
3. Analisar como [admin.py](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/admin.py) configura a visualização das tabelas, em particular o uso de ordering, list_display, list_filter, inlines
4. Criar [layout.html](https://github.com/ULHT-PW/bibliotecalusofona/blob/main/biblioteca/templates/biblioteca/layout.html), para herança de templates.
5. Em views, [importar](https://github.com/ULHT-PW/bibliotecalusofona/blob/ed89e9b8fbd2ead9b8e704be424c8c8c5da3b30a/biblioteca/views.py) os modelos Autor e Livro para poder inserir dados
5. Página de autores:
    1. Para listar autores, criar a view [index_view](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/views.py)
    1. Criar template [index.html](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/index.html) que liste autores
    1. Criar caminho para a view index_view em [urls.py](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/urls.py)
1. Página de um autor
    1. Para apresentar informação de um autor, criar a view [autor_view](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/views.py)
    1. Criar template [autor.html](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/autor.html), que apresente todas as informações do autor, incluindo seu [retrato](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/autor.html) e lista de livros. 
    1. Criar [templatetag](https://github.com/ULHT-PW/bibliotecalusofona/blob/main/biblioteca/templatetags/biblioteca_extras.py) para ordenar os livros pelo ano de publicação. Usar filtro [livros_ordenados](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/autor.html) no template.
    1. Criar caminho para a view autor_view em [urls.py](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/urls.py)
    1. Inserir, na lista de autores, um [link no autor](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/index.html), para a respetiva página do autor
1. Página de géneros:
    1. Para listar géneros, criar a view [generos_view](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/views.py), onde cria a [lista de géneros](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/views.py) 
    1. Criar template [generos.html](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/generos.html) que liste os géneros
    1. Criar [caminho generos](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/urls.py) para a view generos_view, em urls.py
1. Página de género:
    1. Para apresentar [lista](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/views.py) dos livros de um género, criar a view [genero_view](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/views.py)
    1. Criar template [genero.html](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/autor.html), que apresente livros de um género. 
    1. Criar [caminho genero](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/urls.py) para a view genero_view, em urls.py
    1. Inserir, na lista de géneros, um [link no genero](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/generos.html), para a página do género
1. Incluir, no template layout.html, [menu com links](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/layout.html) para as páginas autores e géneros.


# Formulário de criação de novo autor

1. na pasta da sua aplicação, onde está `views.py`, criar `forms.py` com ModelForm `AutorForm`, formulário que terá como base a classe Autor.
```python
from django import forms    # formulários Django
from .models import Autor   

class AutorForm(forms.ModelForm):
  class Meta:
    model = Autor        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.
```
2. em `views.py`, criar view `novo_autor_view`
```python
def novo_autor_view(request):

    form = AutorForm()      # form é uma instancia de AutorForm,
                            # formulário em branco com os campos de Autor

    context = {'form': form}
    return render(request, 'biblioteca/novo_autor.html', context)
```
3. em `urls.py`, criar novo caminho para a view criada
```python
    path('autor/novo', views.novo_autor_view, name="novo_autor")
```
4. Criar template `novo_autor.html`
```html
{% extends 'biblioteca/layout.html' %}

{% block content %}
    <h3>Novo Autor</h3>
    
    <form action="" method="post" enctype='multipart/form-data'>
    <!-- enctype deve ser definido se houver submissão de ficheiros ou imagens -->

      {% csrf_token %}   <!-- obrigatório nos forms Django -->
      <table>
          {{ form }}   <!-- insere input para cada atributo da classe Autor, numa tabela -->
      </table>
      <input type="submit" value="Criar autor"> 

    </form>      

{% endblock %}
```
5. Em `index.html`, depois da lista de autores, inserir um botão com link para o caminho `novo_autor`
```html
    <a href="{% url 'novo_autor' %}">
        <button>Inserir novo Autor</button>
    </a>
```
6. visualizar a página na aplicação
7. configurar a view `novo_autor_view` para receber os valores submetidos através do formulário, guardando-os e redirecionando para a lista de autores
```python
def novo_autor_view(request):

    # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido. 
    # Senão, o form não tem dados e não é válido
    form = AutorForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('autores')
    
    context = {'form': form}
    return render(request, 'biblioteca/novo_autor.html', context)
```
8. visualizar aplicação. Vamos remover mensagem de obrigatorio? em `layout.html`, no elemento `<style>`:
```css
.errorlist {
    display:none;
}
```
# Edita autor
1. cria nova view `edita_autor_view`. 
```python
def edita_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    
    if request.POST:
        form = AutorForm(request.POST or None, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autores')
    else:
        form = AutorForm(instance=autor)  # cria formulário com dados da instância autor
        
    context = {'form': form, 'autor':autor}
    return render(request, 'biblioteca/edita_autor.html', context)
```
2. cria novo HTML para editar
```html
{% extends 'biblioteca/layout.html' %}

{% block content %}
    <h3>Edita Autor</h3>
    
    <form action="{% url 'edita_autor' autor.id %}" method="post" enctype='multipart/form-data'>
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit">
    </form>      

{% endblock %}
```
3. criar novo caminho em `urls.py`
```python
    path('autor/<int:autor_id>/edita', views.edita_autor_view,name="edita_autor")
```
4. inserir no `autor.html`, um botão com um link para `edita_autor`
```html
    <a href="{% url 'edita_autor' autor.id %}">
        <button>Editar informação do Autor</button>
    </a>
```

# Apagar autor
1. cria nova view
```python
def apaga_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    autor.delete()
    return redirect('autores')
```
2. criar novo caminho em `urls.py`
```python
    path('autor/<int:autor_id>/apaga', views.apaga_autor_view,name="apaga_autor"),
```
3. inserir no `autor.html`, um botão com um link para `apaga_autor`
```html
    <a href="{% url 'apaga_autor' autor.id %}">
      <button>Apagar autor e seus livros</button>
    </a>
```

# Novo Livro
1. cria novo ModelForm `LivroForm` em `forms.py`
```python
class LivroForm(forms.ModelForm):
  class Meta:
    model = Livro
    fields = '__all__'
```
2. cria nova view
```python
def novo_livro_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)  # Retrieve the Autor object using autor_id
    form = LivroForm(request.POST or None, request.FILES)

    if form.is_valid():
        livro = form.save(commit=False)  # cria objeto Livro sem gravar na base de dados
        livro.autor = autor  
        livro.save()  
        return redirect('autores')
    
    context = {'form': form}
    return render(request, 'biblioteca/novo_livro.html', context)
```
3. Criar template `novo_livro.html`
```html
{% extends 'biblioteca/layout.html' %}

{% block content %}
    <h3>Novo Livro</h3>
    
    <form action="" method="post" enctype='multipart/form-data'>
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit">
    </form>      

{% endblock %}
```
4. criar novo caminho em `urls.py`
```python
    path('livro/novo/', views.novo_livro_view,name="novo_livro"),
```

# Refinando o form
1. inserção de widgets, labels e help_texts
```python
from django import forms
from .models import Autor, Livro

class AutorForm(forms.ModelForm):
  class Meta:
    model = Autor
    fields = '__all__'

    widgets = {
      'nome': forms.TextInput(attrs={
          'placeholder':'Nome completo',
      })
    }    

class LivroForm(forms.ModelForm):
  class Meta:
    model = Livro
    fields = '__all__'
    
    labels = {
      'titulo': 'Título',
      'ano_publicacao': 'Ano de Publicação',
    }
    
    help_texts = {
      'ano_publicacao': 'verifique o ano de publicação', 
    }
```

# Utilizadores
Registo, login, logout, autenticação, restrições de acesso a views e elementos HTML. Esta matéria será lecionada na semana de 29.4. 

Passos: 
1. Crie template
2. Em views.py, crie view
3. Em urls.py, crie caminho

# Registo
1. Crie um template `registo.html` com formulário que recolhe as credenciais e as reenvia para a view `registo`
```html
{% extends 'biblioteca/layout.html' %}

{% block content %}
    <h3>Registo</h3>
    
    <form action="{% url 'registo' %}" method="post">
      {% csrf_token %}
      <input type="text" name="username" placeholder="O seu username..">
      <input type="text" name="nome" placeholder="O seu nome..">
      <input type="text" name="apelido" placeholder="O seu apelido..">
      <input type="email" name="email" placeholder="O seu email..">
      <input type="password" name="password" placeholder="Defina a sua password..">
      <input type="submit" value="Criar">
    </form> 
    
    <a href="{% url 'login' %}">Cancelar</a>

{% endblock %}
```
2. em `views.py`, crie `registo_view` para criar novo utilizador
```python
from django.contrib.auth import models

def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('login')
        
    return render(request, 'biblioteca/registo.html')
```
3. em `urls.py`, crie caminho `registo`
```python
    path('registo/', views.registo_view, name="registo"),
```

## Login
1. crie template `login.html`  com formulário que pede as credenciais e as reenvia para a view `login`
```html
{% extends 'biblioteca/layout.html' %}

{% block content %}
    <h3>Login</h3>
    
    {% if mensagem %}
      <p>mensagem: {{ mensagem }}</p>
    {% endif %}
    <form action="{% url 'login' %}" method="post">
      {% csrf_token %}
      <input type="text" name="username" placeholder="Username..">
      <input type="password" name="password" placeholder="Password..">
      <input type="submit">
    </form>      

{% endblock %}
```
2. em `layout.html`, crie botão para fazer login
```html
    <h1>Biblioteca da Lusofonía</h1>
    
    <a href="{% url 'autores' %}"><button>Autores</button></a>
    <a href="{% url 'generos' %}"><button>Géneros</button></a>

    <a href="{% url 'login' %}"><button>Login</button></a>
```
3. em `views.py`, crie `login_view` para autenticar e fazer login
```python
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return render(request, 'biblioteca/user.html')
        else:
            render(request, 'biblioteca/login.html', {
                'mensagem':'Credenciais inválidas'
            })
        
    return render(request, 'biblioteca/login.html')
```
4.  em `urls.py`, crie caminho `login`
```python
    path('login/', views.login_view, name="login"),
```
5.  em `views.py`, inserir decorador `@login_required` em views que requeiram estar autenticado.
```python
from django.contrib.auth.decorators import login_required

@login_required
def apaga_autor_view(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    autor.delete()
    return redirect('autores')
```
6. Usar `request.user.is_authenticated` para avaliar se está autenticado em templates (nas views usar decorador @login_required). Tipicamente, links para operações Create/Update/Delete só deverão ser renderizados se estivermos autenticados. Por exemplo, em `layout.html`, só permite criar novo autor se estiver autenticado.
```html
{% if request.user.is_authenticated %}
    <a href="{% url 'novo_autor' %}">
        <button>Inserir novo Autor</button>
    </a>
{% endif %}
```

## Logout
1. em `views.py`, crie `logout_view` com chamada da função `logout(request)`
```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('autores')
```
2. em `urls.py`, crie caminho `logout`
```python
    path('logout/', views.logout_view, name="logout"),
```
3.  em `layout.html`, crie botão `logout` que aparece se estiver autenticado
```html
    {% if request.user.is_authenticated %}
        Username:{{request.user.username}}
        <a href="{% url 'logout' %}"><button>Logout</button></a>
    {% else %}
        <a href="{% url 'login' %}"><button>Login</button></a>
    {% endif %}
```
