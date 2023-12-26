# Generated by Django 5.0 on 2023-12-26 02:58

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=50)),
                ('asunto', models.CharField(max_length=100)),
                ('mensaje', models.TextField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaAutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoria')),
            ],
            options={
                'ordering': ('categoria',),
            },
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('titulo', models.CharField(max_length=255, unique=True)),
                ('url', models.SlugField(max_length=255, unique=True)),
                ('resumen', ckeditor.fields.RichTextField()),
                ('contenido', ckeditor.fields.RichTextField()),
                ('vistas', models.PositiveIntegerField(default=0)),
                ('destacado', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=True)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('imagen', models.ImageField(upload_to='articulo/imagenes/')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.perfil')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('categoria_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoriaautor')),
            ],
            options={
                'ordering': ('creacion',),
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=5000)),
                ('visible', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.articulo')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.perfil')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
