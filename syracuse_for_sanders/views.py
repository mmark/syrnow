from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_protect
from django.views.generic.base import TemplateView
from django.utils.http import urlunquote


from .utility_functions import send_submission_notification
from .models import Volunteer, FormRecipients, VolunteerSuccess
from .forms import VolunteerForm, VolunteerEmailsForm


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
                form_recipient_type=FormRecipients.S4S_Volunteer_Profile,
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

        try:
            thank_you = VolunteerSuccess.objects.filter(
                is_active=True,
                last_edited__lt=timezone.now()).order_by('-last_edited').first()
        except:
            thank_you = "Thank you for volunteering to join our " \
                        "grassroots movement for Bernie Sanders.  " \
                        "Please jump in and " \
                        "<a href='http://syracuseforsanders.com/events/'>" \
                        "start coming to some events!</a>"

        context['thank_you_text'] = thank_you

        return context


@csrf_protect
@login_required
@staff_member_required
def email_list_of_volunteers(request,):
    context = {}
    form_class = VolunteerEmailsForm
    template_name = 'email-list-of-volunteers.html'
    recipient_list = request.session.get('recipient_list', False)

    if request.method == 'POST':
        context['form'] = form_class(request.POST)

        if context['form'].is_valid():
            context['form'].save(user=request.user)
            from_email = context['form'].cleaned_data.get('from_address')
            to_emails = context['form'].cleaned_data.get('recipient_list')
            to_emails = to_emails.split(',')
            html_message = context['form'].cleaned_data.get('message')
            text_message = strip_tags(html_message)
            subject = context['form'].cleaned_data.get('subject')
            success = 'Sent'
            failed = 'Failed to Send'
            results = []
            result_string = ''

            for email in to_emails:
                this_result = {}
                to_email = email.strip()
                result = send_mail(subject, text_message, from_email, [to_email], html_message=html_message)

                if result:
                    this_result[to_email] = success
                    result_string = result_string + to_email + ': ' + success  + ' '
                else:
                    this_result[to_email] = failed
                    result_string = result_string + to_email + ': ' + failed  + ' '

                results.append(this_result)

            context['results'] = results
            context['form'].results = result_string
            context['form'].save()

        return render_to_response(template_name,
                                  context,
                                  context_instance=RequestContext(request))

    else:
        initial = {'recipient_list': recipient_list}
        context['form'] = form_class(initial=initial)

    return render_to_response(template_name,
                              context,
                              context_instance=RequestContext(request))
