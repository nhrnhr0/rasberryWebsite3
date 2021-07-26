# Generated by Django 3.2.5 on 2021-07-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cachebarcode',
            name='barcdoe',
        ),
        migrations.AddField(
            model_name='cachebarcode',
            name='barcode',
            field=models.CharField(default=1, max_length=120, unique=True),
            preserve_default=False,
        ),
    ]
