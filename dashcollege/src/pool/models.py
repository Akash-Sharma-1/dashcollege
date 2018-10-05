from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings


class PoolResource(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    description = models.CharField("Name", max_length=20, blank=False, null=False)
    picture = models.ImageField('Object picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    description = models.CharField("Description", max_length=200, blank=True, null=True)
    avaiable = models.BooleanField("Available", default=True)

    class Meta:
        abstract = True