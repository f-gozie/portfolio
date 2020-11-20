from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
	return render(request, "portfolio/index.html")

def overview(request):
	projects = Project.objects.all()
	context = {
		'projects':projects
	}
	return render(request, "portfolio/overview.html", context)

def detail(request, pk):
	project = Project.objects.get(pk=pk)
	context = {
		'project':project
	}
	return render(request, "portfolio/detail.html", context)