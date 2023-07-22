from django.shortcuts import render
from . models import Main_model

def index(request):
    data = {
        'blogs': Main_model.objects.all()
    }
    return render(request, 'blog/index.html', data)

def about(request):
    return render(request, 'blog/about.html')

def communication(request):
    return render(request, 'blog/communication.html')

def blog_details(request, slug):
    data = {
        'blogs': Main_model.objects.get(slug=slug)
    }
    return render(request, 'blog/blog_details.html', data)

