from django.contrib import admin
from .models import Project, Contact

class ContactAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'message']

# Register your models here.
admin.site.register(Project)
admin.site.register(Contact, ContactAdmin)