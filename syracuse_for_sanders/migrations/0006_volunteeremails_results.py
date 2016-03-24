# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syracuse_for_sanders', '0005_auto_20160321_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteeremails',
            name='results',
            field=models.TextField(null=True, blank=True),
        ),
    ]
