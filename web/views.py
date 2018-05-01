#from django.shortcuts import render
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

def deactivate_users():
    users = User.objects.all()
    for user in users:
        if not user.is_staff and timezone.now() > user.date_joined + datetime.timedelta(days=5):
            user.is_active = False
            user.save()
# Create your views here.
