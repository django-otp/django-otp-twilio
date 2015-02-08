.. vim:ft=rst

This is a django-otp plugin that delivers tokens via Twilio's `SMS
<https://www.twilio.com/sms>`_ service.

See `django-otp <http://packages.python.org/django-otp>`_ for more information
on the OTP framework.

This version is supported on Python 2.6, 2.7, and 3.3+; and Django >= 1.4.

.. warning::

    otp_twilio now contains both South and Django migrations. If you're using
    South or upgrading to Django 1.7, please see the `upgrade notes`_ in the
    django-otp documentation first.

.. _upgrade notes: https://pythonhosted.org/django-otp/overview.html#upgrading
