# views.py
from django.core.mail import send_mail
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .models import Email
from django.conf import settings
from .serializers import EmailSerializer

class SendEmailView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EmailSerializer(data=request.data)

        if serializer.is_valid():
            # Save the email data to the database
            serializer.save()

            # Access the saved data
            to_email = serializer.data.get('to_email')
            subject = serializer.data.get('subject')
            message = serializer.data.get('message')

            # Send the email
            send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [to_email],
            fail_silently=False,
            html_message=message, )

            return JsonResponse({'status': 'success'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'status': 'error', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

