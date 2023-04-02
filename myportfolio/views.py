from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all().order_by('rank')
    return render(request, "myportfolio/index.html", {
        "projects" : projects,
    })
