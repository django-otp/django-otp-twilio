import re

from django.db import IntegrityError

from django_otp.oath import totp
from django_otp.tests import TestCase

from .conf import override_settings


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

    def test_current(self):
        device = self.alice.twiliosmsdevice_set.get()
        token = device.generate_challenge()
        ok = device.verify_token(token)

        self.assertTrue(ok)

    def test_previous(self):
        device = self.alice.twiliosmsdevice_set.get()
        token = totp(device.bin_key, t0=30)
        ok = device.verify_token(token)

        self.assertTrue(ok)

    def test_past(self):
        device = self.alice.twiliosmsdevice_set.get()
        token = totp(device.bin_key, t0=60)
        ok = device.verify_token(token)

        self.assertTrue(not ok)

    def test_future(self):
        device = self.alice.twiliosmsdevice_set.get()
        token = totp(device.bin_key, t0=-30)
        ok = device.verify_token(token)

        self.assertTrue(not ok)

    def test_cross_user(self):
        device = self.alice.twiliosmsdevice_set.get()
        token = device.generate_challenge()
        ok = self.bob.twiliosmsdevice_set.get().verify_token(token)

        self.assertTrue(not ok)

    @override_settings(OTP_TWILIO_TOKEN_TEMPLATE='Token is {token}')
    def test_format(self):
        device = self.alice.twiliosmsdevice_set.get()
        token = device.generate_challenge()
        match = re.match(r'Token is (\d{6})', token)

        self.assertTrue(match is not None)
        self.assertTrue(device.verify_token(match.group(1)))
