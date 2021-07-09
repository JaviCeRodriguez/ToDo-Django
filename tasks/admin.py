from django.contrib import admin

from .models import Task, TaskState


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'completed')
    search_fields = ['name', 'state__state'] # Acá pongo state solo para demostrar las relaciones con __


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskState)