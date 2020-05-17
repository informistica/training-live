from django.urls import path,reverse
from .views import registrazioneView,userProfileView,UserList,userProfileModifyView
urlpatterns = [
    path('registrazione', registrazioneView, name='registration_view'),
    path('users/', UserList.as_view(), name="users_list"),
    path('user/<username>/', userProfileView, name="user_profile"),
    path('user/<username>/modify', userProfileModifyView, name="user_profile_modify"),
]
 