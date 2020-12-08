from django.urls import path
from projects import views

app_name = "projects"
urlpatterns = [
	# path('', views.index, name='index'),
	path('', views.IndexView.as_view(), name='index'),
	path('projects', views.overview, name='overview'),
	path('projects/<int:pk>/', views.detail, name='detail')
]