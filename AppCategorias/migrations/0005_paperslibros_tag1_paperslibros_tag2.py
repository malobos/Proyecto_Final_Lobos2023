# Generated by Django 4.1.5 on 2023-02-18 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCategorias', '0004_noticias_tag1_noticias_tag2'),
    ]

    operations = [
        migrations.AddField(
            model_name='paperslibros',
            name='tag1',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='paperslibros',
            name='tag2',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]