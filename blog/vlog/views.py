from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse


def home(request):
    return render(request, 'vlog/home.html')


def about(request):
    return render(request, "vlog/about.html")