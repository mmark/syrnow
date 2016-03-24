# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syracuse_for_sanders', '0002_volunteer_replied_to_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='replied_to_by',
            new_name='contacted_by',
        ),
    ]
