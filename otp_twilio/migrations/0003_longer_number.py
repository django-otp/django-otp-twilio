# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_twilio', '0002_last_t'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twiliosmsdevice',
            name='number',
            field=models.CharField(help_text='The mobile number to deliver tokens to.', max_length=30),
        ),
    ]
