# Django
from django.conf import settings

# put your app settings here
LAWN_HELPERS_COGS = getattr(
    settings,
    "LAWN_HELPERS_COGS",
    [
        "lawn_helpers.cogs.auth",
        "lawn_helpers.cogs.it",
        "lawn_helpers.cogs.links",
    ],
)
