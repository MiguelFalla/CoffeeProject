# Generated by Django 5.1.3 on 2024-12-19 03:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_delete_contactmessage_remove_publicacion_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Core.categoria'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
    ]
