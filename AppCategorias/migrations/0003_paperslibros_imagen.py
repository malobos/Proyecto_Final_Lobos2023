# Generated by Django 4.1.5 on 2023-02-18 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCategorias', '0002_alter_noticias_titulo_alter_paperslibros_reseña'),
    ]

    operations = [
        migrations.AddField(
            model_name='paperslibros',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='papers'),
        ),
    ]
