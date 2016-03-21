from django.forms import ModelForm, TextInput, Textarea, Select
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Volunteer


class VolunteerForm(ModelForm):

    class Meta:
        model = Volunteer
        fields = ['first_name', 'last_name', 'primary_contact_phone_number',
                  'hours_days_ok_to_contact_on_this_number',
                  'any_alternate_numbers', 'zip_code',
                  'hours_days_ok_to_volunteer', 'how_much_time_can_volunteer',
                  'most_interested_in_volunteering_to_do', 'email',
                  'facebook_name', 'twitter_handle', 'other_social_media',
                  'member_of_syracuse_for_sanders_facebook',
                  'where_do_you_work', 'what_skills_do_you_have',
                  'member_of_any_unions']
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
                       'title': 'What are the best days and times to call you.'}
            ),
            'any_alternate_numbers': Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Are there other phone numbers we should try?',
                       'title': 'Are there other phone numbers we should try?'}
            ),
        }
