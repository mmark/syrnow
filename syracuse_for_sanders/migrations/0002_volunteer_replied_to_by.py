# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('syracuse_for_sanders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='replied_to_by',
            field=models.ForeignKey(related_name='replied_to_by_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
