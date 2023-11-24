from django.contrib import admin
from .models import SectionPorfolio

# Register your models here.
@admin.register(SectionPorfolio)
class SectionPorfolioAdmin(admin.ModelAdmin):
    list_display = ["section_name","visible","created","updated"]

    # ACTIONS BUTTONS
    def disable_section(self, request, queryset):
        queryset.update(visible=False)    
    disable_section.short_description = 'Section disable'

    def enable_section(self, request, queryset):
        queryset.update(visible=True)
    enable_section.short_description = 'Section enable'

    # Agregamos las acciones
    actions = [enable_section,disable_section]