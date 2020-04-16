from django.urls import path
from . import views
app_name = 'esempi'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /esempi/if
    path('if', views.es_if, name='if'),
    # ex: /esempi/ifelse
    path('ifelse', views.es_ifelse, name='ifelse'),
    # ex: /esempi/for
    path('for', views.es_for, name='for'),
     # ex: /esempi/isequal
    path('ifequal', views.es_ifequal, name='ifequal'),
     # ex: /esempi/isequal
    path('ifnotequal', views.es_ifnotequal, name='ifnotequal'),
     # ex: /esempi/elif
    path('elif', views.es_elif, name='elif'),
    # ex: /esempi/filter
    path('filter', views.es_filter, name='filter'),
      # ex: /esempi/form
    path('form', views.es_form, name='form'),
]