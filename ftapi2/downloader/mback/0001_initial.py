# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aktor',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('typeid', models.IntegerField()),
                ('gruppenavnkort', models.CharField(max_length=200)),
                ('navn', models.CharField(max_length=200)),
                ('fornavn', models.CharField(max_length=200)),
                ('efternavn', models.CharField(max_length=200)),
                ('biografi', models.CharField(max_length=200)),
                ('opdateringsdato', models.DateTimeField()),
                ('periodeid', models.IntegerField()),
                ('startdato', models.DateTimeField()),
                ('slutdato', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='aktoraktor',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('ifraaktorid', models.IntegerField()),
                ('tilaktorid', models.IntegerField()),
                ('startdato', models.DateTimeField()),
                ('slutdato', models.DateTimeField()),
                ('rolleid', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='aktoraktorrolle',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('rolle', models.CharField(max_length=200)),
                ('opdateringsdato', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='aktortype',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=200)),
                ('opdateringsdato', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
