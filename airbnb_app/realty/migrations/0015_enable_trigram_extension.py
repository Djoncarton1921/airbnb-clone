# Generated by Django 3.1.13 on 2021-11-03 14:11

from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0014_auto_20211030_1331'),
    ]

    operations = [
        TrigramExtension(),
    ]
