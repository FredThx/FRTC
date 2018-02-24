#!/usr/bin/env python
# -*- coding:utf-8 -*
#from setuptools import setup
from distutils.core import setup

import FRTC

setup(
    name='FRTC',
    version=FRTC.__version__,
#	packages=find_packages(),
	author="FredThx",
	author_email="FredThx@gmail.com",
	description="DS1302 and NTP sync on Raspberry pi",
    long_description=open('README.md').read(),
    license='MIT',
    url='https://github.com/FredThx/FRTC',
    platforms='any',
    py_modules=[
        'FRTC'
    ],
    scripts=[
        'scripts/ds1302_ntp_sync'
    ]
)