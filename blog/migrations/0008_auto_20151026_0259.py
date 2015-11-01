# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_alumno_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='direccion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='nombre',
            field=models.CharField(default='Tecnico Superior en Informatica', max_length=35),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='sede',
            field=models.CharField(default='CC Chaguaramos', max_length=18),
        ),
    ]
