from django.shortcuts import render
from rest_framework import viewsets,status
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveDestroyAPIView
from django.http import HttpResponse
from form_to_email.models import *
from form_to_email.serializers import *


# Create your views here.

def form(body):
    """
    
    Function to send email to the client

    """          
    subject = "New entry through the FSC app"
    from_email = settings.EMAIL_HOST_USER
    to_email = settings.EMAIL_RECIPIENT
    message = "{}".format(body)
    send_mail(subject = subject,message = message, from_email = from_email, recipient_list = to_email, fail_silently = False)

class FormToEmail(ListCreateAPIView):
    queryset = EmailBody.objects.all()
    serializer_class = EmailBodySerializer


# class DestroyForm(RetrieveDestroyAPIView):





        
