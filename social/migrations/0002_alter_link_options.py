# Generated by Django 4.1.5 on 2023-01-30 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("social", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="link",
            options={
                "ordering": ["-name"],
                "verbose_name": "Enlace",
                "verbose_name_plural": "Enlaces",
            },
        ),
    ]
