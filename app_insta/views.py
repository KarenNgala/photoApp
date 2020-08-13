from django.shortcuts import render, redirect
from .models import Image, Profile, Comment, Relation
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import uploadForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def feed(request):
    pictures = Image.objects.all()
    return render(request, 'index.html',{'pictures':pictures})


@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile.html')
 

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user.profile
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('profile')
    else:
        form = uploadForm()
    return render(request, 'new_image.html', {'form':form})