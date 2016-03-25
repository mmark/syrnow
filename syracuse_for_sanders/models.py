from __future__ import unicode_literals

import datetime

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, validate_email
from django.db import models


ALPHANUM_PATTERN = r'^[A-Za-z0-9\(\)\/\-@_&#:,\.\?!\s\']*$'
ALPHA_VALIDATOR = RegexValidator(
    ALPHANUM_PATTERN,
    'Only letters, numbers, spaces and '
    '&#40;&#41;&#64;&#47;&#45;&#95;&#38;&#35;&#58;&#44;&#46;&#33;&#63;'
    ' are allowed here.')
ZIP_PATTERN = r'^\d{5}(?:[-\s]\d{4})?$'
ZIP_VALIDATOR = RegexValidator(
    ZIP_PATTERN,
    'Zip codes require 5 numbers to be valid, but can be followed by an '
    'optional dash and plus four'
)


def is_born(birth_date):
    """Used to validate a birthday is actually not a day in the future and also
    not a day over 200 years ago.  IE: is this a plausible real birth date?
    :param birth_date: DateField value like: YYYY-MM-DD"""
    now = datetime.date.today()

    if birth_date >= now:

        raise ValidationError(u'%s' % 'Birth date indicates you are not yet '
                                      'born, please correct.')

    # If they are more than 200 years old lets assume that's an error also
    if birth_date < (now + datetime.timedelta(days=-73000)):

        raise ValidationError(u'%s' % 'Birth date indicates you are over 200 ')


class VolunteerEmails(models.Model):
    recipient_list = models.TextField()
    from_address = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_time = models.DateTimeField(auto_now_add=True,
                                     blank=True,
                                     editable=False)
    sent_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                blank=True,
                                null=True,
                                related_name="emails_sent")
    results = models.TextField(blank=True,
                               null=True)

    class Meta:
        db_table = 'volunteer_emails_sent'
        verbose_name_plural = 'Volunteer Emails Sent'
        ordering = ['sent_time', 'subject']

    def __unicode__(self):

        return u'%s, %s' % (self.first_name, self.last_name)


class FormRecipients(models.Model):
    S4S_Volunteer_Profile = 'Syracuse for Sanders Volunteer Profile'
    FORM_CHOICES = (
        (S4S_Volunteer_Profile, 'Syracuse for Sanders Volunteer Profile'),
    )
    type = models.CharField(max_length=50,
                            choices=FORM_CHOICES,
                            default=S4S_Volunteer_Profile)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        db_table = 'form_recipients'
        verbose_name_plural = 'Form Recipients'

    def __unicode__(self):

        return u'%s - %s' % (self.type, self.user.email)

    def user_email(self):

        return self.user.email


class Volunteer(models.Model):
    first_name = models.CharField(max_length=50,
                                  blank=False,
                                  null=False,
                                  validators=[ALPHA_VALIDATOR])
    last_name = models.CharField(max_length=50,
                                 blank=False,
                                 null=False,
                                 validators=[ALPHA_VALIDATOR])
    primary_contact_phone_number = models.CharField(max_length=50,
                                                    blank=True,
                                                    null=True,
                                                    validators=[ALPHA_VALIDATOR])
    hours_days_ok_to_contact_on_this_number = models.TextField(blank=True,
                                                               null=True,
                                                               validators=[ALPHA_VALIDATOR])
    any_alternate_numbers = models.TextField(blank=True,
                                             null=True,
                                             validators=[ALPHA_VALIDATOR])
    street_address = models.CharField(max_length=255,
                                      blank=True,
                                      null=True)
    suite_or_apartment_number = models.CharField(max_length=100,
                                                 blank=True,
                                                 null=True)
    city = models.CharField(max_length=255,
                            blank=True,
                            null=True)
    state = models.CharField(max_length=2,
                             blank=True,
                             null=True)
    zip_code = models.CharField(max_length=10,
                                blank=True,
                                null=True)
    hours_days_ok_to_volunteer = models.TextField(blank=True,
                                                  null=True,
                                                  validators=[ALPHA_VALIDATOR])
    most_interested_in_volunteering_to_do = models.TextField(blank=True,
                                                             null=True,
                                                             validators=[ALPHA_VALIDATOR])
    email = models.EmailField(max_length=254,
                              validators=[validate_email],
                              blank=True,
                              null=True)
    facebook_name = models.CharField(max_length=100,
                                     blank=True,
                                     null=True,
                                     validators=[ALPHA_VALIDATOR])
    twitter_handle = models.CharField(max_length=100,
                                      blank=True,
                                      null=True,
                                      validators=[ALPHA_VALIDATOR])
    other_social_media = models.CharField(max_length=100,
                                          blank=True,
                                          null=True,
                                          validators=[ALPHA_VALIDATOR])
    member_of_syracuse_for_sanders_facebook = models.BooleanField(default=False)
    where_do_you_work = models.CharField(max_length=100,
                                         blank=True,
                                         null=True)
    what_skills_do_you_bring = models.TextField(blank=True,
                                                null=True)
    member_of_any_community_groups = models.CharField(max_length=500,
                                                      blank=True,
                                                      null=True)
    willing_to_volunteer_for_bernie_friendly_candidates = models.BooleanField(default=False)
    submitted_time = models.DateTimeField(auto_now_add=True,
                                          blank=True,
                                          editable=False)
    has_been_contacted = models.BooleanField(blank=False,
                                             null=False,
                                             default=False,
                                             editable=True)
    contacted_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     blank=True,
                                     null=True,
                                     related_name="replied_to_by_user")

    class Meta:
        db_table = 'volunteers'
        verbose_name_plural = 'Volunteers'
        ordering = ['zip_code', 'last_name', 'first_name']

    def __unicode__(self):

        return u'%s, %s' % (self.first_name, self.last_name)
