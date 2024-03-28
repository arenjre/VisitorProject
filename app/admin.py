from django.contrib import admin
from .models import Worker, Unit, Visit

# Register your models here.


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    search_fields = ['name']

class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'worker')
    search_fields = ['name']

class VisitAdmin(admin.ModelAdmin):
    list_display = ('unit', 'datetime')
    search_fields = ['unit__worker__name', 'unit__name']

admin.site.register(Worker, WorkerAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Visit, VisitAdmin)
