# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cup',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 22, 9, 37, 42, 816000, tzinfo=utc), verbose_name=b'Time'),
            preserve_default=True,
        ),
    ]
