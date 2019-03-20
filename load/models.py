from django.db import models

class NewCountry(models.Model):
    id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=20)

    def __str__(self):
        return self.country_name

class NewCity(models.Model):
    country = models.ForeignKey('NewCountry', to_field='id', on_delete=models.CASCADE, related_name='country_city')
    city_name = models.CharField(max_length=20)
    class Meta:
        ordering = ('-city_name',)
    def __str__(self):
        return self.city_name
