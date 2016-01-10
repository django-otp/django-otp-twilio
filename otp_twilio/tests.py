from __future__ import absolute_import, division, print_function, unicode_literals

import re

from django.db import IntegrityError
from django.test.utils import override_settings

from django_otp.tests import TestCase

from .conf import settings


@override_settings(
    OTP_TWILIO_NO_DELIVERY=True,
    OTP_TWILIO_CHALLENGE_MESSAGE='{token}',
)
class TestTwilioSMS(TestCase):
    def setUp(self):
        try:
            self.alice = self.create_user('alice', 'password')
            self.bob = self.create_user('bob', 'password')
        except IntegrityError:
            self.skipTest("Unable to create test users.")
        else:
            self.alice.twiliosmsdevice_set.create(number='test',
                                                  key='01234567890123456789')
            self.bob.twiliosmsdevice_set.create(number='test',
                                                key='98765432109876543210')

        self._now = 1420099200
        self._delivered = None

    def test_instant(self):
        """ Verify a code the instant it was generated. """
        device = self.alice.twiliosmsdevice_set.get()
        with self.with_time(self._now):
            token = device.generate_challenge()
            ok = device.verify_token(token)

        self.assertTrue(ok)

    def test_barely_made_it(self):
        """ Verify a code at the last possible second. """
        device = self.alice.twiliosmsdevice_set.get()
        with self.with_time(self._now):
            token = device.generate_challenge()
        with self.with_time(self._now + settings.OTP_TWILIO_TOKEN_VALIDITY):
            ok = device.verify_token(token)

        self.assertTrue(ok)

    def test_too_late(self):
        """ Try to verify a code one second after it expires. """
        device = self.alice.twiliosmsdevice_set.get()
        with self.with_time(self._now):
            token = device.generate_challenge()
        with self.with_time(self._now + settings.OTP_TWILIO_TOKEN_VALIDITY + 1):
            ok = device.verify_token(token)

        self.assertFalse(ok)

    def test_future(self):
        """ Try to verify a code from the future. """
        device = self.alice.twiliosmsdevice_set.get()
        with self.with_time(self._now + 1):
            token = device.generate_challenge()
        with self.with_time(self._now):
            ok = device.verify_token(token)

        self.assertFalse(ok)

    def test_code_reuse(self):
        """ Try to verify the same code twice. """
        device = self.alice.twiliosmsdevice_set.get()
        with self.with_time(self._now):
            token = device.generate_challenge()
            ok1 = device.verify_token(token)
            ok2 = device.verify_token(token)

        self.assertTrue(ok1)
        self.assertFalse(ok2)

    def test_cross_user(self):
        device = self.alice.twiliosmsdevice_set.get()
        with self.with_time(self._now):
            token = device.generate_challenge()
            ok = self.bob.twiliosmsdevice_set.get().verify_token(token)

        self.assertFalse(ok)

    @override_settings(
        OTP_TWILIO_NO_DELIVERY=False,
        OTP_TWILIO_TOKEN_TEMPLATE='Token is {token}',
    )
    def test_format(self):
        device = self.alice.twiliosmsdevice_set.get()
        with self._patch('otp_twilio.models.TwilioSMSDevice._deliver_token', self._deliver_token):
            device.generate_challenge()
        match = re.match(r'^Token is (\d{6})$', self._delivered)

        self.assertTrue(match is not None)
        self.assertTrue(device.verify_token(match.group(1)))

    #
    # Utilities
    #

    def _deliver_token(self, token):
        self._delivered = token

    def with_time(self, timestamp):
        return self._patch('time.time', lambda: timestamp)

    def _patch(self, *args, **kwargs):
        try:
            from unittest import mock
        except ImportError:
            try:
                import mock
            except ImportError:
                self.skipTest("mock is not installed")

        return mock.patch(*args, **kwargs)
