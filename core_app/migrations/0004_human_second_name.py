# Generated by Django 2.1.2 on 2018-12-19 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0003_remove_human_second_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='second_name',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
    ]
