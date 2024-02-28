from django.urls import path

from my_music_app.core.views import create_profile, index

urlpatterns = (
    path('', index, name='index'),
    path('create-profile/', create_profile, name='create_profile'),
)