# Generated by Django 3.1.7 on 2021-04-10 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0003_realtyhost_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realtyhost',
            name='date_of_birth',
        ),
    ]
