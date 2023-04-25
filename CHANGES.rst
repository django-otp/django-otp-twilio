v1.0.3 - April 25, 2023 - Fix API key handling
--------------------------------------------------------------------------------

Fix `#6`_: Code uses "TWILIO_API_KEY" instead of "OTP_TWILIO_API_KEY"

.. _#6: https://github.com/django-otp/django-otp-twilio/pull/6


v1.0.2 - April 11, 2023 - New configuration options
--------------------------------------------------------------------------------

- Allow configuration of API URL and API key.


v1.0.1 - November 29, 2021 - Forward compatibility
--------------------------------------------------------------------------------

Default to AutoField to avoid spurious migrations.


v1.0.0 - August 13, 2020 - Update test matrix
------------------------------------------------------------

- Added Django 3.1 to the test environments and fixed deprecation warnings.

- Version bumped to align with the core django-otp project.


v0.6.0 - May 06, 2020 - ThrottlingMixin and SideChannelDevice
-------------------------------------------------------------------------------

TwilioSMSDevice is now a :class:`~django_otp.models.SideChannelDevice` and
implements :class:`~django_otp.models.ThrottlingMixin`.

This also drops support for old versions of Python (2.7) and Django (1.11,
2.1).

Note that this version includes migrations that will invalidate any in-flight
tokens.


v0.5.1 - August 26, 2019 - Housekeeping
---------------------------------------

Build, test, and documentation cleanup.


v0.5.0 - August 14, 2018 - Django 2.1 support
---------------------------------------------

- Drop support for Django < 1.11.


v0.4.2 - October 18, 2017 - Fix migration
-----------------------------------------

- Fix a spurious migration offered by makemigrations.


v0.4.1 - August 29, 2017 - Default keys
---------------------------------------

- Fix `#25`_: make sure default keys are unicode values.

.. _#25: https://bitbucket.org/psagers/django-otp/issues/25/attributeerror-bytes-object-has-no


v0.4.0 - July 19, 2017 - Update support matrix
----------------------------------------------

- Drop support for versions of Django that are past EOL.


v0.3.6 - November 27, 2016 - Forward compatbility for Django 2.0
----------------------------------------------------------------

- Treat :attr:`~django.contrib.auth.models.User.is_authenticated` and
  :attr:`~django.contrib.auth.models.User.is_anonymous` as properties in Django
  1.10 and later.

- Add explict on_delete behavior for all foreign keys.


v0.3.5 - October 9, 2016 - Longer numbers
-----------------------------------------

- Support longer phone numbers.


v0.3.4 - January 10, 2016 - Python 3 cleanup
--------------------------------------------

- All modules include all four Python 3 __future__ imports for consistency.

- Migrations no longer have byte strings in them.


v0.3.3 - October 11, 2015 - Django 1.8
--------------------------------------

- Use ModelAdmin.raw_id_fields for foreign keys to users.

- General cleanup and compatibility with Django 1.9a1.


v0.3.1 - March 1, 2015 - Token validity
---------------------------------------

- The length of time that tokens are valid can now be configured with
  :setting:`OTP_TWILIO_TOKEN_VALIDITY`.

- Tokens now become invalid as soon as they have been verified.


v0.3.0 - February 7, 2015 - Support Django migrations
-----------------------------------------------------

- otp_twilio now has both Django and South migrations. Please see the `upgrade
  notes`_ for details on upgrading from previous versions.

.. _upgrade notes: https://pythonhosted.org/django-otp/overview.html#upgrading


v0.2.2 - Aug 20, 2014 - Challenge template
------------------------------------------

- :setting:`OTP_TWILIO_CHALLENGE_MESSAGE` allows you to customize the string
  returned to the user after the SMS is sent. It also accepts the {token}
  placeholder as a convenience for development.

- Fixes for unit tests under the latest pre-release version of Django 1.7.


v0.2.1 - May 8, 2014 - Message template
---------------------------------------

- :setting:`OTP_TWILIO_TOKEN_TEMPLATE` allows you to customize the message that
  is sent by SMS.


v0.2.0 - November 10, 2013 - Django 1.6
---------------------------------------

- Now supports Django 1.4 to 1.6 on Python 2.6, 2.7, 3.2, and 3.3. This is the
  first release for Python 3.


v0.1.3 - May 9, 2013 - Unit test improvements
---------------------------------------------

Major unit test cleanup. Tests should pass or be skipped under all supported
versions of Django, with or without custom users and timzeone support.


v0.1.2 - March 24, 2013 - Bug fix
---------------------------------

- Fix for requests integration.


v0.1.1 - October 8, 2012 - Bug fix
----------------------------------

- Fix exception with an empty token form.


v0.1.0 - August 20, 2012 - Initial Release
------------------------------------------

Initial release.
