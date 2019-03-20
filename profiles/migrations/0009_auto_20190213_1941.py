# Generated by Django 2.1.3 on 2019-02-13 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20190206_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='profiles.City'),
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='profiles.Country'),
        ),
        migrations.AlterField(
            model_name='country',
            name='country',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]