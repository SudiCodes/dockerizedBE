# mt_backend/management/commands/send_superuser_email.py

from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
import socket


class Command(BaseCommand):
    help = 'Send email with superuser details'

    def handle(self, *args, **options):
        container_name = socket.gethostname()
        # You can use any method to get the container ID
        container_id = socket.gethostname()
        superuser_password = settings.DJANGO_SUPERUSER_PASSWORD

        # Compose the email content
        subject = 'Superuser Details'
        message = f'Container Name: {container_name}\nContainer ID: {container_id}\nSuperuser Password: {superuser_password}'
        from_email = settings.DEFAULT_FROM_EMAIL
        # Specify the email address to receive the email
        recipient_list = [settings.SUPERUSER_EMAIL]

        # Send the email
        send_mail(subject, message, from_email, recipient_list)
