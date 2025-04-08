# biblioteca-zero

Aplicação desenvolvida na aula teórica: https://bibliotecalusofona.pythonanywhere.com/bib/autores

### Recursos
* Aplicação biblioteca: https://bibliotecalusofona.pythonanywhere.com/
* Código: https://github.com/ULHTPW/bibliotecalusofona/tree/main/biblioteca
* Aplicação admin (usr:admin, pwd:admin): https://bibliotecalusofona.pythonanywhere.com/admin/

### Passos a Rever

* crie na consola a aplicação bib com o comando `python manage.py startapp bib`
* em `settings.py`, adicione o `'bib'` em `INSTALLED_APPS` ([link](https://github.com/ULHT-PW/biblioteca-zero/blob/485ca030af11a407a85f541aefbc47afe22d1d6b/project/settings.py#L43))
* crie um caminho em `urls.py` ([link](https://github.com/ULHT-PW/biblioteca-zero/blob/485ca030af11a407a85f541aefbc47afe22d1d6b/project/urls.py#L24))
* crie na pasta `/bib` um ficheiro `urls.py` para definir os caminhos da aplicação ([link](https://github.com/ULHT-PW/biblioteca-zero/blob/main/bib/urls.py))
* em `views.py` crie uma função que retorne o que queira. ([link](https://github.com/ULHT-PW/biblioteca-zero/blob/485ca030af11a407a85f541aefbc47afe22d1d6b/bib/views.py#L12))
* crie uma pasta `templates\bib\` onde guarda os ficheiros HTML a renderizar pela função ([link](https://github.com/ULHT-PW/biblioteca-zero/tree/main/bib/templates/bib))
* utilize a linguagem template do Django para renderizar dados. 
* a `base.html` permite ter várias paginas com o mesmo layout ([link]([url](https://github.com/ULHT-PW/biblioteca-zero/blob/main/bib/templates/bib/base.html))) 
* em `urls.py` crie um caminho para essa função ([link](https://github.com/ULHT-PW/biblioteca-zero/blob/485ca030af11a407a85f541aefbc47afe22d1d6b/bib/urls.py#L6))
