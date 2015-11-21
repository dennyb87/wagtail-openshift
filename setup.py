#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='wagtail-openshift',
    # GETTING-STARTED: set your app version:
    version='0.1',
    # GETTING-STARTED: set your app description:
    description='Wagtail on Openshift',
    # GETTING-STARTED: set author name (your name):
    author='Denny Baldini',
    # GETTING-STARTED: set author email (your email):
    author_email='dennybaldini@gmail.com',
    # GETTING-STARTED: define required django version:
    install_requires=['wagtail==1.2'],
)
