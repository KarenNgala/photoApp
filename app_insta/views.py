from django.shortcuts import render
from .models import Image, Profile, Comment, Relation
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def feed(request):
    pictures = Image.objects.all()
    return render(request, 'index.html',{'pictures':pictures})

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile.html')