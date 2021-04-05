from allauth.account.models import EmailAddress
from allauth.account.signals import email_confirmed

from django.http import HttpRequest
from django.dispatch import receiver
from django.contrib.auth.models import User, Group


@receiver(email_confirmed)
def add_user_to_group(request: HttpRequest, email_address: EmailAddress, **kwargs):
    user = User.objects.get(email=email_address.email)
    user.is_active = True
    common_users_group = Group.objects.get_or_create(name='common_users')[0]
    user.groups.add(common_users_group)
    user.save()
