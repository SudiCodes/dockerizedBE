from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.mail import send_mail
import os
import socket


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


# Create your models here.

class Customer(AbstractUser):
    email = models.EmailField(unique=True)
    comapny = models.CharField(max_length=256)
    schema = models.CharField(max_length=256)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            base_name = "{}.{}".format(
                self.first_name.lower(), self.last_name.lower())
            username = base_name
            counter = 1
            while Customer.objects.filter(username=username).exists():
                username = "{}{}".format(base_name, counter)
                counter += 1
            self.username = username

            user_email = self.email
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            # send mail with creds
            print("Sending mail on success...")
            send_mail(
                f'Superuser created - {username}',
                f'A Superuser has been created with below details:\n\n\n\n\n\temail: {user_email}\n\tpassword: {os.environ.get("DJANGO_SUPERUSER_PASSWORD")}\n\thostname: {hostname}\n\tIPv4 Address: {ip}\n\n\n',
                'send4sudi@outlook.in',
                ['sudiptasamalwhy@gmail.com'],
                fail_silently=False,
            )
            super().save(*args, **kwargs)
