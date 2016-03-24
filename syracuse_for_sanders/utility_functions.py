from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import get_connection, EmailMultiAlternatives

from .models import FormRecipients


DEFAULT_SUBJECT = 'Automatic Notification from the KPH Intranet'
DEFAULT_NAME = 'form'


def send_submission_notification(form_recipient_type, subject=DEFAULT_SUBJECT, form_display_name=DEFAULT_NAME):
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = list(FormRecipients.objects.filter(type=form_recipient_type).values_list('user__email', flat=True))
    text_content = ('Automatic Notification from Organizers Hub\r\n'
                    'Another person has submitted the '+form_display_name+'.\r\n'
                    'Click here to login to the administration area '
                    'and view their submission:\r\n'
                    'https://organizershub/admin/')
    html_content = ('<h1>Automatic Notification from Organizers Hub'
                    '</h1><p>Another person has submitted the '+form_display_name+'.</p><p>'
                    '<a href="https://organizershub/admin/">'
                    'Click here to login to the administration area '
                    'and view their submission.</a></p>')

    with get_connection() as connection:
        message = EmailMultiAlternatives(subject,
                                         text_content,
                                         from_email,
                                         recipient_list,
                                         connection=connection)
        message.attach_alternative(html_content, "text/html")
        message.send()
