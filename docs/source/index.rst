django-otp-twilio
=================

.. include:: ../../README.rst


Installation
------------

django-otp-twilio can be installed via pip::

    pip install django-otp-twilio


Once installed it should be added to INSTALLED_APPS after django_otp core::

    INSTALLED_APPS = [
        ...
        'django_otp',
        'django_otp.plugins.otp_totp',
        'django_otp.plugins.otp_hotp',
        'django_otp.plugins.otp_static',

        'otp_twilio',
    ]


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

.. setting:: OTP_TWILIO_URL

**OTP_TWILIO_URL**

Default: ``"https://api.twilio.com""``

Twilio API URL. This can be used to change edge location

.. setting:: OTP_TWILIO_ACCOUNT

**OTP_TWILIO_ACCOUNT**

Default: ``None``

Your Twilio account ID.

.. setting:: OTP_TWILIO_API_KEY

**OTP_TWILIO_API_KEY**

Default: ``None``

Your Twilio API key, if no API key is specified requests are made using the Twilio Account ID.


.. setting:: OTP_TWILIO_AUTH

**OTP_TWILIO_AUTH**

Default: ``None``

Your Twilio auth token used for API requests. (Either API Key token or account auth token)


.. setting:: OTP_TWILIO_CHALLENGE_MESSAGE

**OTP_TWILIO_CHALLENGE_MESSAGE**

Default: ``"Sent by SMS"``

The message returned by
:meth:`~otp_twilio.models.TwilioSMSDevice.generate_challenge`. This may contain
``'{token}'``, which will be replaced by the token. This completely negates any
security benefit to the device, but it's handy for development, especially in
combination with :setting:`OTP_TWILIO_NO_DELIVERY`.


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


.. setting:: OTP_TWILIO_THROTTLE_FACTOR

**OTP_TWILIO_THROTTLE_FACTOR**

Default: ``1``

This controls the rate of throttling. The sequence of 1, 2, 4, 8... seconds is
multiplied by this factor to define the delay imposed after 1, 2, 3, 4...
successive failures. Set to ``0`` to disable throttling completely.


.. setting:: OTP_TWILIO_TOKEN_TEMPLATE

**OTP_TWILIO_TOKEN_TEMPLATE**

Default: ``"{token}"``

A string template for generating the token message. By default, this is just the
token itself, but you can customize it. The template will be rendered with
Python string formatting (``template.format(token=token)``).


.. setting:: OTP_TWILIO_TOKEN_VALIDITY

**OTP_TWILIO_TOKEN_VALIDITY**

Default: ``30``

The number of seconds for which a delivered token will be valid.


Changes
-------

:doc:`changes`


License
-------

.. include:: ../../LICENSE
