# Generated by Django 3.2.5 on 2021-07-26 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210725_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarcodeScanHit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestemp', models.DateTimeField(auto_now_add=True)),
                ('barcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cachebarcode')),
            ],
        ),
    ]