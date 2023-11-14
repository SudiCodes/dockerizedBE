from django.db import models
from authentication.models import Customer
# Create your models here.


class File(models.Model):
    file = models.FileField(upload_to="uploads/file")
    uploaded_by = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True)
    uploaded_on = models.DateTimeField(auto_now_add=True, null=True)
    uploaded_from = models.GenericIPAddressField(protocol="ipv4", null=True)


class ImageFile(models.Model):
    img_file = models.ImageField(
        upload_to="uploads/images/")
    uploaded_by = models.ForeignKey(
        Customer, on_delete=models.CASCADE, to_field='email', related_name='uploaded_images', null=True)
    uploaded_on = models.DateTimeField(auto_now_add=True, null=True)
    uploaded_from = models.GenericIPAddressField(protocol="IPv4", null=True)
