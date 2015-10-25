# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20151025_0436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='foto',
        ),
    ]
