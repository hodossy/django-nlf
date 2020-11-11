from django.conf import settings as dj_settings
from django.core.signals import setting_changed
from django.utils.translation import gettext_lazy as _

from .utils import deprecate

DEFAULTS = {
    "QUERY_PARAM": "q",
    "PATH_SEPARATOR": ".",
    "EMPTY_VALUE": "EMPTY",
}


DEPRECATED_SETTINGS = [
]


def is_callable(value):
    # check for callables, except types
    return callable(value) and not isinstance(value, type)


class Settings:

    def __getattr__(self, name):
        if name not in DEFAULTS:
            msg = "'%s' object has no attribute '%s'"
            raise AttributeError(msg % (self.__class__.__name__, name))

        value = self.get_setting(name)

        if is_callable(value):
            value = value()

        # Cache the result
        setattr(self, name, value)
        return value

    def get_setting(self, setting):
        django_setting = 'NLF_%s' % setting

        if setting in DEPRECATED_SETTINGS and hasattr(dj_settings, django_setting):
            deprecate("The '%s' setting has been deprecated." % django_setting)

        return getattr(dj_settings, django_setting, DEFAULTS[setting])

    def change_setting(self, setting, value, enter, **kwargs):
        if not setting.startswith('NLF_'):
            return
        setting = setting[4:]  # strip 'NLF_'

        # ensure a valid app setting is being overridden
        if setting not in DEFAULTS:
            return

        # if exiting, delete value to repopulate
        if enter:
            setattr(self, setting, value)
        else:
            delattr(self, setting)


settings = Settings()
setting_changed.connect(settings.change_setting)
