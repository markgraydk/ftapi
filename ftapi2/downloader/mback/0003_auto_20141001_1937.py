# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0002_auto_20141001_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktor',
            name='opdateringsdato',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='aktor',
            name='slutdato',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='aktor',
            name='startdato',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
