from django.contrib.auth.models import AbstractUser
from django.db import models


class AuthUser(AbstractUser):
    social_thumb = models.URLField(null=True, blank=True)
