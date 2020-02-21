from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

posts = [
    {
        'author': 'Dark Devil',
        'title': 'Blog-Post-1',
        'content': 'Hello world',
        'date': 'Date'
    },
    {
        'author': 'darkdevil',
        'title': 'vlog-post-1',
        'content': 'Hello world second time',
        'date': 'date2'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'vlog/home.html', context)


def about(request):
    return render(request, "vlog/about.html", {'title': 'About'})


def contact(request):
    return render(request, 'vlog/contact.html', {'title': 'Contact'})
