#!/usr/bin/env python

from distutils.core import setup


setup(
    name='django-otp-twilio',
    version='0.3.0',
    description="A django-otp plugin that delivers tokens via Twilio's SMS service.",
    long_description=open('README.rst').read(),
    author='Peter Sagerson',
    author_email='psagersDjwublJf@ignorare.net',
    packages=[
        'otp_twilio',
    ],
    url='https://bitbucket.org/psagers/django-otp',
    license='BSD',
    install_requires=[
        'django-otp >= 0.3.0',
        'requests',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
    ],
)
