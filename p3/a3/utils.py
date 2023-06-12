from django.template.loader import render_to_string 
from django.core.mail import EmailMessage, message
from django.conf import settings
def send_notification(mail_subject,mail_template,context):
    from_email =  settings.DEFAULT_FROM_EMAIL
    if(isinstance(context['reference'],str)):
        reid =  []
        reid.append(context['reference'])
    print("hii")
    message = render_to_string(mail_template,context)
    print("hii")
    mail = EmailMessage(mail_subject, message, from_email, to=[context['to_email']])
    mail.send(fail_silently=False)