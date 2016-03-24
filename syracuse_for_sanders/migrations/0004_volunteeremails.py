# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('syracuse_for_sanders', '0003_auto_20160321_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerEmails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recipient_list', models.TextField()),
                ('subject', models.CharField(max_length=200)),
                ('message', ckeditor_uploader.fields.RichTextUploadingField()),
                ('sent_time', models.DateTimeField(auto_now_add=True)),
                ('sent_by', models.ForeignKey(related_name='emails_sent', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['sent_time', 'subject'],
                'db_table': 'volunteer_emails_sent',
                'verbose_name_plural': 'Volunteer Emails Sent',
            },
        ),
    ]
