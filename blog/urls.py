from django.urls import path
from .views import listaPostView, modificaPostView, eliminaPostView, PostDetailView2, modificaCommentView,eliminaCommentView
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('crea-post', views.creaPostView, name='crea_post'),
    path('lista-post', listaPostView.as_view(), name='lista_post'),
    path('leggi-post/<int:pk>', PostDetailView2, name='leggi_post'),
    path('modifica-post/<int:pk>', modificaPostView, name='modifica_post'),
    path('elimina-post/<int:pk>', eliminaPostView, name='elimina_post'),
    path('modifica-comment/<int:pk_comment>/<int:pk_post>', modificaCommentView, name='modifica_comment'),
    path('elimina-comment/<int:pk>', eliminaCommentView, name='elimina_comment'),


]
