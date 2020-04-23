from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BlogPostModelForm
from .models import BlogPostModel

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

#pagina con la lista delle applicazioni  
def home(request): 
    blog_command = ['esempi','blog']
    context = {
        'menu': blog_command,
    }
    return render(request, "/index.html", context)

#pagina con la lista dei comandi disponibili
def index(request): 
    blog_command = ['crea-post','lista-post']
    context = {
        'blog_command': blog_command,
    }
    return render(request, "blog/index.html", context)

#Creazione del post
@login_required(login_url='/accounts/login/')
def creaPostView(request):
    if request.method == "POST": 
        form = BlogPostModelForm(request.POST) #ottengo il form dalla richiesta
        if form.is_valid():     #validazione del form
            print("Il Form è Valido!")
            new_post = form.save()  #creo il post nel db
            print("new_post: ", new_post)
            return HttpResponseRedirect("lista-post")
    else: #se la chiamata non è POST vuol dire che è la prima chiamata GET, quindi mostro il form vuoto
        form = BlogPostModelForm()
    context = {"form": form}   #contesto dei parametri da passare al render
    return render(request, "blog/crea_post.html", context)  #passo il form alla pagina per il render

#Modifica del post
@login_required(login_url='/accounts/login/')
def modificaPostView(request, pk=None):
    obj = get_object_or_404(BlogPostModel, pk=pk) #carico il post in base alla chiave primaria pk
    form = BlogPostModelForm(request.POST or None, instance=obj)  #passo l'oggetto post al form
    if request.method == 'POST': 
        if form.is_valid():
           form.save()
           return redirect('/blog/lista-post')
    context = {"form": form,"pk":pk} #creo i parametri
    return render(request, 'blog/modifica_post.html', context)

#Elimina del post
@login_required(login_url='/accounts/login/')
def eliminaPostView(request, pk=None):
    obj = get_object_or_404(BlogPostModel, pk=pk) #carico il post in base alla chiave primaria pk
    obj.delete()
    #return HttpResponse("<h1>post eliminato con successo!</h1>")
    return HttpResponseRedirect("lista-post")

 
# Class based views
# provide an alternative way to implement views as Python objects instead of functions
# more extensible and flexible than their function-based counterparts
# https://docs.djangoproject.com/en/3.0/topics/class-based-views/intro/

class PostDetailView(DetailView):
    model = BlogPostModel #modello dei dati da utilizzare 
    template_name = "blog/post_detail.html" #pagina per mostrare i dati


class listaPostView(ListView):
    model = BlogPostModel #modello dei dati da utilizzare 
    template_name = "blog/lista_post.html"  #pagina per mostrare i dati
    
    #recupera di dati da passare alla pagina per il render
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = BlogPostModel.objects.all()
        return context


