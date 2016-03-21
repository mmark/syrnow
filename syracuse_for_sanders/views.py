from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic.base import TemplateView


from .utility_functions import send_submission_notification
from .models import Volunteer, FormRecipients
from .forms import VolunteerForm


class S4SVolunteerView(TemplateView):
    model = Volunteer
    form_class = VolunteerForm
    template_name = 'volunteer.html'
    success_url = 's4svolunteersuccess'
    email_subject = "New Volunteer Signup"
    form_display_name = 'Syracuse for Sanders New Volunteer Signup'

    def get_context_data(self, **kwargs):
        context = super(S4SVolunteerView, self).get_context_data(**kwargs)
        context['page_title'] = self.form_display_name
        context['extra_css'] = []
        context['extra_javascript'] = []
        context['display_name'] = self.form_display_name

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class()

        return render_to_response(self.template_name, context,
                                  context_instance=RequestContext(self.request))

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class(self.request.POST)

        if context['form'].is_valid():
            context['form'].save()
            send_submission_notification(
                form_recipient_type=FormRecipients.SUSPICIOUS_ACTIVITY_REPORT,
                subject=self.email_subject,
                form_display_name=self.form_display_name
            )

            return redirect(self.success_url)

        return render_to_response(self.template_name, context,
                                  context_instance=RequestContext(self.request))

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):

        return super(S4SVolunteerView, self).dispatch(*args, **kwargs)


class S4SVolunteerSuccessView(TemplateView):
    template_name = 'volunteer-success.html'

    def get_context_data(self, **kwargs):
        context = super(S4SVolunteerSuccessView, self).get_context_data(**kwargs)
        context['page_title'] = "Volunteer with Syracuse For Sanders - Success"
        context['extra_css'] = []
        context['extra_javascript'] = []

        return context

