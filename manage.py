#!/usr/bin/env python

"""
Convenience wrapper for the test project. Suggested uses:

  ./manage.py test otp_twilio

  coverage run manage.py test otp_twilio

  ./manage.py makemigrations

"""

import os
import site
import sys


if __name__ == "__main__":
    site.addsitedir('test')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
