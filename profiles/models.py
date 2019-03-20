from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Country(models.Model):
    country = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.country

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, )
    def __str__(self):
        return f"{self.name}"
    class Meta:
        unique_together=('name','country')

class Language(models.Model):
    lang = models.CharField(max_length=15)
    short_description = models.CharField(max_length=6)


    def __str__(self):
        return self.lang

class TestUser(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    language = models.ManyToManyField('Language',)

    def __str__(self):
        return self.name

    def all_language(self):
        return self.language.all()

    # all_language.description = "Lang"

class Profile(models.Model):
    MALE = 1
    FEMALE = 0
    GENDER = (
        (MALE, "male"),
        (FEMALE, "female")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    birth = models.DateField(blank=True, null=True)
    gender = models.SmallIntegerField(choices=GENDER, blank=True, null=True)
    telephone = models.CharField(max_length=13, blank=True)
    image = models.ImageField(upload_to="user/%d%m%y", blank=True)

    def get_image(self):
        try:
            return self.image.url
        except:
            pass


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])

def content_file_name(instance, filename):
    name, ext = filename.split('.')
    file_path = '{account_id}/photos/user_{user_id}.{ext}'.format(
         account_id=instance.account_id, user_id=instance.id, ext=ext)
    return file_path
# @receiver(post_save, sender = User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
