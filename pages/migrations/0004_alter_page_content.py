# Generated by Django 4.1.5 on 2023-01-30 18:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_alter_page_options_page_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="content",
            field=ckeditor.fields.RichTextField(verbose_name="Contenido"),
        ),
    ]
