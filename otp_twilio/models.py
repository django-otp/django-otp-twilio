from __future__ import absolute_import, division, print_function, unicode_literals

from binascii import unhexlify
import logging
import requests
import time

from django.core.exceptions import ImproperlyConfigured
from django.db import models

from django_otp.models import Device
from django_otp.oath import TOTP
from django_otp.util import random_hex, hex_validator

from .conf import settings


logger = logging.getLogger(__name__)


def default_key():
    return random_hex(20)


def key_validator(value):
    return hex_validator(20)(value)


class TwilioSMSDevice(Device):
    """
    A :class:`~django_otp.models.Device` that delivers codes via the Twilio SMS
    service. This uses TOTP to generate temporary tokens, which are valid for
    :setting:`OTP_TWILIO_TOKEN_VALIDITY` seconds. Once a given token has been
    accepted, it is no longer valid, nor is any other token generated at an
    earlier time.

    .. attribute:: number

        *CharField*: The mobile phone number to deliver to. `Twilio recommends
        <https://www.twilio.com/docs/api/rest/sending-messages>`_ using the
        `E.164 <http://en.wikipedia.org/wiki/E.164>`_ format. For US numbers,
        this would look like '+15555555555'. At the time of writing, Twilio
        will try to infer the correct E.164 format if it is not used, but this
        should not be relied upon.

    .. attribute:: key

        *CharField*: The secret key used to generate TOTP tokens.

    .. attribute:: last_t

        *BigIntegerField*: The t value of the latest verified token.

    """
    number = models.CharField(
        max_length=30,
        help_text="The mobile number to deliver tokens to (E.164)."
    )

    key = models.CharField(
        max_length=40,
        validators=[key_validator],
        default=default_key,
        help_text="A random key used to generate tokens (hex-encoded)."
    )

    last_t = models.BigIntegerField(
        default=-1,
        help_text="The t value of the latest verified token. The next token must be at a higher time step."
    )

    class Meta(Device.Meta):
        verbose_name = "Twilio SMS Device"

    @property
    def bin_key(self):
        return unhexlify(self.key.encode())

    def generate_challenge(self):
        """
        Sends the current TOTP token to ``self.number``.

        :returns: :setting:`OTP_TWILIO_CHALLENGE_MESSAGE` on success.
        :raises: Exception if delivery fails.

        """
        totp = self.totp_obj()
        token = format(totp.token(), '06d')
        message = settings.OTP_TWILIO_TOKEN_TEMPLATE.format(token=token)

        if settings.OTP_TWILIO_NO_DELIVERY:
            logger.info(message)
        else:
            self._deliver_token(message)

        challenge = settings.OTP_TWILIO_CHALLENGE_MESSAGE.format(token=token)

        return challenge

    def _deliver_token(self, token):
        self._validate_config()

        url = 'https://api.twilio.com/2010-04-01/Accounts/{0}/Messages.json'.format(settings.OTP_TWILIO_ACCOUNT)
        data = {
            'From': settings.OTP_TWILIO_FROM,
            'To': self.number,
            'Body': str(token),
        }

        response = requests.post(
            url, data=data,
            auth=(settings.OTP_TWILIO_ACCOUNT, settings.OTP_TWILIO_AUTH)
        )

        try:
            response.raise_for_status()
        except Exception as e:
            logger.exception('Error sending token by Twilio SMS: {0}'.format(e))
            raise

        if 'sid' not in response.json():
            message = response.json().get('message')
            logger.error('Error sending token by Twilio SMS: {0}'.format(message))
            raise Exception(message)

    def _validate_config(self):
        if settings.OTP_TWILIO_ACCOUNT is None:
            raise ImproperlyConfigured('OTP_TWILIO_ACCOUNT must be set to your Twilio account identifier')

        if settings.OTP_TWILIO_AUTH is None:
            raise ImproperlyConfigured('OTP_TWILIO_AUTH must be set to your Twilio auth token')

        if settings.OTP_TWILIO_FROM is None:
            raise ImproperlyConfigured('OTP_TWILIO_FROM must be set to one of your Twilio phone numbers')

    def verify_token(self, token):
        try:
            token = int(token)
        except Exception:
            verified = False
        else:
            totp = self.totp_obj()
            tolerance = settings.OTP_TWILIO_TOKEN_VALIDITY

            for offset in range(-tolerance, 1):
                totp.drift = offset
                if (totp.t() > self.last_t) and (totp.token() == token):
                    self.last_t = totp.t()
                    self.save()

                    verified = True
                    break
            else:
                verified = False

        return verified

    def totp_obj(self):
        totp = TOTP(self.bin_key, step=1)
        totp.time = time.time()

        return totp
