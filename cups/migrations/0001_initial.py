# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lister_name', models.CharField(max_length=50)),
                ('topic', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2014, 11, 22, 6, 4, 8, 889000, tzinfo=utc), verbose_name=b'Time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=50)),
                ('location_lon', models.FloatField(default=0)),
                ('location_lat', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cup',
            name='location',
            field=models.ForeignKey(to='cups.Location'),
            preserve_default=True,
        ),
    ]
