from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Emploe, Subdivision, Position


@admin.register(Emploe)
class AdminEmploe(DraggableMPTTAdmin):
    pass


@admin.register(Subdivision)
class AdminSubdivision(admin.ModelAdmin):
    list_display = ['title', 'supervisor']
    list_display_links = ['title', 'supervisor']
    search_fields = ['title', 'supervisor__name']


@admin.register(Position)
class AdminPosition(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']
