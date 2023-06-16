from django.contrib import admin
from .models import Project, Technologie



# Register your models here.
@admin.register(Project) 
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "fecha_created_formateada","fecha_updated_formateada", "visible"]
    
    def fecha_created_formateada(self, obj):
        return obj.created.strftime('%d/%m/%Y %H:%M:%S')
    
    fecha_created_formateada.short_description = 'Creada'
    
    def fecha_updated_formateada(self, obj):
        return obj.updated.strftime('%d/%m/%Y %H:%M:%S')
    
    fecha_updated_formateada.short_description = 'Actualizada'
    
    # Actions
    def desactivar_Proyectos(self, request, queryset):
        queryset.update(visible=False)
        
    desactivar_Proyectos.short_description = 'Desactivar Proyectos'

    def activar_Proyectos(self, request, queryset):
        queryset.update(visible=True)
        
    activar_Proyectos.short_description = 'Activar Proyectos'
    
    # Agregamos las acciones
    actions = [activar_Proyectos,desactivar_Proyectos]
    
    
@admin.register(Technologie)
class TechonolgieAdmin(admin.ModelAdmin):
    list_display = ["name_Tech","fecha_created_formateada","fecha_updated_formateada"]

    def fecha_created_formateada(self, obj):
        return obj.created.strftime('%d/%m/%Y %H:%M:%S')
        
    fecha_created_formateada.short_description = 'Creada'

    
    def fecha_updated_formateada(self, obj):
        return obj.updated.strftime('%d/%m/%Y %H:%M:%S')
    
    fecha_updated_formateada.short_description = 'Actualizada'
    