"""
App Models
Create your models in here
"""

# Django
from django.contrib.auth.models import Group
from django.db import models


class General(models.Model):
    """Meta model for app permissions"""

    class Meta:
        """Meta definitions"""

        managed = False
        default_permissions = ()
        permissions = (
            ("basic_access", "Basic access to this app"),
            ("it_commands", "Can use IT commands"),
        )


class Link(models.Model):
    description = models.TextField(max_length=500)
    name = models.CharField(max_length=255, null=False, unique=True)
    url = models.CharField(max_length=255, null=False)
    thumbnail = models.CharField(max_length=255)

    class Meta:
        default_permissions = ()
        permissions = (("manage_links", "Can manage links"),)

    def __str__(self):
        return self.name


class GroupWelcome(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    message = models.TextField()
    enabled = models.BooleanField(default=True)
    channel = models.BigIntegerField()

    class Meta:
        verbose_name = "Group Welcome Message"
        verbose_name_plural = "Group Welcome Messages"

    def __str__(self):
        return "Welcome Message: %s" % self.group.name
