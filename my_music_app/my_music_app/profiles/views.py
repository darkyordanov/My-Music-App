from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from my_music_app.common.profile_helpers import get_profile
from my_music_app.profiles.models import Profile


class ProfileDetailsView(DetailView):
    template_name = 'profiles/profile-details.html'
    
    def get_object(self, queryset=None):
        return get_profile() 
    

class ProfileDeleteView(DeleteView):
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index')
    
    def get_object(self, queryset=None):
        return get_profile() 
    