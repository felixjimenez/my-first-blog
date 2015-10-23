# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151018_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='cedula',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='email',
            field=models.EmailField(max_length=254, default='a@a.com'),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='fecha',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
