# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151024_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='foto',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]
