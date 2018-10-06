from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings


class PoolResource(models.Model):
    user = models.CharField("Owner", max_length=20, blank=False, null=False)
    name = models.CharField("Name", max_length=20, blank=False, null=False)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Object picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    description = models.CharField("Description", max_length=200, blank=True, null=True)
    avaiable = models.BooleanField("Available", default=True)

    class Meta:
        db_table = 'pool_resource'

class StoreResource(models.Model):
    user = models.CharField("Owner", max_length=20, blank=False, null=False)
    name = models.CharField("Name", max_length=20, blank=False, null=False)
    price = models.BigIntegerField("Price", blank=False, null=False)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Object picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    description = models.CharField("Description", max_length=200, blank=True, null=True)
    avaiable = models.BooleanField("Available", default=True)

    class Meta:
        db_table = 'pool_store'

class PoolCab(models.Model):
    user = models.CharField("Owner", max_length=20, blank=False, null=False)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    start = models.CharField("Start",default="IIITD", max_length=200, blank=False, null=False)
    end = models.CharField("End",default="IIITD", max_length=200, blank=False, null=False)
    waittime = models.DurationField("Wait time",blank=True, null=True)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Object picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    description = models.CharField("Description", max_length=200, blank=True, null=True)
    avaiable = models.BooleanField("Available", default=True)

    class Meta:
        db_table = 'pool_cab'


class PoolFood(models.Model):
    user = models.CharField("Order by", max_length=20, blank=False, null=False)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    what = models.CharField("What", max_length=200, blank=False, null=False)
    where = models.CharField("From Where", max_length=200, blank=False, null=False)
    waittime = models.BigIntegerField("Wait time")
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
        db_table = 'pool_food'