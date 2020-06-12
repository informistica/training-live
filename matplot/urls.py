from django.contrib import admin
from django.urls import path, include
from matplot import views

urlpatterns = [
    path('', views.home, name="home"),
    path('classi/<str:id_classe>/<int:periodo>', views.mostraclassi, name="mostra_classe"),
    path('gruppi/<str:id_classe>', views.mostragruppi, name="mostra_gruppi"),

]
