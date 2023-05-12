from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import TwilioSMSDevice


class TwilioSMSDeviceAdmin(admin.ModelAdmin):
    """
    :class:`~django.contrib.admin.ModelAdmin` for
    :class:`~otp_twilio.models.TwilioSMSDevice`.
    """

    fieldsets = [
        (
            'Identity',
            {
                'fields': ['user', 'name', 'confirmed'],
            },
        ),
        (
            'Configuration',
            {
                'fields': ['number'],
            },
        ),
    ]
    raw_id_fields = ['user']


try:
    admin.site.register(TwilioSMSDevice, TwilioSMSDeviceAdmin)
except AlreadyRegistered:
    # Ignore the useless exception from multiple imports
    pass
