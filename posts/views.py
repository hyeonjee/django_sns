from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pdb
from .forms import PostForm #이거 추가

# Create your views here.
@login_required
def create(request):
    # if request.method == "POST":
    #     title = request.POST.get("title")
    #     content = request.POST.get("content")
    #     image = request.FILES.get("image")
    #     user = request.user
    #     post = Post.objects.create(title=title, content=content, image=image, user=user)
    #     return redirect('home')
    # return render(request, 'posts/create.html')

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # pdb.set_trace()
            form.save(user = request.user)
            #save할 때 user를 같이 저장// 저장은 즉시저장 안되도록 처리한다. 즉시저장하면 user값 없이 저장될 수 있음
        return redirect('home')
    else: 
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})
    

@login_required
def update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.image = request.FILES.get("image")
        post.save()
        return redirect('home')
    return render(request, 'posts/update.html', {"post": post})
    

@login_required
def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('home')


@login_required
def create_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        user = request.user
        content = request.POST.get('content')
        Comment.objects.create(content=content, user=user, post=post)
    return redirect('home')


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('home')

@login_required
def post_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.user in post.like_user_set.all():
        post.like_user_set.remove(request.user)
    else:
        post.like_user_set.add(request.user)

    return redirect('home')

@login_required
def like_list(request):
    likes = request.user.like_user_set.all()
    return render(request, 'posts/like_list.html', {'likes': likes})

