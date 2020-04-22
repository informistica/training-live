from django.urls import path,reverse
from .views import registrazioneView

urlpatterns = [
    path('registrazione/', registrazioneView, name='registration_view')
]
