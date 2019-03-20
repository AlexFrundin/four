from django.db import models
from django.utils.safestring import mark_safe



class Catalog(models.Model):
    name = models.CharField(verbose_name="Название", max_length=25, unique=True)
    position = models.PositiveSmallIntegerField(verbose_name="Позиция")

    def __str__(self):
        return self.name

class SubCatalog(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.PROTECT)
    name = models.CharField(verbose_name = "Название", max_length=25, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    sub = models.ForeignKey(SubCatalog, on_delete=models.CASCADE)
    name = models.CharField(verbose_name = "Название", max_length=25,)
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=5)
    short_descript = models.CharField(verbose_name="О товаре", max_length=120,)
    full_descript = models.TextField(verbose_name="Описание")
    foto = models.ImageField(verbose_name="Картинка", upload_to = "product/", blank=True)

    def image_prev(self):
        return mark_safe(f'<img width="30" height="30" src="{self.foto.url}" alt="">')

    image_prev.short_description = "Картинка"

    def __str__(self):
        return self.name

class Edit(models.Model):
    quantity = models.IntegerField()
    list_name = models.TextField()
    category_name = models.CharField(max_length=60)
