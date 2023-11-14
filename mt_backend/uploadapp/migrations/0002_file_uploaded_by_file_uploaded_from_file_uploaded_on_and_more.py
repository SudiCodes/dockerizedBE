# Generated by Django 4.2.2 on 2023-11-14 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uploadapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='file',
            name='uploaded_from',
            field=models.GenericIPAddressField(null=True, protocol='ipv4'),
        ),
        migrations.AddField(
            model_name='file',
            name='uploaded_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='imagefile',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='imagefile',
            name='uploaded_from',
            field=models.GenericIPAddressField(null=True, protocol='IPv4'),
        ),
        migrations.AddField(
            model_name='imagefile',
            name='uploaded_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
