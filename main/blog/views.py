from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.

def index(request):
    blogs=Blogpost.objects.all();
    return render(request, 'blog/index.html', {"blogs":blogs})

#myid paramter gets it value from the URL in the urls.py file
def blogpost(request,bid):
    post= Blogpost.objects.filter(post_id=bid)[0]; #This returns a queryset of which we will select [0] object
    return render(request, 'blog/blogpost.html', {'post':post})