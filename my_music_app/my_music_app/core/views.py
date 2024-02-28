from django.shortcuts import redirect, render

from my_music_app.albums.models import Album
from my_music_app.core.forms import CreateProfileForm
from my_music_app.common.profile_helpers import get_profile
from my_music_app.profiles.models import Profile



def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')
    
    context = {
        'form': form,
        'no_nav': True,
    }
    
    return render(request, 'core/home-no-profile.html', context)
        

def index(request):
    profile = get_profile()
    
    if profile is None:
        return create_profile(request)
    
    context = {
        'albums': Album.objects.all(),
    }
    
    return render(request, 'core/home-with-profile.html', context)
