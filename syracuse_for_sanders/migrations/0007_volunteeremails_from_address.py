# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('syracuse_for_sanders', '0006_volunteeremails_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteeremails',
            name='from_address',
            field=models.CharField(default=datetime.datetime(2016, 3, 23, 19, 30, 32, 948838, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
