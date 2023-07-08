from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
import os
import socket


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, is_admin=False, password=None):
        """
        Creates and saves a User with the given email, name and password.
        """
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_admin=is_admin
        )
        user.is_staff = user.is_admin
        user.username = user.get_custom_username()
        user.password = make_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        """
        Creates and saves a Superuser with the given email, name and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = user.is_admin
        # Send mail with creds for superuser
        print("Sending mail on success...")
        send_mail(
            f'Superuser created - {user.username}',
            f'A Superuser has been created with below details:\n\n\n\n\n\temail: {user.email}\n\tpassword: {os.environ.get("DJANGO_SUPERUSER_PASSWORD")}\n\thostname: {socket.gethostname()}\n\tIPv4 Address: {socket.gethostbyname(socket.gethostname())}\n\n\n',
            'send4sudi@outlook.in',
            ['sudiptasamalwhy@gmail.com'],
            fail_silently=False,
        )
        user.save()
        return user


# Custom User Model.
class Customer(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email',
                              max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=511, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + self.last_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_custom_username(self):
        if not self.pk:
            base_name = "{}.{}".format(
                self.first_name.lower(), self.last_name.lower())
            username = base_name
            counter = 1
            while Customer.objects.filter(username=username).exists():
                username = "{}{}".format(base_name, counter)
                counter += 1
            return username
