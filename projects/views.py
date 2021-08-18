from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return HttpResponse('Here are our projects.')


def project(request, pk):
    return HttpResponse('Here is a single project no ' + str(pk))