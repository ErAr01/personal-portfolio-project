from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects' : projects})

def blog(request):
    return render(request, 'personal_portfolio-project/blog/templates/blog/all_blogs.html')

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/project_detail.html', {'project':project})
