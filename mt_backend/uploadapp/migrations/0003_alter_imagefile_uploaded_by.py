# Generated by Django 4.2.2 on 2023-11-14 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uploadapp', '0002_file_uploaded_by_file_uploaded_from_file_uploaded_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefile',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_images', to=settings.AUTH_USER_MODEL, to_field='email'),
        ),
    ]
