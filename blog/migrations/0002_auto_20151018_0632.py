# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=8)),
                ('direccion', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(default='Informatica', max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('alumno', models.ForeignKey(to='blog.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(default='IUTIRLA', max_length=18)),
                ('sede', models.CharField(default='Chaguaramos', max_length=18)),
                ('rif', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('carrera', models.ForeignKey(to='blog.Carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('fechaevalua', models.DateTimeField(default=django.utils.timezone.now)),
                ('nota', models.IntegerField(default=0)),
                ('inscripcion', models.ForeignKey(to='blog.Inscripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('seccion', models.CharField(max_length=10)),
                ('aula', models.ForeignKey(to='blog.Aula')),
                ('materia', models.ForeignKey(to='blog.Materia')),
            ],
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='seccion',
            field=models.ForeignKey(to='blog.Seccion'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='institucion',
            field=models.ForeignKey(to='blog.Institucion'),
        ),
    ]
