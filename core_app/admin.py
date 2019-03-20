from django.contrib import admin
from .models import Human

@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    # fields = ['name', 'age']
    list_display = ('name', 'age', 'info')
    list_filter = ('age', 'name')
    list_editable = ('name',)
    list_display_links = ('age',)
    search_fields = ('name',)
    
