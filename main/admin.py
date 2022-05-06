from django.contrib import admin
from .models import Worker, Visit, Store


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']
    search_fields = ['name']


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['id', 'store', 'latitude', 'longitude']
    search_fields = ['store__worker__name', 'store__name']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
