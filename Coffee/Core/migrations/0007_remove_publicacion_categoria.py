# Generated by Django 5.1.3 on 2024-12-20 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0006_remove_categoria_descripcion_alter_categoria_nombre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='categoria',
        ),
    ]
