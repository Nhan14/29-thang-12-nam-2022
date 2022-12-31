from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "project_cua_nhan.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import project_cua_nhan.users.signals  # noqa F401
        except ImportError:
            pass
