from django.contrib.auth.models import User
from django.test import TestCase

from django_otp.oath import totp


class TestTwilioSMS(TestCase):
    fixtures = ['tests/alice_and_bob']

    def setUp(self):
        self.alice = User.objects.get(username='alice')
        self.bob = User.objects.get(username='bob')

    def test_current(self):
        device = self.alice.twiliosmsdevice_set.get()
        token = device.generate_challenge()
        ok = device.verify_token(token)

        self.assert_(ok)

    def test_previous(self):
        device = self.alice.twiliosmsdevice_set.get()
        token = totp(device.bin_key, t0=30)
        ok = device.verify_token(token)

        self.assert_(ok)

    def test_past(self):
        device = self.alice.twiliosmsdevice_set.get()
        token = totp(device.bin_key, t0=60)
        ok = device.verify_token(token)

        self.assert_(not ok)

    def test_future(self):
        device = self.alice.twiliosmsdevice_set.get()
        token = totp(device.bin_key, t0=-30)
        ok = device.verify_token(token)

        self.assert_(not ok)

    def test_cross_user(self):
        device = self.alice.twiliosmsdevice_set.get()
        token = device.generate_challenge()
        ok = self.bob.twiliosmsdevice_set.get().verify_token(token)

        self.assert_(not ok)
