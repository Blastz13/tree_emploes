from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Emploe, Subdivision, Position


@admin.register(Emploe)
class AdminEmploe(admin.ModelAdmin):
    list_display = ['name', 'subdivision', 'position', 'date_of_birth']
    list_display_links = ['name', 'subdivision', 'position', 'date_of_birth']
    search_fields = ['name', 'subdivision', 'position', 'date_of_birth']


@admin.register(Subdivision)
class AdminSubdivision(admin.ModelAdmin):
    list_display = ['title', 'supervisor']
    list_display_links = ['title', 'supervisor']
    search_fields = ['title', 'supervisor__name']


@admin.register(Position)
class AdminPosition(DraggableMPTTAdmin):
    pass
