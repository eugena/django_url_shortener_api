from __future__ import unicode_literals
import random
import string

from django.db import models
from django.conf import settings


def get_code():
    """
    Randomly generates unique short code
    """
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase

    while True:
        short_id = ''.join(random.choice(char)
                           for x in range(settings.CODE_LENGTH))
        try:
            Link.objects.get(pk=short_id)
        except:
            return short_id


class Link(models.Model):
    """
    Model that represents a shortened URL
    """
    code = models.CharField(
        max_length=settings.CODE_LENGTH,
        primary_key=True,
        default=get_code)
    url = models.URLField()
    target = models.CharField(
        max_length=1,
        choices=settings.DEVICE_TYPES,
        default=settings.TYPE_DESKTOP)
    created = models.DateTimeField(auto_now_add=True)
    qty = models.PositiveIntegerField(
        verbose_name="Number of Redirects",
        default=0)

    class Meta:
        get_latest_by = 'created'
