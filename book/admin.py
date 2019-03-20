from django.contrib import admin
from .models import Author, Book, Genre

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','second_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'genre')

admin.site.register(Genre)
