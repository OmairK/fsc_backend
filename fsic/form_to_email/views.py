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


@api_view(['POST'])
def form(request):
    """
    Function to send email to the client
    """          
    subject = "New entry through the FSC app"
    from_email = settings.EMAIL_HOST_USER
    to_email = settings.EMAIL_RECIPIENT
    message = request.data
    send_mail(subject = subject,message = message, from_email = from_email, recipient_list =['abbasi.daniyal@gmail.com'], fail_silently = False)
# 
# def send_email(request):
#     subject = "New entry through the FSC app"
#     message = request.POST.get('message', '')
#     from_email = 'omairkhan064@gmail.com'
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, ['omairkhan064@.com'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponse('200')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse('Make sure all fields are entered and valid.')



# class FormToEmail(ListCreateAPIView):
#     queryset = EmailBody.objects.all()
#     serializer_class = EmailBodySerializer


# class DestroyForm(RetrieveDestroyAPIView):





        
