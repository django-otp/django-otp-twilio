from copy import copy

import django.conf

import django.test.utils
from django.utils.six import iteritems


class Settings(object):
    """
    This is a simple class to take the place of the global settings object. An
    instance will contain all of our settings as attributes, with default values
    if they are not specified by the configuration.
    """
    defaults = {
        'OTP_TWILIO_ACCOUNT': None,
        'OTP_TWILIO_AUTH': None,
        'OTP_TWILIO_FROM': None,
        'OTP_TWILIO_NO_DELIVERY': False,
        'OTP_TWILIO_TOKEN_TEMPLATE': '{token}',
    }

    def __init__(self):
        """
        Loads our settings from django.conf.settings, applying defaults for any
        that are omitted.
        """
        for name, default in iteritems(self.defaults):
            value = getattr(django.conf.settings, name, default)
            setattr(self, name, value)


class override_settings(django.test.utils.override_settings):
    def enable(self):
        self._twilio_settings = copy(settings)
        for name, value in self.options.items():
            setattr(settings, name, value)

    def disable(self):
        for name in self.options:
            value = getattr(self._twilio_settings, name)
            setattr(settings, name, value)
        self._twilio_settigs = None


settings = Settings()
