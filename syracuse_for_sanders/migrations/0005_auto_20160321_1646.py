# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syracuse_for_sanders', '0004_volunteeremails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteeremails',
            name='message',
            field=models.TextField(),
        ),
    ]
