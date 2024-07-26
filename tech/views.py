from django.shortcuts import render, HttpResponseRedirect
from .forms import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def index (request):
    submitted = False
    if request.POST:
        form = ContactForm(request.POST)
        email = request.POST['email']
        name = request.POST['name']
        subject = request.POST['subject']

        if form.is_valid():
            send_mail(
                f'Sub: {subject}' , #title
                f'Dear {name}, if you are receiving this mail, you have successfully received your submission. We are glad that you have decide to use our services. A member of the support team will reply your and help solve the issue(s). Responses takes 4 to 8 hours.', # message
                settings.EMAIL_HOST_USER,
                [ email, 'stephanas.odogu@cybria.tech'],#receivers email
                fail_silently=False

            )
            form.save()

            return HttpResponseRedirect("/becomeadeveloper?submitted=True")
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'index.html',{
        'form' : ContactForm(),
        "submitted" : submitted
    })
  

def becomeadeveloper(request):
    submitted = False
    if request.POST:
        form = BecomeadeveloperForm(request.POST)
        email = request.POST['email']
        name = request.POST['firstname']
        skill = request.POST['skills']
        if form.is_valid():
           
           send_mail(
                f'Sub: {name} want to become a developer' , #title
                f'Dear {name}, if you are receiving this mail, you have successfully received your submission. We are glad that you have decide to that you want join the vast growing fields in tech.\
                 you can make payments to the account below and send the reciept to this same mail line, so we can keep track of it.\
                 Bank Name = KUDA BANK\
                 \
                 Account Name =  Stephanas Odogu\
                 \
                 Account Number = 2010718265\
                 \
                 A member of the support team will reply your and help solve the issue(s). Responses takes 4 to 8 hours.', # message
                settings.EMAIL_HOST_USER,
                [ email, 'stephanas.odogu@cybria.tech'],#receivers email
                fail_silently=False )
           
           form.save()
           
           return HttpResponseRedirect("/becomeadeveloper?submitted=True")
    else:
        form = BecomeadeveloperForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'becomeadeveloper.html',{
        'form' : BecomeadeveloperForm(),
        "submitted" : submitted
    })
  