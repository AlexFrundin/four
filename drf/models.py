from django.db import models
def save_image(self, filename):
    return '/'.join(['drf',self.name, filename])

class TestModel(models.Model):
    name = models.CharField(max_length=20)
    foto = models.ImageField(upload_to=save_image)
    def __str__(self):
        return self.name
    def get_foto_url(self):
        if self.foto:
            return self.foto.url
        else:
            return None
