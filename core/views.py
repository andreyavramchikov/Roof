# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy

from core.form import RequestEstimateForm


class HomeView(TemplateView):
    template_name = 'pages/index.html'


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'


class ServicesView(TemplateView):
    template_name = 'pages/services.html'


class ProjectsView(TemplateView):
    template_name = 'pages/projects.html'


class ContactUsView(TemplateView):
    template_name = 'pages/contact_us.html'


class RequestEstimateView(FormView):
    form_class = RequestEstimateForm
    success_url = reverse_lazy('home')
    template_name = 'pages/request_estimate.html'

    def send_email_to_michael(self, phone, email, address, message):
        pass

    def form_valid(self, form):
        data = form.data
        # send message if form valid here
        phone = data['phone']
        email = data['email']
        address = data['address']
        message = data['message']
        self.send_email_to_michael(phone, email, address, message)
        return super(RequestEstimateView, self).form_valid(form)



