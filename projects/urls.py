from django.urls import path
from projects import views

urlpatterns = [
	path('', views.index, name='index'),
	path('projects', views.overview, name='overview'),
	path('projects/<int:pk>/', views.detail, name='detail')
]