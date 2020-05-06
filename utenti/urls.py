from django.urls import path,reverse
from .views import registrazioneView,userProfileView,UserList
urlpatterns = [
    path('registrazione', registrazioneView, name='registration_view'),
    path('users/', UserList.as_view(), name="users_list"),
    path('user/<username>/', userProfileView, name="user_profile"),
]
 