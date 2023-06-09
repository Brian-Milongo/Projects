

from django.shortcuts import render
from django.http import HttpRequest

posts=[
    {
        'author':'BrianMS',
        'content':'Content posted',
        'title': 'Testing learning',
        'date_posted':'August 28, 2018'
    },
{
        'author':'JamesMS',
        'content':'Second content posted',
        'title': 'Second testing learning',
        'date_posted':'August 29, 2018'
    },
]

def home(request):
    context={
        'posts':posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
