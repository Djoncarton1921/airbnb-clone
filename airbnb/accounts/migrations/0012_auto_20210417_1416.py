# Generated by Django 3.1.7 on 2021-04-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_profile_is_phone_number_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_phone_number_confirmed',
            field=models.BooleanField(default=False, verbose_name='is phone number confirmed'),
        ),
    ]
