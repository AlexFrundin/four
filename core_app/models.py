from django.db import models

class Human(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    info = models.TextField()
    second_name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
