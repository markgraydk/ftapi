# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0005_auto_20141001_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktor',
            name='aktorid',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='aktor',
            name='biografi',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='aktor',
            name='efternavn',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='aktor',
            name='fornavn',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='aktor',
            name='gruppenavnkort',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='aktor',
            name='navn',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='aktor',
            name='periodeid',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='aktor',
            name='typeid',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
