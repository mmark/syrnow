from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^volunteer/success', views.S4SVolunteerSuccessView.as_view(), name='s4svolunteersuccess'),
    url(r'^volunteer', views.S4SVolunteerView.as_view(), name='s4svolunteer'),
]
