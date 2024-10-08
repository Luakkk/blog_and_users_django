from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Profile, Follow
from django.contrib.auth.decorators import login_required

def user_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user)
        login(request, user)
        return redirect('post_list')
    return render(request, 'users/registration.html')

def user_profile(request, user_id):
    profile = get_object_or_404(Profile, user_id=user_id)
    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def follow_user(request, user_id):
    to_follow = get_object_or_404(User, pk=user_id)
    Follow.objects.get_or_create(follower=request.user, following=to_follow)
    return redirect('user_profile', user_id=user_id)

@login_required
def unfollow_user(request, user_id):
    to_unfollow = get_object_or_404(User, pk=user_id)
    Follow.objects.filter(follower=request.user, following=to_unfollow).delete()
    return redirect('user_profile', user_id=user_id)
