from django.shortcuts import render
from .models import Post

def home(request):

    context = {
        'posts': Post.objects.all(),
        'title': 'Home page'
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    context = {
        'title': 'About page'
    }
    return render(request, 'blog/about.html', context=context)
