from django.shortcuts import render, redirect, get_object_or_404
from .models import Image, Profile, Comment, Relation
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import uploadForm, commentForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def feed(request):
    pictures = Image.objects.all()
    number = Comment.objects.count()
    return render(request, 'index.html',{'pictures':pictures, 'number':number})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user.profile
    pics = Image.objects.filter(profile=current_user).all()
    return render(request, 'profile.html', {'pics':pics})

def user(request, user_id):
    users = User.objects.filter(id=user_id)
    pics = Image.objects.filter(profile=user_id).all()    
    return render(request, 'user.html', {'pics':pics, 'users':users}) 

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user.profile
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('feed')
    else:
        form = uploadForm()
    return render(request, 'new_image.html', {'form':form})

@login_required(login_url='accounts/login')
def comments(request, id):
    current_user = request.user.profile
    post = Image.objects.filter(id=id)

    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.name = current_user
            comment.related_post = post
            comment.save()
        return redirect('comments')
    else:
        form = commentForm()

    maoni = Comment.objects.filter(related_post=id).all()
    return render(request, 'comments.html', {'maoni':maoni, 'form':form})


def like_post(request, post_id):
    current_user = request.user
    img = Image.objects.get(id=post_id)
    if img.likes.filter(id=current_user.id).exists():
        img.likes.remove(current_user)
    else:
        img.likes.add(current_user)
    return redirect('feed')