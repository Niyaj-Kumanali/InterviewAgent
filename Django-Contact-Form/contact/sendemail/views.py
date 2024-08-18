# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
import smtplib
import ssl
from email.message import EmailMessage

# Define email sender and receiver
email_sender = 'junaidpashaspatel@gmail.com'
email_password = 'zljpgtdqiiaxtise'
email_receiver = 'iamniyazahmad777@gmail.com'


# Add SSL (layer of security)
context = ssl.create_default_context()

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():

            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = from_email
            em['Subject'] = subject
            em.set_content(message)

            try:
                #send_mail(subject, message, from_email, ['admin@example.com'])
                # Log in and send the email
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender, from_email, em.as_string())
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('<h1 style="display: absolute; margin:25% 25% ; padding:0; font-size:3rem;">Success! Thank you for your message.</h1>')