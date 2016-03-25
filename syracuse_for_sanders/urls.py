from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^email-volunteers/', email_list_of_volunteers, name='s4semailvolunteers'),
    url(r'^volunteer/success', S4SVolunteerSuccessView.as_view(), name='s4svolunteersuccess'),
    url(r'^volunteer', S4SVolunteerView.as_view(), name='s4svolunteer'),
    url(r'^$', S4SVolunteerView.as_view()),
]

RECAPTCHA_PUBLIC_KEY = '6LdcbxsTAAAAAJVVEIW7ljeXXJ6BwTlpvubsylix'
RECAPTCHA_PRIVATE_KEY = '6LdcbxsTAAAAAFgGowBRuMAiwgFqBGRolHzf_qgM'
