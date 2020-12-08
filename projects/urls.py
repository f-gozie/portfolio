from django.urls import path
from projects import views

app_name = "projects"
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('resume', views.ResumeView.as_view(), name='resume'),
	path('projects', views.overview, name='overview'),
	path('projects/<int:pk>/', views.detail, name='detail')
]