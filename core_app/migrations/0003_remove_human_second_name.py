# Generated by Django 2.1.2 on 2018-12-19 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0002_human_second_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='human',
            name='second_name',
        ),
    ]
