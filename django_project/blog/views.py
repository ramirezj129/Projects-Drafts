from django.shortcuts import render
from django.http import HttpResponse
from . models import Post

posts = [

    {
        "author": "Javier Ramirez",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "august 27, 2049"

    },
        {
        "author": "James Ramirez",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "august 22, 2039"

    }

]

# Create your views here.
def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")
