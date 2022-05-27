from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects' : projects})

def blog(request):
    return render(request, 'personal_portfolio-project/blog/templates/blog/all_blogs.html')
