# Generated by Django 2.1.3 on 2019-03-04 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_testuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='short_description',
            field=models.CharField(default='', max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='language',
            name='lang',
            field=models.CharField(max_length=15),
        ),
    ]