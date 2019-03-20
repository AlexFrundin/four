from django.contrib import admin
from .models import Language, TestUser


@admin.register(Language)
class LangAdmin(admin.ModelAdmin):
    fields = ('lang','short_description')
    list_display = ('lang',)

@admin.register(TestUser)
class TestUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'all_language')
