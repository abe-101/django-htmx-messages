from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HtmxMessagesAppConfig(AppConfig):
    """App config for Django Htmx Messages."""

    name = "django_htmx_messages"
    verbose_name = _("htmx messages")
