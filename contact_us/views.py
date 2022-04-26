from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views import View
from . import forms
from django.urls import reverse
from . import models
from django.core.mail import send_mail

# Create your views here


class ContactUsView(View):
    def get(self, request: HttpRequest):
        ack = request.GET.get('ack', '0')
        form = forms.ContactUsForm()

        context = dict(ack=ack, form=form)

        return render(request, 'contact_us/contact_us.html', context)

    def post(self, request: HttpRequest):
        form = forms.ContactUsForm(data=request.POST)
        if form.is_valid():
            # save the form
            contact_request: models.ContactUsInfo = form.save()

            # create email
            message = """
            [Contact Request]

            User Email: %s

            Full Name: %s

            [Query]
            %s
            """ % (contact_request.email, contact_request.fullname, contact_request.query)

            # send email
            send_mail(
                subject='Contact Request',
                message=message,
                recipient_list=['sameshipilla94@gmail.com'],
                from_email=None,
                fail_silently=False
            )

            url = '%s?ack=1' % reverse("contact_us:contact-us")
            return redirect(url)

        context = dict(form=form, ack='0')
        return render(request, 'contact_us/contact_us.html', context)