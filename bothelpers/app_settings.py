"""Settings for helpers."""

# Django
from django.conf import settings

# put your app settings here
bothelpers_COGS = getattr(
    settings,
    "BOTHELPERS_COGS",
    [
        "bothelpers.cogs.auth",
        "bothelpers.cogs.it",
        "bothelpers.cogs.links",
    ],
)
