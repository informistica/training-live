from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Profile
from utenti.forms import FormRegistrazione, UserChangeForm
from blog.views import listaPostView
from blog.models import BlogPostModel, BlogCommentModel
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.db.models import Count, Sum
from django.http import JsonResponse
from django.urls import reverse_lazy


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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['object_list'] = User.objects.annotate(tot_punti=Sum('comment__punti')).order_by("-tot_punti")
        return context


@login_required(login_url='/accounts/login/')
def userProfileView(request, username):
    user = get_object_or_404(User, username=username)
    post_utente = BlogPostModel.objects.filter(autore=user).order_by("-pk")
    commenti_utente = BlogCommentModel.objects.filter(autore=user).order_by("-pk")
    punti_utente = BlogCommentModel.objects.filter(autore=user).aggregate(Sum('punti'))
    context = {"user": user, "post_utente": post_utente, "commenti_utente": commenti_utente,
               "punti_utente": punti_utente}
    return render(request, 'utenti/profilo.html', context)


@login_required(login_url='/accounts/login/')
def userProfileModifyView(request, username):
    profile = get_object_or_404(Profile, user=request.user)
    profile_form = UserChangeForm(request.POST or None, instance=profile)

    if request.method == 'POST':
        if profile_form.is_valid():
            profile_form.save()
            print("Salvato profilo")
            return redirect('user_profile', request.user)

    context = {'profile_form': profile_form}
    return render(request, 'utenti/profilo_modifica.html', context)


"""
def PostDetailView2(request, pk):
    post = get_object_or_404(BlogPostModel, id=pk)
    # Lista di commenti attivi per questo post
    comments = post.comments.filter(attivo=True)
    num_comments = post.comments.count() + 1
    response_data = {}
    if request.POST.get('action') == 'post':
        description = request.POST.get('description')
        response_data['description'] = description
        response_data['autore'] = request.user.get_username()
        response_data['num_comments'] = num_comments
        myDate = datetime.datetime.now()
        #response_data['data_creazione'] = myDate
        format_date = myDate.strftime("%A %d %B %Y %H:%M")
        response_data['data_creazione'] = format_date

        BlogCommentModel.objects.create(
            contenuto=description,
            autore=request.user,
            post=post,
        )
        return JsonResponse(response_data)
    else:
        # preparo il form vuoto in cui scrivere il commento
        comment_form = BlogCommentModelForm()

    context = {'post': post,
               'comments': comments,
               'comment_form': comment_form
               }

    return render(request, 'blog/post_detail.html', context)
"""
