from django.db import models

from django.contrib.auth.models import AbstractUser

from django_social_launch.models import SocialLaunchUserMixin


class User(SocialLaunchUserMixin, AbstractUser):
    pass
