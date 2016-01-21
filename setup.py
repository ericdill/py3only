#!/usr/bin/env python

from setuptools import setup

version = '1.0.0'

required = open('requirements.txt').read().split('\n')

setup(
    name='py3only',
    version=version,
    description= '',
    author='ericdill',
    author_email='edill@bnl.gov',
    url='https://github.com/ericdill/py3only',
    packages=['py3only'],
    install_requires=required,
    long_description='See ' + 'https://github.com/ericdill/py3only',
    license='MIT'
)
