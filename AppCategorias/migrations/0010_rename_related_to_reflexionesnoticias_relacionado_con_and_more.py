# Generated by Django 4.1.5 on 2023-02-19 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCategorias', '0009_delete_reflexionespapers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reflexionesnoticias',
            old_name='related_to',
            new_name='relacionado_con',
        ),
        migrations.AlterField(
            model_name='paperslibros',
            name='editorial',
            field=models.CharField(max_length=100),
        ),
    ]
