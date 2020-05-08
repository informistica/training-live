from django.urls import path
from .views import listaPostView ,PostDetailView,modificaPostView,eliminaPostView,DiscussionePostView
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('crea-post', views.creaPostView, name='crea_post'),
    path('lista-post', listaPostView.as_view(), name='lista_post'),
    path('leggi-post/<int:pk>', PostDetailView.as_view(), name='leggi_post'),
    path('modifica-post/<int:pk>', modificaPostView, name='modifica_post'),
    path('elimina-post/<int:pk>', eliminaPostView, name='elimina_post'),
    path('discussione-post/<int:pk>', DiscussionePostView, name='discussione_post'),


       
]