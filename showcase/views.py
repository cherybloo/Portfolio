from django.shortcuts import render
from .models import Project
# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request,"home.html",{'projects':list(projects)})

def project2(request):
    projects = Project.objects.all()
    return render(request,"project2.html",{'projects':list(projects)})

def project3(request):
    projects = Project.objects.all()
    return render(request,"project3.html",{'projects':list(projects)})
