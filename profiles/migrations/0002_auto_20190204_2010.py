# Generated by Django 2.1.3 on 2019-02-04 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='user/%d%m%y'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telephone',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]
