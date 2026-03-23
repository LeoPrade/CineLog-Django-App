from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import UserProfile
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'GET': 
        return render(request, 'registration/register.html', {'form': RegisterForm()})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data.get('email')
            user.save()
            login(request, user)
        else:
            return render(request, 'registration/register.html', {'form': form})

        return redirect('movie_list')

@login_required
def profile(request):
    if request.method == 'GET': 
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        return render(request, 'users/profile.html', {'profile': profile})

    if request.method == 'POST':
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.bio = request.POST.get('bio')
        profile.favorite_genre = request.POST.get('genre')
        profile.favorite_movie = request.POST.get('favorite_movie')
        profile.favorite_actor = request.POST.get('favorite_actor')
        profile.favorite_director = request.POST.get('favorite_director')
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']
        profile.save()
        return redirect('profile')