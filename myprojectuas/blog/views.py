from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import post

def index(request):
    #query
    posts = post.objects.all()
    context = {
        'title':'',
        'heading':'',
        'Posts':posts,
    }

    return render(request,'blog/index.html',context)