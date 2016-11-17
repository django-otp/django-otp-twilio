# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import otp_twilio.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TwilioSMSDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='The human-readable name of this device.', max_length=64)),
                ('confirmed', models.BooleanField(default=True, help_text='Is this device ready for use?')),
                ('number', models.CharField(help_text='The mobile number to deliver tokens to.', max_length=16)),
                ('key', models.CharField(default=otp_twilio.models.default_key, help_text='A random key used to generate tokens (hex-encoded).', max_length=40, validators=[otp_twilio.models.key_validator])),
                ('user', models.ForeignKey(help_text='The user that this device belongs to.', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Twilio SMS Device',
            },
            bases=(models.Model,),
        ),
    ]
