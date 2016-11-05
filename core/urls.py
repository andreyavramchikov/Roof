from django.conf.urls import url

from core.views import HomeView, ContactUsView, ServicesView, \
    AboutUsView, ProjectsView, RequestEstimateView, ProjectView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^contact/$', ContactUsView.as_view(), name='contact'),
    url(r'^services/$', ServicesView.as_view(), name='services'),
    url(r'^about/$', AboutUsView.as_view(), name='about'),
    url(r'^projects/$', ProjectsView.as_view(), name='projects'),
    url(r'^projects/(?P<pk>[0-9]+)/$', ProjectView.as_view(), name='project'),
    url(r'^request-estimate/$', RequestEstimateView.as_view(), name='request_estimate'),
]