#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='django-otp-twilio',
    version='1.0.3',
    description="A django-otp plugin that delivers tokens via Twilio's SMS service.",
    author="Peter Sagerson",
    author_email='psagers@ignorare.net',
    url='https://github.com/django-otp/django-otp-twilio',
    project_urls={
        "Documentation": 'https://django-otp-twilio.readthedocs.io/',
        "Source": 'https://github.com/django-otp/django-otp-twilio',
    },
    license='BSD',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
    ],

    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'django-otp >= 1.0.0',
        'requests',
    ],
)
