from django.shortcuts import render
from rest_framework import viewsets, status
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import smtplib
import json


@api_view(['POST'])
def form(request):
    """
    Function to send email to the client regarding CIEN Form
    """
    subject = "New entry through the FSC app"
    from_email = settings.EMAIL_USER
    to_email = settings.EMAIL_RECIPIENT
    body = request.data

    message = '\n'.join(['%s : %s' % (key, value)
                            for (key, value) in body.items()])

    if subject and message:
        try:
            send_mail(subject, message,
                      from_email, [(to_email)],
                      fail_silently=False)
            return Response(status=status.HTTP_200_OK)
        except BadHeaderError:
            content = {'Try again': 'Try again'}
            return Response(content, status=status.HTTP_404_BAD_REQUEST)
