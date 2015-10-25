# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151021_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='observacion',
            field=models.CharField(default='no asistio', max_length=50),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='apellido',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='aula',
            name='direccion',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='nombre',
            field=models.CharField(default='Informatica', max_length=25),
        ),
        migrations.AlterField(
            model_name='materia',
            name='nombre',
            field=models.CharField(max_length=25),
        ),
    ]
