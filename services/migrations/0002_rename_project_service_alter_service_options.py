# Generated by Django 4.1.5 on 2023-01-29 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='Service',
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
    ]