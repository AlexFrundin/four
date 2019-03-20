# Generated by Django 2.1.2 on 2018-12-19 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20181219_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена')),
                ('short_descript', models.CharField(max_length=120, verbose_name='О товаре')),
                ('full_descript', models.TextField(verbose_name='Описание')),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.SubCatalog')),
            ],
        ),
    ]
