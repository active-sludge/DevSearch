from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    all_projects = Project.objects.all()
    context = {'projects': all_projects}
    return render(request, 'projects/projects.html', context=context)


def project(request, pk):
    projectObject = Project.objects.get(id=pk)
    tags = projectObject.tags.all()
    return render(request, 'projects/single-project.html', {'project': projectObject, 'tags': tags})


def create_project(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)
