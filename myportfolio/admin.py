from django.contrib import admin
from .models import Tag, Tool, Project

# Register your models here.
admin.site.register(Tag)
admin.site.register(Tool)
admin.site.register(Project)