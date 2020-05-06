from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from utenti.forms import FormRegistrazione
from blog.views import listaPostView
from blog.models import BlogPostModel
from django.shortcuts import get_object_or_404,  render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

# Create your views here.

def registrazioneView(request):
    if request.method == "POST":
        form = FormRegistrazione(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = FormRegistrazione()
    context = {"form": form}
    return render(request, 'utenti/registrazione.html', context)



class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'utenti/profili.html'

@login_required(login_url='/accounts/login/')
def userProfileView(request, username):
    user = get_object_or_404(User, username=username)
    posts_utente = BlogPostModel.objects.filter(autore=user).order_by("-pk")
    context = {"user": user, "posts_utente": posts_utente}
    return render(request, 'utenti/profilo.html', context)




