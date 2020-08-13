from django.shortcuts import render
from .models import Image, Profile, Comment, Relation

# Create your views here.
def feed(request):
    pictures = Image.objects.all()
    return render(request, 'index.html',{'pictures':pictures})

def profile(request):
    return render(request, 'profile.html')