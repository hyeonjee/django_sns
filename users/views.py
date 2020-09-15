from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from posts.models import *

# Create your views here.

@login_required
def follow_toggle(request, id):      
    user = request.user   
    followed_user = get_object_or_404(User, pk = id)
    is_follower = user.profile in followed_user.profile.followers.all()
    
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
        print('팔로우 취소')
    else:
        user.profile.followings.add(followed_user.profile)
        print('팔로우')
    return redirect('home')


def profile(request, id):
    context = {
        'user':  get_object_or_404(User, pk = id),
        'posts': Post.objects.all(),
    }
    return render(request, 'users/profile.html',context)

