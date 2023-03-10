# Generated by Django 4.1.5 on 2023-02-15 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('medio', models.CharField(max_length=40)),
                ('url', models.URLField(blank=True, null=True)),
                ('fechaDePublicacion', models.DateField(blank=True, null=True)),
                ('fechaDeSubida', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='papersLibros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor1', models.CharField(max_length=40)),
                ('autor2', models.CharField(blank=True, max_length=40, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('editorial', models.CharField(max_length=40)),
                ('reseña', models.TextField(max_length=240)),
                ('fechaDeSubida', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
