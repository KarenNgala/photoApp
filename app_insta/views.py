from django.shortcuts import render

# Create your views here.
def feed(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')