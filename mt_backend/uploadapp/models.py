from django.db import models
from django.core.validators import validate_image_file_extension
# Create your models here.


class File(models.Model):
    file = models.FileField(upload_to="uploads/file")


class ImageFile(models.Model):
    img_file = models.ImageField(
        upload_to="uploads/images/")
