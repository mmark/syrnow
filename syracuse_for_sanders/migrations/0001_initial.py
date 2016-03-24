# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormRecipients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default='Syracuse for Sanders Volunteer Profile', max_length=50, choices=[('Syracuse for Sanders Volunteer Profile', 'Syracuse for Sanders Volunteer Profile')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'form_recipients',
                'verbose_name_plural': 'Form Recipients',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator("^[A-Za-z0-9\\(\\)\\/\\-@_&#:,\\.\\?!\\s\\']*$", 'Only letters, numbers, spaces and &#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63; are allowed here.')])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator("^[A-Za-z0-9\\(\\)\\/\\-@_&#:,\\.\\?!\\s\\']*$", 'Only letters, numbers, spaces and &#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63; are allowed here.')])),
                ('primary_contact_phone_number', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator("^[A-Za-z0-9\\(\\)\\/\\-@_&#:,\\.\\?!\\s\\']*$", 'Only letters, numbers, spaces and &#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63; are allowed here.')])),
                ('hours_days_ok_to_contact_on_this_number', models.TextField(blank=True, null=True, validators=[django.core.validators.RegexValidator("^[A-Za-z0-9\\(\\)\\/\\-@_&#:,\\.\\?!\\s\\']*$", 'Only letters, numbers, spaces and &#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63; are allowed here.')])),
                ('any_alternate_numbers', models.TextField(blank=True, null=True, validators=[django.core.validators.RegexValidator("^[A-Za-z0-9\\(\\)\\/\\-@_&#:,\\.\\?!\\s\\']*$", 'Only letters, numbers, spaces and &#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63; are allowed here.')])),
                ('street_address', models.CharField(max_length=255, null=True, blank=True)),
                ('suite_or_apartment_number', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=255, null=True, blank=True)),
                ('state', models.CharField(max_length=2, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=10)),
                ('hours_days_ok_to_volunteer', models.TextField(blank=True, null=True, validators=[django.core.validators.RegexValidator("^[A-Za-z0-9\\(\\)\\/\\-@_&#:,\\.\\?!\\s\\']*$", 'Only letters, numbers, spaces and &#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63; are allowed here.')])),
                ('how_much_time_can_volunteer', models.TextField(blank=True, null=True, validators=[django.core.validators.RegexValidator("^[A-Za-z0-9\\(\\)\\/\\-@_&#:,\\.\\?!\\s\\']*$", 'Only letters, numbers, spaces and &#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63; are allowed here.')])),
                ('most_interested_in_volunteering_to_do', models.TextField(blank=True, null=True, validators=[django.core.validators.RegexValidator("^[A-Za-z0-9\\(\\)\\/\\-@_&#:,\\.\\?!\\s\\']*$", 'Only letters, numbers, spaces and &#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63; are allowed here.')])),
                ('email', models.EmailField(blank=True, max_length=254, null=True, validators=[django.core.validators.EmailValidator()])),
                ('facebook_name', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator("^[A-Za-z0-9\\(\\)\\/\\-@_&#:,\\.\\?!\\s\\']*$", 'Only letters, numbers, spaces and &#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63; are allowed here.')])),
                ('twitter_handle', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator("^[A-Za-z0-9\\(\\)\\/\\-@_&#:,\\.\\?!\\s\\']*$", 'Only letters, numbers, spaces and &#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63; are allowed here.')])),
                ('other_social_media', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator("^[A-Za-z0-9\\(\\)\\/\\-@_&#:,\\.\\?!\\s\\']*$", 'Only letters, numbers, spaces and &#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63; are allowed here.')])),
                ('member_of_syracuse_for_sanders_facebook', models.BooleanField(default=False)),
                ('where_do_you_work', models.CharField(max_length=100, null=True, blank=True)),
                ('what_skills_do_you_bring', models.TextField(null=True, blank=True)),
                ('member_of_any_community_groups', models.CharField(max_length=500, null=True, blank=True)),
                ('has_been_contacted', models.BooleanField(default=False)),
                ('submitted_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['zip_code', 'last_name', 'first_name'],
                'db_table': 'volunteers',
                'verbose_name_plural': 'Volunteers',
            },
        ),
    ]
