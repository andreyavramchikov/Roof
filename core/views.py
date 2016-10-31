# Create your views here.
from django.views.generic.base import TemplateView


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


class RequestEstimateView(TemplateView):
    template_name = 'pages/request_estimate.html'



