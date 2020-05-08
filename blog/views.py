from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BlogPostModelForm, BlogCommentModelForm
from .models import BlogPostModel, BlogCommentModel

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse


# Create your views here.

# pagina con la lista delle applicazioni
def home(request):
    blog_command = ['esempi', 'blog']
    context = {
        'menu': blog_command,
    }
    return render(request, "/index.html", context)


# pagina con la lista dei comandi disponibili
def index(request):
    blog_command = ['crea-post', 'lista-post']
    context = {
        'blog_command': blog_command,
    }
    return render(request, "blog/index.html", context)


# Creazione del post
@login_required(login_url='/accounts/login/')
def creaPostView(request):
    if request.method == "POST":
        form = BlogPostModelForm(request.POST)  # ottengo il form dalla richiesta
        if form.is_valid():  # validazione del form
            print("Il Form è Valido!")
            new_post = form.save(commit=False)  # creo il post ma non salvo
            new_post.autore = request.user
            print("new_post: ", new_post)
            new_post.save()
            return HttpResponseRedirect("lista-post")
    else:  # se la chiamata non è POST vuol dire che è la prima chiamata GET, quindi mostro il form vuoto
        form = BlogPostModelForm()
    context = {"form": form}  # contesto dei parametri da passare al render
    return render(request, "blog/crea_post.html", context)  # passo il form alla pagina per il render


# Creazione del commento
@login_required(login_url='/accounts/login/')
def creaCommentView(request,pk):
    post = get_object_or_404(BlogPostModelForm, pk=pk)
    if request.method == "POST":
        form = BlogCommentModelForm(request.POST)  # ottengo il form dalla richiesta
        if form.is_valid():  # validazione del form
            print("Il Form è Valido!")
            new_comment = form.save(commit=False)  # creo il post ma non salvo
            new_comment.post = post
            new_comment.autore = request.user
            print("new_comment: ", new_comment)
            new_comment.save()
            url_discussione = reverse("risposte_post", kwargs={"pk": pk})
            return HttpResponseRedirect(url_discussione)
    else:  # se la chiamata non è POST vuol dire che è la prima chiamata GET, quindi mostro il form vuoto
        form = BlogCommentModelForm()
    context = {"form": form}  # contesto dei parametri da passare al render
    return render(request, "blog/crea_comment.html", context)  # passo il form alla pagina per il render


# Modifica del post
@login_required(login_url='/accounts/login/')
def modificaPostView(request, pk=None):
    obj = get_object_or_404(BlogPostModel, pk=pk)  # carico il post in base alla chiave primaria pk
    form = BlogPostModelForm(request.POST or None, instance=obj)  # passo l'oggetto post al form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/blog/lista-post')
    context = {"form": form, "pk": pk}  # creo i parametri
    return render(request, 'blog/modifica_post.html', context)


# Elimina del post
@login_required(login_url='/accounts/login/')
def eliminaPostView(request, pk=None):
    obj = get_object_or_404(BlogPostModel, pk=pk)  # carico il post in base alla chiave primaria pk
    obj.delete()
    # return HttpResponse("<h1>post eliminato con successo!</h1>")
    return HttpResponseRedirect("lista-post")


# Class based views
# provide an alternative way to implement views as Python objects instead of functions
# more extensible and flexible than their function-based counterparts
# https://docs.djangoproject.com/en/3.0/topics/class-based-views/intro/

class PostDetailView(DetailView):
    model = BlogPostModel  # modello dei dati da utilizzare
    template_name = "blog/post_detail.html"  # pagina per mostrare i dati

#questa sotto dovrà sostituire quella sopra

def PostDetailView2(request, pk):
    post = get_object_or_404(BlogPostModel, id=pk)
    # List of active comments for this post
    comments = post.comments.filter(attivo=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = BlogCommentModelForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.autore = request.user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = BlogCommentModelForm()
    
    context= {'post': post,
              'comments': comments,
              'new_comment': new_comment,
              'comment_form': comment_form
            }
    return render(request,'blog/p_detail.html',context)



#lista risposte ad un post
class RispostePostView(LoginRequiredMixin, ListView):
    model = BlogCommentModel  # modello dei dati da utilizzare
    template_name = "blog/lista_commenti.html"  # pagina per mostrare i dati

    # recupera di dati da passare alla pagina per il render
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = BlogCommentModel.objects.all().order_by("-data_creazione")
        return context


class listaPostView(LoginRequiredMixin, ListView):
    model = BlogPostModel  # modello dei dati da utilizzare
    template_name = "blog/lista_post.html"  # pagina per mostrare i dati

    # recupera di dati da passare alla pagina per il render
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = BlogPostModel.objects.all().order_by("-data_creazione")
        return context
