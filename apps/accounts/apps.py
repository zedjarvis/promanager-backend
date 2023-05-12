from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.accounts"
    verbose_name = _("Accounts")

    def ready(self) -> None:
        try:
            import apps.accounts.signals  # noqa: F401
        except ImportError:
            pass
