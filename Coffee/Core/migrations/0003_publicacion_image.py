# Generated by Django 4.1 on 2024-11-12 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_categoria_remove_publicacion_image_comentario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
