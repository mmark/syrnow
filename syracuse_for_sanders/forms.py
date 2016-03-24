from django.forms import ModelForm, TextInput, Textarea, NullBooleanSelect
from ckeditor.widgets import CKEditorWidget
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

from .models import *


class VolunteerEmailsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(VolunteerEmailsForm, self).__init__(*args, **kwargs)
        self.fields['message'].label = ''

    class Meta:
        model = VolunteerEmails
        fields = ['recipient_list', 'from_address', 'subject', 'message']
        widgets = {
            'recipient_list': Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'List of recipients that will receive this email',
                       'title': 'List of recipients that will receive this email',
                       'rows': 2}
            ),
            'from_address': TextInput(attrs={'class': 'form-control',
                                             'required': 'required',
                                             'placeholder': 'From, or reply to, email address',
                                             'title': 'From, or reply to, email address'}),
            'subject': TextInput(attrs={'class': 'form-control',
                                        'required': 'required',
                                        'placeholder': 'Subject line of email',
                                        'title': 'Subject line of email'}),
            'message': CKEditorWidget(config_name='default',
                                      attrs={'class': 'form-control',
                                             'required': 'required'})
        }

    def save(self, user=None, commit=True):
        instance = super(VolunteerEmailsForm, self).save(commit=False)

        if commit and user is not None:
            instance.sent_by = user
            instance.save()

        return instance


class VolunteerForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())

    class Meta:
        model = Volunteer
        fields = ['first_name', 'last_name', 'primary_contact_phone_number',
                  'hours_days_ok_to_contact_on_this_number',
                  'any_alternate_numbers', 'street_address',
                  'suite_or_apartment_number', 'city', 'state', 'zip_code',
                  'hours_days_ok_to_volunteer', 'how_much_time_can_volunteer',
                  'most_interested_in_volunteering_to_do', 'email',
                  'facebook_name', 'twitter_handle', 'other_social_media',
                  'member_of_syracuse_for_sanders_facebook',
                  'where_do_you_work', 'what_skills_do_you_bring',
                  'member_of_any_community_groups',
                  'willing_to_volunteer_for_bernie_friendly_candidates',
                  'captcha']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control',
                                           'required': 'required',
                                           'placeholder': 'Your first name',
                                           'title': 'Your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control',
                                          'required': 'required',
                                          'placeholder': 'Your last name',
                                          'title': 'Your last name'}),
            'primary_contact_phone_number': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Main number to call you on',
                       'title': 'Enter the main number you would like us to contact you on'}
            ),
            'hours_days_ok_to_contact_on_this_number': Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'What days and times are best to call you?',
                       'title': 'What are the best days and times to call you.',
                       'rows': 2}
            ),
            'any_alternate_numbers': Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Are there other phone numbers we should try?',
                       'title': 'Are there other phone numbers we should try?',
                       'rows': 2}
            ),
            'street_address': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Street address',
                       'title': 'Street address'}
            ),
            'suite_or_apartment_number': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Optional suite, PO Box or apartment number',
                       'title': 'Optional suite, PO Box or apartment number'}
            ),
            'city': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'City',
                       'title': 'City'}
            ),
            'state': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'State Abbreviated to 2 characters, like NY',
                       'title': 'State Abbreviated to 2 characters, like NY'}
            ),
            'zip_code': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Are there other phone numbers we should try?',
                       'title': 'Are there other phone numbers we should try?'}
            ),
            'hours_days_ok_to_volunteer': Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Normally which days do you have available to do volunteer work, and during which hours?',
                       'title': 'Normally which days do you have available to do volunteer work, and during which hours?',
                       'rows': 2}
            ),
            'how_much_time_can_volunteer': Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'On an average week how many hours would you be interested in volunteering?',
                       'title': 'On an average week how many hours would you be interested in volunteering?',
                       'rows': 2}
            ),
            'most_interested_in_volunteering_to_do': Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'What types of volunteer work most interest you? Examples: canvassing, phone banking',
                       'title': 'What types of volunteer work most interest you? Examples: canvassing, phone banking',
                       'rows': 6}
            ),
            'email': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'What email address should we use to contact you?',
                       'title': 'What email address should we use to contact you?'}
            ),
            'facebook_name': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'If you are on Facebook what is your username?',
                       'title': 'If you are on Facebook what is your username?'}
            ),
            'twitter_handle': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'If you are on Twitter what is your handle?',
                       'title': 'If you are on Twitter what is your handle?'}
            ),
            'other_social_media': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Any other social media accounts you can help us spread the Bern on?',
                       'title': 'Any other social media accounts you can help us spread the Bern on?'}
            ),
            'member_of_syracuse_for_sanders_facebook': NullBooleanSelect(
                attrs={'class': 'form-control',
                       'placeholder': 'Are you a member of Syracuse for Sanders Facebook group?',
                       'title': 'Are you a member of Syracuse for Sanders Facebook group?'}
            ),
            'where_do_you_work': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Where you work helps us understand what resources our volunteers might bring.',
                       'title': 'Where you work helps us understand what resources our volunteers might bring.'}
            ),
            'what_skills_do_you_bring': Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Everyone is unique, and we would like to know what types of skills you bring.',
                       'title': 'Everyone is unique, and we would like to know what types of skills you bring.',
                       'rows': 6}
            ),
            'member_of_any_community_groups': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Member of a local labor union or ANY OTHER community group?  This information might help.',
                       'title': 'Member of a local labor union OR ANY OTHER community group?  This information might help.',
                       'rows': 6}
            ),
            'willing_to_volunteer_for_bernie_friendly_candidates': NullBooleanSelect(
                attrs={'class': 'form-control',
                       'placeholder': 'Are you willing to also volunteer for other local Bernie friendly candidates?',
                       'title': 'Are you willing to also volunteer for other local Bernie friendly candidates?'}
            ),
        }
