import os

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.views import View
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse,Http404, JsonResponse
from django.core.mail import send_mail

from .models import Project
from .forms import ContactForm

class IndexView(TemplateView):
	template_name = "portfolio/index.html"

class ResumeView(View):

	# GET request
	def get(self, request):
		resume_path = settings.MEDIA_ROOT + '/documents/Agozie Favour Resume.pdf'
		if os.path.exists(resume_path):
			with open(resume_path, 'rb') as resume:
				response = HttpResponse(resume.read(), 'application/pdf')
				response['Content-Disposition'] = 'filename=Agozie Favour Resume.pdf'
				return response
		raise Http404

class ContactMeView(FormView):
	form_class = ContactForm

	def form_valid(self, form):
		message = form.cleaned_data.get('message')
		to_email = form.cleaned_data.get('email')
		form.save()
		send_mail("Contact Me Form", message, 'no-reply@mg.agoziefavour.tech', [to_email])
		return redirect('portfolio:index')
		# send_response = send_mail("Contact Me Form", message, 'no-reply@mg.agoziefavour.tech', [to_email])
		# if send_response:
		# 	return JsonResponse({'success': True, 'message':'Thank you for reaching out. I will send you an email soon'})
		# else:
		# 	return JsonResponse({'success': False, 'message':'Email could not be sent. Is the specified email address correct?'})

	def form_invalid(self, form):
		return JsonResponse({'success': False, 'errors':form.errors})


# def overview(request):
# 	projects = Project.objects.all()
# 	context = {
# 		'projects':projects
# 	}
# 	return render(request, "portfolio/overview.html", context)

# def detail(request, pk):
# 	project = Project.objects.get(pk=pk)
# 	context = {
# 		'project':project
# 	}
# 	return render(request, "portfolio/detail.html", context)