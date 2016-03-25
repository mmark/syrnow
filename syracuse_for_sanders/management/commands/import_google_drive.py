import csv
import os
import re
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand

from syracuse_for_sanders.models import Volunteer

FILE_PATH = 'data_export.csv'
SKIPPED_FILE_NAME = 'skipped_log.csv'

# If DEBUG is not False then this will consume enormous amounts of memory
settings.DEBUG = False


def strip_non_ascii(string):
    """Returns the string without non ASCII characters"""
    stripped = (char for char in string if 0 < ord(char) < 127)

    return ''.join(stripped)


def clean_string(string):
    string = strip_non_ascii(string)

    return string.strip(' \t\n\r')


def clean_string_lower_or_none(string):
    string = clean_string(string).lower()

    if string == '':
        string = None

    return string


def clean_string_titled_or_none(string):
    string = clean_string(string).title()

    if string == '':
        string = None

    return string


def clean_digit_string(number):
    number = clean_string(number)

    return re.sub("\D", "", number)


def digits_or_none(number):
    number = clean_string(number)

    if number == '':
        number = None
    else:
        number = re.sub("\D", "", number)
        zeros_tester = re.compile(r'^[0]+$')

        if zeros_tester.search(number):
            number = None

    return number


def clean_string_upper_or_none(string):
    string = clean_string(string).upper()

    if string == '':
        string = None

    return string


class Command(BaseCommand):
    help = 'Imports CHF data from Google exported csv.'

    # make_option to save data to database
    option_list = BaseCommand.option_list + (
        make_option(
            '-s',
            '--save',
            dest='save',
            default=False,
            help='Do the full import, saving data to database.'),
    )

    def bool_val(self, value):
        return_value = False

        if value:
            value = value.lower()

            if value == 'yes' or value == 'y':
                return_value = True

        return return_value

    def handle(self, *args, **options):
        verbosity = int(options['verbosity'])

        if os.path.isfile(FILE_PATH):

            with open(FILE_PATH, "r+") as volunteer_file:
                csv_reader = csv.reader(volunteer_file)

                for cur_record in csv_reader:
                    first_name = clean_string_titled_or_none(cur_record[0])
                    last_name = clean_string_titled_or_none(cur_record[1])
                    primary_contact_phone_number = clean_string(cur_record[2])
                    hours_days_ok_to_contact_on_this_number = clean_string(cur_record[3])
                    any_alternate_numbers = clean_string(cur_record[4])
                    street_address = clean_string_titled_or_none(cur_record[5])
                    suite_or_apartment_number = clean_string_titled_or_none(cur_record[6])
                    city = clean_string_titled_or_none(cur_record[7])
                    state = clean_string_upper_or_none(cur_record[8])
                    zip_code = digits_or_none(cur_record[9])
                    hours_days_ok_to_volunteer = clean_string(cur_record[10])
                    how_much_time_can_volunteer = clean_string(cur_record[11])
                    most_interested_in_volunteering_to_do = clean_string(cur_record[12])
                    email = clean_string_lower_or_none(cur_record[13])
                    facebook_name = clean_string_titled_or_none(cur_record[14])
                    twitter_handle = clean_string(cur_record[15])
                    other_social_media = clean_string(cur_record[16])
                    member_of_syracuse_for_sanders_facebook = self.bool_val(cur_record[17])
                    where_do_you_work = clean_string_titled_or_none(cur_record[18])
                    what_skills_do_you_bring = clean_string(cur_record[19])
                    member_of_any_community_groups = clean_string(cur_record[20])
                    willing_to_volunteer_for_bernie_friendly_candidates = self.bool_val(cur_record[21])

                    try:
                        Volunteer.objects.create(
                            first_name=first_name,
                            last_name=last_name,
                            primary_contact_phone_number=primary_contact_phone_number,
                            hours_days_ok_to_contact_on_this_number=hours_days_ok_to_contact_on_this_number,
                            any_alternate_numbers=any_alternate_numbers,
                            street_address=street_address,
                            suite_or_apartment_number=suite_or_apartment_number,
                            city=city,
                            state=state,
                            zip_code=zip_code,
                            hours_days_ok_to_volunteer=hours_days_ok_to_volunteer,
                            how_much_time_can_volunteer=how_much_time_can_volunteer,
                            most_interested_in_volunteering_to_do=most_interested_in_volunteering_to_do,
                            email=email,
                            facebook_name=facebook_name,
                            twitter_handle=twitter_handle,
                            other_social_media=other_social_media,
                            member_of_syracuse_for_sanders_facebook=member_of_syracuse_for_sanders_facebook,
                            where_do_you_work=where_do_you_work,
                            what_skills_do_you_bring=what_skills_do_you_bring,
                            member_of_any_community_groups=member_of_any_community_groups,
                            willing_to_volunteer_for_bernie_friendly_candidates=willing_to_volunteer_for_bernie_friendly_candidates
                        )
                    except:

                        try:

                            with open(SKIPPED_FILE_NAME, "a+") as log_file:
                                cur_line = ",".join(cur_record)
                                log_file.write(cur_line+'\r\n')
                        except:

                            if verbosity == 2:
                                print("In last exception")




