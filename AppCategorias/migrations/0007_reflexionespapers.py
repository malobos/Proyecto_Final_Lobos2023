# Generated by Django 4.1.5 on 2023-02-19 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCategorias', '0006_reflexionesnoticias'),
    ]

    operations = [
        migrations.CreateModel(
            name='reflexionesPapers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('contenido', models.TextField(max_length=2000)),
                ('fechaDeSubida', models.DateTimeField(auto_now_add=True)),
                ('related_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCategorias.paperslibros')),
            ],
        ),
    ]
