from __future__ import unicode_literals

from datetime import timedelta

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils import timezone
from django.utils.http import urlencode
from django.core.urlresolvers import reverse

from .models import *


class FormRecipientsAdmin(admin.ModelAdmin):
    model = FormRecipients
    fields = ['type', 'user']
    search_fields = ['type', 'user__email', 'user__first_name', 'user__last_name']
    ordering = ['type']

admin.site.register(FormRecipients, FormRecipientsAdmin)


class VolunteerEmailsAdmin(admin.ModelAdmin):
    model = VolunteerEmails
    fields = ['recipient_list', 'from_address', 'subject', 'message',
              'sent_time', 'sent_by', 'results']
    list_display = ['recipient_list', 'subject', 'sent_time', 'sent_by']
    list_display_links = ['recipient_list', 'subject', 'sent_time', 'sent_by']
    search_fields = ['recipient_list', 'from_address', 'subject',
                     'message', 'sent_time']
    ordering = ['sent_time', 'sent_by', 'subject']

admin.site.register(VolunteerEmails, VolunteerEmailsAdmin)


class VolunteerPeriodFilter(admin.SimpleListFilter):
    title = 'Filter By'
    parameter_name = 'submitted_on'

    def lookups(self, request, model_admin):

        return (
            ('NotContacted', 'Not Yet Contacted'),
            ('LastDay', 'Last Day'),
            ('LastSeven', 'Last 7 Days'),
            ('LastThirty', 'Last 30 days'),
            ('LastYear', 'Last Year'),
        )

    def queryset(self, request, queryset):
        today = timezone.now()
        yesterday = today + timedelta(-1)
        last_week = today + timedelta(-7)
        last_month = today + timedelta(-30)
        last_year = today + timedelta(-365)

        if self.value() == 'LastDay':
            return queryset.filter(submitted_time__gte=yesterday)
        if self.value() == 'LastSeven':
            return queryset.filter(submitted_time__gte=last_week)
        if self.value() == 'LastThirty':
            return queryset.filter(submitted_time__gte=last_month)
        if self.value() == 'LastYear':
            return queryset.filter(submitted_time__gte=last_year)
        if self.value() == 'NotContacted':
            return queryset.filter(has_been_contacted=False)


class VolunteerAdmin(admin.ModelAdmin):
    """
    Admin for volunteer form submissions
    """
    models = Volunteer
    list_filter = [VolunteerPeriodFilter]
    actions = ['email_selected_users']
    fieldsets = (
        ('Name / Address', {
            'fields': ['first_name',
                       'last_name',
                       'street_address',
                       'suite_or_apartment_number',
                       'city', 'state', 'zip_code']}),
        ('Contact Information', {
            'fields': ('primary_contact_phone_number',
                       'hours_days_ok_to_contact_on_this_number',
                       'any_alternate_numbers',
                       'email',)}),
        ('Social Media', {
            'fields': ('member_of_syracuse_for_sanders_facebook',
                       'facebook_name',
                       'twitter_handle',
                       'other_social_media')}),
        ('Volunteer Availability', {
           'fields': ('hours_days_ok_to_volunteer',
                      'how_much_time_can_volunteer',
                      'most_interested_in_volunteering_to_do')}),
        ('Skills and Groups', {
            'fields': ('where_do_you_work',
                       'what_skills_do_you_bring',
                       'member_of_any_community_groups')}),
        ('Staff Contact', {
            'fields': ('submitted_time',
                       'has_been_contacted',
                       'contacted_by')}),
    )
    list_display = ['submitted_time', 'has_been_contacted', 'zip_code',
                    'first_name', 'last_name']
    search_fields = [
        'first_name', 'last_name', 'primary_contact_phone_number',
        'hours_days_ok_to_contact_on_this_number',
        'any_alternate_numbers', 'street_address',
        'suite_or_apartment_number', 'city', 'state', 'zip_code',
        'hours_days_ok_to_volunteer', 'how_much_time_can_volunteer',
        'most_interested_in_volunteering_to_do',
        'email', 'facebook_name', 'twitter_handle', 'other_social_media',
        'member_of_syracuse_for_sanders_facebook', 'where_do_you_work',
        'what_skills_do_you_bring', 'member_of_any_community_groups'
    ]
    readonly_fields = ['submitted_time', 'contacted_by']

    def save_model(self, request, obj, form, change):

        if 'has_been_contacted' in form.changed_data and form.cleaned_data.get('has_been_contacted'):
            obj.contacted_by = request.user

        obj.save()

    def email_selected_users(self, request, queryset):
        recipient_list = ''

        for volunteer in queryset:

            if len(recipient_list) > 0:
                recipient_list = recipient_list + ', '

            recipient_list += volunteer.email

        request.session['recipient_list'] = recipient_list

        return redirect('s4semailvolunteers')

    email_selected_users.short_description = "Email all selected users"

admin.site.register(Volunteer, VolunteerAdmin)
