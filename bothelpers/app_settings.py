"""Settings for helpers."""

# Django
from django.apps import apps
from django.conf import settings

# put your app settings here
BOTHELPERS_COGS = getattr(
    settings,
    "BOTHELPERS_COGS",
    [
        "bothelpers.cogs.auth",
        "bothelpers.cogs.it",
        "bothelpers.cogs.links",
    ],
)


def securegroups_active():
    return apps.is_installed("securegroups")
