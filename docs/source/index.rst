django-otp-twilio
=================

.. include:: ../../README


Twilio SMS Devices
------------------

.. autoclass:: otp_twilio.models.TwilioSMSDevice
    :members:


Admin
-----

The following :class:`~django.contrib.admin.ModelAdmin` subclass is registered
with the default admin site. We recommend its use with custom admin sites as
well:

.. autoclass:: otp_twilio.admin.TwilioSMSDeviceAdmin


Settings
--------

.. setting:: OTP_TWILIO_ACCOUNT

**OTP_TWILIO_ACCOUNT**

Default: ``None``

Your Twilio account ID.


.. setting:: OTP_TWILIO_AUTH

**OTP_TWILIO_AUTH**

Default: ``None``

Your Twilio auth token.


.. setting:: OTP_TWILIO_FROM

**OTP_TWILIO_FROM**

Default: ``None``

The phone number to send SMS messages from. This must be one of your Twilio
numbers.


.. setting:: OTP_TWILIO_NO_DELIVERY

**OTP_TWILIO_NO_DELIVERY**

Default: ``False``

Send tokens to the 'otp_twilio.models' logger instead of delivering them by SMS.
Useful for development.


License
-------

.. include:: ../../LICENSE
