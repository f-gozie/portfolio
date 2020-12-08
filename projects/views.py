import os

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.conf import settings
from django.http import HttpResponse,Http404

from .models import Project

class IndexView(TemplateView):
	template_name = "portfolio/index.html"

class ResumeView(View):

	# GET requests
	def get(self, request):
		resume_path = settings.MEDIA_ROOT + 'documents/Agozie Favour Resume.pdf'
		if os.path.exists(resume_path):
			with open(resume_path, 'rb') as resume:
				response = HttpResponse(resume.read(), 'application/pdf')
				response['Content-Disposition'] = 'filename=Agozie Favour Resume.pdf'

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