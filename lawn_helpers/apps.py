"""App Configuration"""

# Third Party
# AA Example App
# Django
from django.apps import AppConfig

# LAWN Helpers
from lawn_helpers import __version__


class ExampleConfig(AppConfig):
    """App Config"""

    name = "lawn_helpers"
    label = "lawn_helpers"
    verbose_name = f"Lawn Helpers v{__version__}"

    def ready(self):
        # LAWN Helpers
        import lawn_helpers.signals  # noqa: F401
