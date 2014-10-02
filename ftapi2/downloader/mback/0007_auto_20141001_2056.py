# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0006_auto_20141001_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktor',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
