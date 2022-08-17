import imp
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def index(request):
    return render(request, 'blog/index.html')