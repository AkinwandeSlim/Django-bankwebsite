
import requests
import re
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from django.core.mail import send_mail
from django.conf import settings
import json
import random
import json
from django.core.exceptions import ValidationError
import re

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

def generate_otp():
    return random.randint(100000, 999999)

def generate_unique_account_id():
    while True:
        account_id = '2' + ''.join([str(random.randint(0, 9)) for _ in range(9)])
        if not get_user_model().objects.filter(account_id=account_id).exists():
            return account_id

def send_otp_email(email,message,subject=None):
        user_email = email
        message=message
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=False,
        )



def is_valid_password(password, user):
    try:
        validate_password(password, user=user)
    except exceptions.ValidationError:
        return False
    return True


def is_valid_email(email):
    if get_user_model().objects.filter(email=email).exists():
        return False
    if not re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email):
        return False
    if email is None:
        return False
    return True
