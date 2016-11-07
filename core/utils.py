from django.core.mail import send_mail
from django.template.loader import render_to_string

CONTACT = 'CONTACT'
ESTIMATE = 'ESTIMATE'


def send_email_to_michael(data, email_type):
    if email_type == ESTIMATE:
        title = u'New request for estimate'
        msg_plain = render_to_string('email_request_estimate.txt', {'data': data})
        msg_html = render_to_string('email_request_estimate.html', {'data': data})
    else:
        title = u'Contact Us request'
        msg_plain = render_to_string('email_contact_us.txt', {'data': data})
        msg_html = render_to_string('email_contact_us.html', {'data': data})

    send_mail(
        title,
        msg_plain,
        'solutioncontractor3@gmail.com',
        ['solutioncontractor3@gmail.com'],
        html_message=msg_html,
    )
