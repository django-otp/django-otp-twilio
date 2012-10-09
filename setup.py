#!/usr/bin/env python

from distutils.core import setup


setup(
    name='django-otp-twilio',
    version='0.1.1',
    description="A django-otp plugin that delivers tokens via Twilio's SMS service.",
    long_description=open('README').read(),
    author='Peter Sagerson',
    author_email='psagersDjwublJf@ignorare.net',
    packages=[
        'otp_twilio',
    ],
    url='https://bitbucket.org/psagers/django-otp',
    license='BSD',
    install_requires=[
        'django-otp',
        'requests',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
) 
