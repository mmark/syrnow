import os
from optparse import make_option

import re

import codecs
import csv

from django.conf import settings
from django.core.management.base import BaseCommand

FILE_PATH = '/home/markm/data/data_export.csv'
SKIPPED_FILE_NAME = 'skipped.csv'

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


def csv_unireader(filename, encoding="utf-8"):

    for row in csv.reader(codecs.iterencode(codecs.iterdecode(filename, encoding), "utf-8")):
        yield [e.decode("utf-8") for e in row]


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

    def handle(self, *args, **options):
        verbosity = int(options['verbosity'])
        errored_rows = []
        num_imported = 0
        num_skipped = 0

        if os.path.isfile(FILE_PATH):
            import_doc = csv_unireader(FILE_PATH)

            for cur_record in import_doc:
                num_imported += 1
                first_name = clean_string_titled_or_none(cur_record[0])
                last_name = clean_string_titled_or_none(cur_record[1])
                primary_contact_phone_number = clean_string(cur_record[3])
                hours_days_ok_to_contact_on_this_number = clean_string(cur_record[5])
                any_alternate_numbers = clean_string(cur_record[6])
                street_address = clean_string_titled_or_none(cur_record[7])
                suite_or_apartment_number = clean_string_titled_or_none(cur_record[8])
                city = clean_string_titled_or_none(cur_record[9])
                state = clean_string_upper_or_none(cur_record[10])
                zip_code = digits_or_none(cur_record[11])
                hours_days_ok_to_volunteer = clean_string(cur_record[12])
                how_much_time_can_volunteer = clean_string(cur_record[13])
                most_interested_in_volunteering_to_do = clean_string(cur_record[14])
                email = clean_string_lower_or_none(cur_record[15])
                facebook_name = clean_string_titled_or_none(cur_record[16])
                twitter_handle = clean_string(cur_record[17])
                other_social_media = clean_string(cur_record[18])
                member_of_syracuse_for_sanders_facebook = clean_string(cur_record[19])
                where_do_you_work = clean_string_titled_or_none(cur_record[20])
                what_skills_do_you_bring = clean_string(cur_record[21])
                member_of_any_community_groups = clean_string(cur_record[22])
                willing_to_volunteer_for_bernie_friendly_candidates = clean_string(cur_record[23])






