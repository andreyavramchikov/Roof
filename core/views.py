# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy


from core.form import RequestEstimateForm, ContactUsForm
from core.models import Project
from core.utils import send_email_to_michael, ESTIMATE, CONTACT


class HomeView(TemplateView):
    template_name = 'pages/index.html'


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'


class ServicesView(TemplateView):
    template_name = 'pages/services.html'


class ProjectsView(TemplateView):
    template_name = 'pages/projects.html'


class ProjectView(DetailView):
    model = Project
    template_name = 'pages/project.html'
    context_object_name = 'project'


class ContactUsView(FormView):
    form_class = ContactUsForm
    success_url = reverse_lazy('home')
    template_name = 'pages/contact_us.html'

    def form_valid(self, form):
        send_email_to_michael(form.data, email_type=CONTACT)
        return super(ContactUsView, self).form_valid(form)


class RequestEstimateView(FormView):
    form_class = RequestEstimateForm
    success_url = reverse_lazy('home')
    template_name = 'pages/request_estimate.html'

    def form_valid(self, form):
        send_email_to_michael(form.data, email_type=ESTIMATE)
        return super(RequestEstimateView, self).form_valid(form)



