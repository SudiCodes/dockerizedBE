# Generated by Django 4.2.2 on 2023-07-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=511, null=True),
        ),
    ]
