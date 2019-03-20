from django.contrib import admin
from .models import Catalog, SubCatalog, Product

admin.site.register(Catalog)
admin.site.register(SubCatalog)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_prev')
